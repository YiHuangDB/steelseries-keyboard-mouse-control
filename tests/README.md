# Test Suite Documentation

Each test case is placed in a separate test file according to project development guidelines.

## Test Files

- [test_steelseries_url.py](test_steelseries_url.py): Verifies SteelSeries GameSense URL discovery.
- [test_steelseries_controller.py](test_steelseries_controller.py): Tests `SteelSeriesLEDController` initialization.
- [test_razer_availability.py](test_razer_availability.py): Checks Razer Chroma SDK DLL availability detection.
- [test_razer_controller.py](test_razer_controller.py): Tests `RazerChromaLEDController` initial state.
- [test_unified_controller.py](test_unified_controller.py): Verifies composition of both controllers in `UnifiedRGBController`.

## Running Tests

Run the test suite from the repository root:
```bash
python -m unittest discover -s tests
```

## Related Documentation

- Master documentation: [../README.md](../README.md)
- Changelog: [../CHANGELOG.md](../CHANGELOG.md)
