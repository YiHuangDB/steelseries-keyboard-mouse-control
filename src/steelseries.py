import os
import json
import requests

def get_steelseries_url():
    """Discover the local SteelSeries GameSense HTTP server address from coreProps.json."""
    paths = [
        os.path.expandvars(r"%PROGRAMDATA%\SteelSeries\GG\coreProps.json"),
        os.path.expandvars(r"%PROGRAMDATA%\SteelSeries\SteelSeries Engine 3\coreProps.json"),
        r"C:\ProgramData\SteelSeries\GG\coreProps.json",
        r"C:\ProgramData\SteelSeries\SteelSeries Engine 3\coreProps.json"
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "address" in data:
                        return f"http://{data['address']}"
            except Exception:
                pass
    return "http://127.0.0.1:52729"

class SteelSeriesLEDController:
    """Controls SteelSeries RGB LED devices using the GameSense HTTP API."""

    def __init__(self, game_name="ANTIGRAVITY_RGB"):
        self.game = game_name
        self.base_url = get_steelseries_url()
        self.is_active = False

    def is_available(self):
        try:
            r = requests.get(f"{self.base_url}/ping", timeout=2)
            return r.status_code == 200
        except Exception:
            return False

    def setup(self):
        """Register game metadata and bind event to turn off all RGB zones."""
        self.base_url = get_steelseries_url()
        try:
            meta = {
                "game": self.game,
                "game_display_name": "RGB LED Controller",
                "icon_color_id": 0,
                "deinitialize_timer_length_ms": 30000
            }
            requests.post(f"{self.base_url}/game_metadata", json=meta, timeout=3)

            bind_all = {
                "game": self.game,
                "event": "ALL_OFF",
                "handlers": [
                    {
                        "device-type": "mouse",
                        "zone": "all",
                        "color": {"red": 0, "green": 0, "blue": 0},
                        "mode": "color"
                    },
                    {
                        "device-type": "keyboard",
                        "zone": "all",
                        "color": {"red": 0, "green": 0, "blue": 0},
                        "mode": "color"
                    },
                    {
                        "device-type": "rgb-per-key-zones",
                        "zone": "all",
                        "color": {"red": 0, "green": 0, "blue": 0},
                        "mode": "color"
                    },
                    {
                        "device-type": "rgb-zoned-device",
                        "zone": "all",
                        "color": {"red": 0, "green": 0, "blue": 0},
                        "mode": "color"
                    }
                ]
            }
            requests.post(f"{self.base_url}/bind_game_event", json=bind_all, timeout=3)

            ev = {
                "game": self.game,
                "event": "ALL_OFF",
                "data": {"value": 1}
            }
            requests.post(f"{self.base_url}/game_event", json=ev, timeout=3)
            self.is_active = True
            return True
        except Exception:
            self.is_active = False
            return False

    def heartbeat(self):
        """Send heartbeat to keep the LED off event active."""
        try:
            r = requests.post(f"{self.base_url}/game_heartbeat", json={"game": self.game}, timeout=3)
            if r.status_code != 200:
                self.setup()
        except Exception:
            self.setup()

    def restore(self):
        """Remove the game from GameSense to restore default SteelSeries Engine/Prism lighting."""
        try:
            requests.post(f"{self.base_url}/remove_game", json={"game": self.game}, timeout=3)
            self.is_active = False
            return True
        except Exception:
            return False
