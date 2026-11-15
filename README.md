# SteelSeries & Razer Keyboard & Mouse RGB LED Control

A unified, lightweight controller for controlling RGB LED illumination on connected keyboards and mice (specifically SteelSeries mice like the Aerox 5, and Razer keyboards like the BlackWidow Chroma, as well as generic SteelSeries and Razer RGB peripherals).

Allows quickly turning off device LEDs without having to configure complex manual color profiles, with an instant restore feature to return back to default illumination.

---

## Documentation Index

This master document tracks and references all project documentation across this repository:

- [CHANGELOG.md](CHANGELOG.md): Complete history of releases, changes, and additions.
- [LICENSE](LICENSE): Project license.
- [src/README.md](src/README.md): Architecture and documentation of the core Python controllers (`steelseries.py`, `razer.py`, `controller.py`).
- [scripts/README.md](scripts/README.md): Documentation of one-click Windows batch scripts.
- [tests/README.md](tests/README.md): Test suite structure, test files, and test execution details.

---

## Features

- **SteelSeries GameSense Integration**: Binds illumination events across all mouse and keyboard zones directly through the local SteelSeries Engine / GG GameSense HTTP API with automatic port discovery from `coreProps.json`.
- **Razer Chroma SDK Integration**: Directly talks to the 64-bit Razer Chroma SDK (`RzChromaSDK64.dll`) to apply `CHROMA_NONE` effects across keyboards, keypads, mice, and ChromaLink devices.
- **Silent Background Daemon**: Can run detached via `pythonw.exe` without popping up terminal or console windows.
- **One-Click Batch Scripts**: Includes Windows desktop batch scripts for instant toggling (`turn_led_off.bat` and `turn_led_on.bat`).
- **Instant Restore**: Restoring lighting immediately releases Chroma SDK and cleans up GameSense events, returning hardware to normal profile lighting.

---

## Requirements

- Windows 10/11
- Python 3.8+
- [SteelSeries GG / Engine 3](https://steelseries.com/gg) (for SteelSeries devices)
- [Razer Synapse 3 / Chroma SDK](https://www.razer.com/synapse-3) (for Razer devices)
- Python packages:
  ```bash
  pip install -r requirements.txt
  ```

---

## Usage

### 1. Command Line Interface

```bash
# Turn off keyboard & mouse LEDs (starts background daemon)
python main.py --off

# Turn LEDs back on (restores default lighting profiles)
python main.py --on

# Check controller status and hardware detection
python main.py --status

# Run the daemon directly in current terminal session
python main.py --daemon
```

### 2. Windows Batch Scripts

Located in the [`scripts/`](scripts/) folder:
- **`scripts/turn_led_off.bat`**: Double-click to turn off keyboard and mouse LEDs.
- **`scripts/turn_led_on.bat`**: Double-click to restore normal RGB lighting.

### 3. Automatic Startup on Windows Login

To automatically keep LEDs off when logging into Windows, place a shortcut or batch script in your Startup folder:
```text
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
```

---

## Testing

Each test case is organized into a dedicated test file in [`tests/`](tests/):

```bash
python -m unittest discover -s tests
```
