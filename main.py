import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.controller import start_daemon, stop_daemon, get_status, UnifiedRGBController

def main():
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else "--off"

    if arg in ["--off", "off", "start"]:
        start_daemon()
    elif arg in ["--on", "on", "stop"]:
        stop_daemon()
    elif arg in ["--daemon"]:
        controller = UnifiedRGBController()
        controller.run_daemon_loop()
    elif arg in ["--status", "status"]:
        get_status()
    else:
        print("SteelSeries & Razer RGB LED Controller")
        print("Usage:")
        print("  python main.py --off     # Turn off keyboard & mouse LEDs (runs background daemon)")
        print("  python main.py --on      # Restore original lighting (stops daemon)")
        print("  python main.py --status  # Check daemon status and hardware detection")
        print("  python main.py --daemon  # Run daemon loop directly in current console")

if __name__ == "__main__":
    main()
