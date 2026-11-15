# Source Modules Documentation

This folder contains the core implementation for controlling SteelSeries and Razer RGB illumination.

## Modules

- [steelseries.py](steelseries.py): Communicates with SteelSeries GameSense HTTP server (supports dynamic port discovery via `coreProps.json`) to control mouse and keyboard zones.
- [razer.py](razer.py): Interfaces with Razer Chroma SDK via `RzChromaSDK64.dll` to set keyboard and mouse effects to `CHROMA_NONE`.
- [controller.py](controller.py): Unified orchestration daemon and CLI functions (`start_daemon`, `stop_daemon`, `get_status`).

## Related Documentation

- Master documentation: [../README.md](../README.md)
- Changelog: [../CHANGELOG.md](../CHANGELOG.md)
