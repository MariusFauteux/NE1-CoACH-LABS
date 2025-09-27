# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is the **CoACH-labs** repository for Neuromorphic Engineering I (NE1) coursework. It contains Python-based laboratory exercises that interface with the CoACH neuromorphic chip via the Teensy microcontroller. The labs are implemented as Jupyter notebooks that guide students through characterizing various circuits on the CoACH chip including FETs, transconductance amplifiers, DVS pixels, and neural circuits.

## Core Architecture

### Hardware Interface Stack
- **CoACH chip**: Custom neuromorphic ASIC containing various analog circuits
- **Plane PCB**: Interface board with DACs, ADCs, current sensing, and USB communication
- **Teensy microcontroller**: Handles USB-to-serial communication and real-time control
- **pyplane library**: Low-level Python extension (C++) for hardware communication
- **Coach() class**: High-level Python wrapper (singleton) that simplifies lab experiments

### Key Components
- `ne1.py`: Main library containing the Coach() class and utilities
- `requirements.txt`: All Python dependencies including pyplane, numpy, matplotlib, scipy
- Lab notebooks: `Lab0X_*.ipynb` files containing exercises for each week
- `test/`: Unit tests for the hardware interface and Coach class functionality
- `figs/`: Circuit diagrams and hardware photos for documentation

## Development Commands

### Environment Setup
```bash
# Create conda environment (recommended)
conda create -n ne1 python=3.9 --yes
conda activate ne1

# Install dependencies
pip install -r requirements.txt

# For Apple Silicon or newer Python versions, build pyplane from source:
git clone https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface
cd CoACH_Teensy_interface
pip install pybind11[global]
mkdir build && cd build
cmake ../src
make -j
# Copy the resulting .so file to your CoACH-labs directory
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test categories
pytest -m "not slow"  # Skip slow tests
pytest -k test_nfet   # Run NFET-related tests only
pytest -s            # Show print output during tests

# Run single test
pytest test/test_ne1.py::test_coach_singleton
```

### Working with Notebooks
```bash
# Start Jupyter notebook
jupyter notebook Lab01_Setup_GroupNumber_FirstName_LastName.ipynb

# Install packages from within notebook
!{sys.executable} -m pip install -r requirements.txt
```

### Documentation Generation
```bash
# Generate API documentation for ne1.py
pip install pydoc-markdown
pydoc-markdown -p ne1 --render-toc >ne1.md
```

## Code Architecture Details

### Coach Class (Singleton Pattern)
The `Coach()` class in `ne1.py` is implemented as a singleton using `@lru_cache(maxsize=None)`. Key architectural features:

- **Hardware abstraction**: Wraps pyplane's low-level interface with high-level methods
- **Experiment setup**: `setup_nfet()`, `setup_dvs()`, `setup_nta()` methods configure chip circuits
- **Measurement methods**: `measure_nfet_id()`, `measure_c2f_freqs()` handle data acquisition
- **USB device management**: Automatic device discovery and firmware version checking
- **Logging integration**: Comprehensive logging with color formatting for debugging

### Current Measurement Architecture
The hardware uses two different measurement approaches:
- **FET currents**: Measured via INA2331 instrumentation amplifiers with switchable gain (1μA/100μA ranges)
- **Small currents**: Measured via Current-to-Frequency (C2F) converters for pA-nA range currents

### Bias Generation System
- **Four DAC53608 10-bit DACs**: Provide reference voltages with 1.76mV resolution
- **Bias addressing system**: Hierarchical addressing for different bias types (N/P) and current ranges
- **Master current sources**: Multiple current ranges from 60pA to 30μA

## Important Development Notes

### Hardware Dependencies
- **Linux/Ubuntu required**: pyplane library requires Linux for USB device access
- **USB permissions**: May need root access or proper udev rules for device access
- **WSL2 support**: Windows users can use WSL2 with usbipd-win for USB passthrough
- **Mac limitations**: ARM Macs require building pyplane from source

### Testing Considerations
- Tests marked `@pytest.mark.serial` must run sequentially (hardware access)
- Coach singleton means tests share state - proper setup/teardown critical
- Hardware timeouts common if firmware versions mismatch
- Physical chip required for most tests - mock testing limited

### Common Development Patterns
```python
# Standard lab setup pattern
from ne1 import Coach
c = Coach()
c.open()
c.setup_nfet()  # Configure for specific experiment
# ... perform measurements ...
c.close()

# Error handling pattern
try:
    c.open()
    # ... experiment code ...
except RuntimeError as e:
    log.error(f"Hardware error: {e}")
finally:
    c.close()
```

### Data Management
- Use `jupyter-save-load-vars` for persistent data storage
- Create `data/labX` directories for organized data storage
- Export notebooks as HTML/PDF for submission (never .ipynb files)

## Debugging and Troubleshooting

### Common Issues
- **USB device not found**: Check `lsusb` for Teensyduino device, verify USB cable
- **Firmware mismatch**: Update Teensy firmware using Teensy Loader application
- **Permission errors**: Run as root or configure USB device permissions
- **Timeout errors**: Usually indicate firmware version mismatch or bad USB connection

### Debug Tools
```python
# Enable detailed pyplane debugging
c.set_debug(True)

# Change logging levels
c = Coach(logging_level=logging.DEBUG)

# Check device status
c.get_firmware_version()
c.find_coach()
```

This repository represents a complete embedded systems interface for neuromorphic engineering education, requiring both hardware and software expertise for effective development and debugging.