# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-15

### Added
- SteelSeries GameSense HTTP API integration to turn off mouse and keyboard LEDs.
- Automatic discovery of local SteelSeries GameSense ports via `coreProps.json`.
- Razer Chroma SDK C DLL integration (`RzChromaSDK64.dll`) to turn off keyboard LEDs using `CHROMA_NONE`.
- Unified controller (`src/controller.py`) coordinating both devices.
- Detached background daemon mode (`--off` / `--daemon`) running silently without console windows.
- Restoration routine (`--on` / `stop`) reverting devices to original SteelSeries and Synapse lighting.
- One-click Windows batch scripts (`scripts/turn_led_off.bat` and `scripts/turn_led_on.bat`).
- Unit test suite covering SteelSeries, Razer, and Unified controller functionality across separate test files.
- Master documentation in `README.md`.
