import os
import sys

# Prevent crashes under pythonw when warnings/prints occur without console handles
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")

import time
import subprocess
import warnings
warnings.filterwarnings("ignore")

from src.steelseries import SteelSeriesLEDController
from src.razer import RazerChromaLEDController

LOCK_FILE = os.path.join(os.environ.get("TEMP", "C:\\Temp"), "rgb_led_controller.pid")
LOG_FILE = os.path.join(os.environ.get("TEMP", "C:\\Temp"), "rgb_led_controller.log")

class UnifiedRGBController:
    """Manages simultaneous control over SteelSeries and Razer RGB illumination."""

    def __init__(self):
        self.steelseries = SteelSeriesLEDController()
        self.razer = RazerChromaLEDController()

    def turn_off_devices(self):
        ss_ok = self.steelseries.setup()
        rz_ok = self.razer.setup()
        return {"steelseries": ss_ok, "razer": rz_ok}

    def restore_devices(self):
        self.razer.close()
        self.steelseries.restore()

    def run_daemon_loop(self):
        with open(LOCK_FILE, "w") as f:
            f.write(str(os.getpid()))

        with open(LOG_FILE, "a") as log:
            log.write(f"[{time.ctime()}] UnifiedRGBController daemon started (PID={os.getpid()})\n")

        status = self.turn_off_devices()
        with open(LOG_FILE, "a") as log:
            log.write(f"[{time.ctime()}] Initial setup: SteelSeries={status['steelseries']}, Razer={status['razer']}\n")

        try:
            while True:
                time.sleep(5)
                self.steelseries.heartbeat()
                self.razer.set_off()
        except Exception as e:
            with open(LOG_FILE, "a") as log:
                log.write(f"[{time.ctime()}] Daemon exception: {e}\n")
        finally:
            self.restore_devices()
            if os.path.exists(LOCK_FILE):
                try:
                    os.remove(LOCK_FILE)
                except Exception:
                    pass
            with open(LOG_FILE, "a") as log:
                log.write(f"[{time.ctime()}] Daemon stopped\n")

def stop_daemon():
    """Stop the running background daemon and restore default hardware lighting."""
    if os.path.exists(LOCK_FILE):
        try:
            with open(LOCK_FILE, "r") as f:
                pid = int(f.read().strip())
            subprocess.run(["taskkill", "/F", "/PID", str(pid)], capture_output=True)
            print(f"Stopped background daemon (PID {pid}).")
        except Exception as e:
            print("Error stopping daemon:", e)
        try:
            os.remove(LOCK_FILE)
        except Exception:
            pass

    controller = UnifiedRGBController()
    controller.restore_devices()
    print("Default device lighting restored.")

def start_daemon():
    """Start the background daemon process without a visible console window."""
    stop_daemon()
    pythonw = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
    if not os.path.exists(pythonw):
        pythonw = sys.executable

    main_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "main.py"))
    flags = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    proc = subprocess.Popen(
        [pythonw, main_script, "--daemon"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=flags
    )
    time.sleep(1)
    print(f"Started LED Off controller in background (PID {proc.pid}).")
    print("Keyboard and Mouse LEDs are now turned OFF.")

def get_status():
    """Check running status of daemon and hardware availability."""
    running = False
    pid = None
    if os.path.exists(LOCK_FILE):
        try:
            with open(LOCK_FILE, "r") as f:
                pid = int(f.read().strip())
            # Check if process exists
            check = subprocess.run(["tasklist", "/FI", f"PID eq {pid}"], capture_output=True, text=True)
            if str(pid) in check.stdout:
                running = True
        except Exception:
            running = False

    ctrl = UnifiedRGBController()
    ss_avail = ctrl.steelseries.is_available()
    rz_avail = ctrl.razer.is_available()

    print("RGB LED Controller Status:")
    print(f"  Daemon Running: {running} (PID: {pid if running else 'N/A'})")
    print(f"  SteelSeries Engine Detected: {ss_avail}")
    print(f"  Razer Chroma SDK Detected:   {rz_avail}")
