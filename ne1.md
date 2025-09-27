# Table of Contents

* [ne1](#ne1)
  * [CustomFormatter](#ne1.CustomFormatter)
    * [grey](#ne1.CustomFormatter.grey)
    * [cyan](#ne1.CustomFormatter.cyan)
    * [green](#ne1.CustomFormatter.green)
    * [red](#ne1.CustomFormatter.red)
  * [get\_logger](#ne1.get_logger)
  * [Coach](#ne1.Coach)
    * [DEFAULT\_USB\_PORT](#ne1.Coach.DEFAULT_USB_PORT)
    * [\_\_init\_\_](#ne1.Coach.__init__)
    * [\_\_del\_\_](#ne1.Coach.__del__)
    * [open](#ne1.Coach.open)
    * [find\_coach](#ne1.Coach.find_coach)
    * [is\_open](#ne1.Coach.is_open)
    * [close](#ne1.Coach.close)
    * [check\_open](#ne1.Coach.check_open)
    * [get\_firmware\_version](#ne1.Coach.get_firmware_version)
    * [get\_pyplane](#ne1.Coach.get_pyplane)
    * [reset\_soft](#ne1.Coach.reset_soft)
    * [reset\_hard](#ne1.Coach.reset_hard)
    * [set\_debug](#ne1.Coach.set_debug)
    * [setup\_nfet](#ne1.Coach.setup_nfet)
    * [set\_nfet\_vg](#ne1.Coach.set_nfet_vg)
    * [set\_nfet\_vb](#ne1.Coach.set_nfet_vb)
    * [set\_nfet\_vs](#ne1.Coach.set_nfet_vs)
    * [set\_nfet\_vd](#ne1.Coach.set_nfet_vd)
    * [measure\_nfet\_id](#ne1.Coach.measure_nfet_id)
    * [measure\_nfet\_is](#ne1.Coach.measure_nfet_is)
    * [setup\_nfa](#ne1.Coach.setup_nfa)
    * [set\_nfa\_vg](#ne1.Coach.set_nfa_vg)
    * [setup\_pfa](#ne1.Coach.setup_pfa)
    * [set\_pfa\_vg](#ne1.Coach.set_pfa_vg)
    * [setup\_pfet](#ne1.Coach.setup_pfet)
    * [set\_pfet\_vg](#ne1.Coach.set_pfet_vg)
    * [set\_pfet\_vb](#ne1.Coach.set_pfet_vb)
    * [set\_pfet\_vs](#ne1.Coach.set_pfet_vs)
    * [set\_pfet\_vd](#ne1.Coach.set_pfet_vd)
    * [measure\_pfet\_id](#ne1.Coach.measure_pfet_id)
    * [measure\_pfet\_is](#ne1.Coach.measure_pfet_is)
    * [setup\_diffpair\_n](#ne1.Coach.setup_diffpair_n)
    * [set\_diffpair\_n\_v1](#ne1.Coach.set_diffpair_n_v1)
    * [set\_diffpair\_n\_v2](#ne1.Coach.set_diffpair_n_v2)
    * [set\_diffpair\_n\_ib](#ne1.Coach.set_diffpair_n_ib)
    * [setup\_ndp](#ne1.Coach.setup_ndp)
    * [set\_ndp\_v1](#ne1.Coach.set_ndp_v1)
    * [set\_ndp\_v2](#ne1.Coach.set_ndp_v2)
    * [set\_ndp\_ib](#ne1.Coach.set_ndp_ib)
    * [setup\_bab](#ne1.Coach.setup_bab)
    * [set\_bab\_v1](#ne1.Coach.set_bab_v1)
    * [set\_bab\_v2](#ne1.Coach.set_bab_v2)
    * [set\_bab\_ib](#ne1.Coach.set_bab_ib)
    * [NTA\_I1\_C2F\_CHANNEL](#ne1.Coach.NTA_I1_C2F_CHANNEL)
    * [NTA\_I2\_C2F\_CHANNEL](#ne1.Coach.NTA_I2_C2F_CHANNEL)
    * [setup\_nta](#ne1.Coach.setup_nta)
    * [set\_nta\_ib](#ne1.Coach.set_nta_ib)
    * [set\_nta\_v1](#ne1.Coach.set_nta_v1)
    * [set\_nta\_v2](#ne1.Coach.set_nta_v2)
    * [PTA\_I1\_C2F\_CHANNEL](#ne1.Coach.PTA_I1_C2F_CHANNEL)
    * [PTA\_I2\_C2F\_CHANNEL](#ne1.Coach.PTA_I2_C2F_CHANNEL)
    * [setup\_pta](#ne1.Coach.setup_pta)
    * [set\_pta\_ib](#ne1.Coach.set_pta_ib)
    * [set\_pta\_v1](#ne1.Coach.set_pta_v1)
    * [set\_pta\_v2](#ne1.Coach.set_pta_v2)
    * [setup\_wrt](#ne1.Coach.setup_wrt)
    * [set\_wrt\_ib](#ne1.Coach.set_wrt_ib)
    * [set\_wrt\_v1](#ne1.Coach.set_wrt_v1)
    * [set\_wrt\_v2](#ne1.Coach.set_wrt_v2)
    * [measure\_wrt\_vout](#ne1.Coach.measure_wrt_vout)
    * [setup\_dvs](#ne1.Coach.setup_dvs)
    * [DVS\_DIFF\_FINE\_VAL](#ne1.Coach.DVS_DIFF_FINE_VAL)
    * [DVS\_DIFF\_CB](#ne1.Coach.DVS_DIFF_CB)
    * [DVS\_DIFF\_ON\_OFF\_RATIO](#ne1.Coach.DVS_DIFF_ON_OFF_RATIO)
    * [DVS\_DEFAULT\_BIASES](#ne1.Coach.DVS_DEFAULT_BIASES)
    * [setup\_dvs\_biases](#ne1.Coach.setup_dvs_biases)
    * [set\_dvs\_threshold\_biases](#ne1.Coach.set_dvs_threshold_biases)
    * [filter\_dvs\_events](#ne1.Coach.filter_dvs_events)
    * [set\_led\_intensity](#ne1.Coach.set_led_intensity)
    * [setup\_ahn](#ne1.Coach.setup_ahn)
    * [set\_ahn\_vpw\_ib](#ne1.Coach.set_ahn_vpw_ib)
    * [read\_ahn\_vout](#ne1.Coach.read_ahn_vout)
    * [request\_coach\_output\_events](#ne1.Coach.request_coach_output_events)
    * [read\_coach\_output\_events](#ne1.Coach.read_coach_output_events)
    * [capture\_coach\_output\_events](#ne1.Coach.capture_coach_output_events)
    * [coach\_events\_to\_timestamps\_addresses](#ne1.Coach.coach_events_to_timestamps_addresses)
    * [setup\_foi](#ne1.Coach.setup_foi)
    * [set\_foi\_vin](#ne1.Coach.set_foi_vin)
    * [foi\_compensate\_vin](#ne1.Coach.foi_compensate_vin)
    * [set\_foi\_ib](#ne1.Coach.set_foi_ib)
    * [measure\_foi\_waveform](#ne1.Coach.measure_foi_waveform)
    * [setup\_c2f](#ne1.Coach.setup_c2f)
    * [measure\_c2f\_freqs](#ne1.Coach.measure_c2f_freqs)
    * [set\_bias\_from\_tuple](#ne1.Coach.set_bias_from_tuple)
    * [set\_bias](#ne1.Coach.set_bias)
    * [transient\_response](#ne1.Coach.transient_response)
  * [input\_with\_timeout](#ne1.input_with_timeout)
  * [yes\_or\_no\_or\_always](#ne1.yes_or_no_or_always)
  * [Timer](#ne1.Timer)
    * [\_\_init\_\_](#ne1.Timer.__init__)
    * [print\_timing\_info](#ne1.Timer.print_timing_info)

<a id="ne1"></a>

# ne1

<a id="ne1.CustomFormatter"></a>

## CustomFormatter Objects

```python
class CustomFormatter(logging.Formatter)
```

Logging Formatter to add colors and count warning / errors

<a id="ne1.CustomFormatter.grey"></a>

#### grey

2 faint, 37 gray

<a id="ne1.CustomFormatter.cyan"></a>

#### cyan

0 normal 36 cyan

<a id="ne1.CustomFormatter.green"></a>

#### green

dark green

<a id="ne1.CustomFormatter.red"></a>

#### red

bold red

<a id="ne1.get_logger"></a>

#### get\_logger

```python
def get_logger()
```

Use get_logger to define a logger with useful color output and info and warning turned on according to the global LOGGING_LEVEL.

**Returns**:

the logger.

<a id="ne1.Coach"></a>

## Coach Objects

```python
@lru_cache(maxsize=None)
class Coach()
```

A wrapper for pyplane to make it easier to use in Python notebooks. 
NOTE Coach() is a singleton - you can only create one instance of it in a Python run.

The main methods are open(), close(), and setup_XXX() methods. These setup experiments and simplify the measurements.

There are also methods for setting up measuring the C2F output frequencies and for setting biases.

<a id="ne1.Coach.DEFAULT_USB_PORT"></a>

#### DEFAULT\_USB\_PORT

The default USB port that Plane PCB appears on, usually.

<a id="ne1.Coach.__init__"></a>

#### \_\_init\_\_

```python
def __init__(logging_level=_LOGGING_LEVEL)
```

Make or return existing CoACH device. Coach() is a wrapper for pyplane to make it easier to use in Python notebooks.

The main methods are open(), close(), and setup_XXX() methods. These setup experiments and simplify the measurements.

    There are also methods for setting up measuring the C2F output frequencies and for setting biases.

**Arguments**:

- `logging_level`: set the logging level, e.g. logging.DEBUG. Default is logging.INFO

<a id="ne1.Coach.__del__"></a>

#### \_\_del\_\_

```python
def __del__()
```

We override the default destructor to make sure the Pyplane object is deleted

<a id="ne1.Coach.open"></a>

#### open

```python
def open(usbport: str = None) -> None
```

Opens the CoACH Plane PCB

**Arguments**:

- `usbport`: the name of the Teensy USB port, if None, then try to scan for Teensyduino

**Raises**:

- `None`: RunTimeError if board cannot be opened or there is a timeout or there is a firmware mismatch

<a id="ne1.Coach.find_coach"></a>

#### find\_coach

```python
def find_coach() -> str
```

Finds the CoACH board USB device if it is there.

**Returns**:

the device name, e.g. /dev/ttyACM0, or None if it is not found

<a id="ne1.Coach.is_open"></a>

#### is\_open

```python
def is_open() -> bool
```

check if board is open

**Returns**:

True if open and firmware version is not error timeout value

<a id="ne1.Coach.close"></a>

#### close

```python
def close() -> None
```

Closes the board. Deletes the pyplane.Plane() object.

<a id="ne1.Coach.check_open"></a>

#### check\_open

```python
def check_open() -> None
```

Checks if open and opens if not.

<a id="ne1.Coach.get_firmware_version"></a>

#### get\_firmware\_version

```python
def get_firmware_version() -> tuple
```

returns the firmware version

**Returns**:

a 3-tuple, e.g. (1,24,12)

<a id="ne1.Coach.get_pyplane"></a>

#### get\_pyplane

```python
def get_pyplane() -> pyplane.Plane
```

Returns the low level pyplane object

<a id="ne1.Coach.reset_soft"></a>

#### reset\_soft

```python
def reset_soft() -> None
```

Do a soft reset. This
1. turns off AER output, LEDs, DAC outputs
2. sets analog read resolution to 12 bits 
3. Sets read averaging to 4

<a id="ne1.Coach.reset_hard"></a>

#### reset\_hard

```python
def reset_hard() -> None
```

Do a hard reset. This operation requires several seconds. It

    1. Asks the Teensy to initiate a full reset of the Teensy and everything resettable on the board.
    2. Waits for the Teensy to say that it can do a hard reset (boards <v0.4 cannot). (The Teensy then waits to give us a chance to close the USB connection before it actually performs the reset).
    3. Closes the USB connection.
    4. Waits for what we hope will be long enough for the Teensy to reset (this is of course racy)
    5. Tries to reconnect to the Teensy using the same device name with which it was opened.
    6. Checks that the board that it has now connected to has the same serial number as the board that it was connected to before the reset.

NOTE: This call will block the Coach board from being accessed for at least 5 seconds

<a id="ne1.Coach.set_debug"></a>

#### set\_debug

```python
def set_debug(yes: bool) -> None
```

Enables or disables debug mode for pyplane.

This option prints out the serial communication packets. 
Each starts with a packet type, followed by a number of bytes expected in the packet.
An example follows:
``` 
        Tx 08 00
        Rx90 08 03 01 0c 05
        Tx 08 00
        Rx90 08 03 01 0c 05
        Tx 38 04 00 00 b0 01
        Rx90 04 01 00
        Tx 08 00
    ```

**Arguments**:

- `yes`: set True to turn on debugging.

<a id="ne1.Coach.setup_nfet"></a>

#### setup\_nfet

```python
def setup_nfet() -> None
```

Setup the nfet for measurement

<a id="ne1.Coach.set_nfet_vg"></a>

#### set\_nfet\_vg

```python
def set_nfet_vg(v) -> float
```

set the nfet gate voltage

**Returns**:

the actual voltage set after DAC quantization

<a id="ne1.Coach.set_nfet_vb"></a>

#### set\_nfet\_vb

```python
def set_nfet_vb(v) -> int
```

does nothing, since nfet bulk is always zero

<a id="ne1.Coach.set_nfet_vs"></a>

#### set\_nfet\_vs

```python
def set_nfet_vs(v) -> float
```

set the nfet source voltage

<a id="ne1.Coach.set_nfet_vd"></a>

#### set\_nfet\_vd

```python
def set_nfet_vd(v) -> float
```

set the nfet drain voltage

<a id="ne1.Coach.measure_nfet_id"></a>

#### measure\_nfet\_id

```python
def measure_nfet_id() -> float
```

measure the nfet drain current and return it

**Returns**:

the current in amps

<a id="ne1.Coach.measure_nfet_is"></a>

#### measure\_nfet\_is

```python
def measure_nfet_is() -> float
```

measure the nfet source current and return it

**Returns**:

the current in amps

<a id="ne1.Coach.setup_nfa"></a>

#### setup\_nfa

```python
def setup_nfa() -> None
```

Sets up the NFET array.

Set the common gate voltages with `set_nfa_vg()` and read
the drain currents with `measure_c2f_freqs()`. 

The 16 C2F channels are the 16 FETs.

The FET lengths are  in `(N+1)*NFA_LENGTHS_UNIT_UM` where `N` is the C2F channel number.

<a id="ne1.Coach.set_nfa_vg"></a>

#### set\_nfa\_vg

```python
def set_nfa_vg(vgn) -> float
```

Sets the NFET array gate voltage

**Arguments**:

- `vgn`: the gate voltage

**Returns**:

the quantized voltage

<a id="ne1.Coach.setup_pfa"></a>

#### setup\_pfa

```python
def setup_pfa() -> None
```

Sets up the PFET array.

Set the common gate voltages with `set_nfa_vg()` and read
the drain currents with `measure_c2f_freqs()`. 

The 16 C2F channels are the 16 FETs.

The FET lengths are  in `(N+1)*NFA_LENGTHS_UNIT_UM` where `N` is the C2F channel number.

<a id="ne1.Coach.set_pfa_vg"></a>

#### set\_pfa\_vg

```python
def set_pfa_vg(vgp) -> float
```

Sets the PFET array gate voltage

**Arguments**:

- `vgp`: the gate voltage

**Returns**:

the quantized voltage

<a id="ne1.Coach.setup_pfet"></a>

#### setup\_pfet

```python
def setup_pfet() -> None
```

setup the PFET for measurement

<a id="ne1.Coach.set_pfet_vg"></a>

#### set\_pfet\_vg

```python
def set_pfet_vg(v) -> float
```

set the pfet gate voltage

**Returns**:

the actual voltage set after DAC quantization

<a id="ne1.Coach.set_pfet_vb"></a>

#### set\_pfet\_vb

```python
def set_pfet_vb(v) -> float
```

set the pfet bulk voltage

<a id="ne1.Coach.set_pfet_vs"></a>

#### set\_pfet\_vs

```python
def set_pfet_vs(v) -> float
```

set the pfet source voltage

<a id="ne1.Coach.set_pfet_vd"></a>

#### set\_pfet\_vd

```python
def set_pfet_vd(v) -> float
```

set the pfet drain voltage

<a id="ne1.Coach.measure_pfet_id"></a>

#### measure\_pfet\_id

```python
def measure_pfet_id() -> float
```

measure the pfet source current and return it

**Returns**:

the current in amps

<a id="ne1.Coach.measure_pfet_is"></a>

#### measure\_pfet\_is

```python
def measure_pfet_is() -> float
```

measure the pfet source current and return it

**Returns**:

the current in amps

<a id="ne1.Coach.setup_diffpair_n"></a>

#### setup\_diffpair\_n

```python
@deprecated('Use setup_ndp() instead')
def setup_diffpair_n()
```

Sets up n-type diff pair

<a id="ne1.Coach.set_diffpair_n_v1"></a>

#### set\_diffpair\_n\_v1

```python
@deprecated('Use set_ndp_v1() instead')
def set_diffpair_n_v1(v1)
```

Sets NDP V1

**Arguments**:

- `v1`: the voltage

**Returns**:

its quantized value

<a id="ne1.Coach.set_diffpair_n_v2"></a>

#### set\_diffpair\_n\_v2

```python
@deprecated('Use set_ndp_v2() instead')
def set_diffpair_n_v2(v2: float)
```

Sets NDP V2

**Arguments**:

- `v2`: the voltage

**Returns**:

its quantized value

<a id="ne1.Coach.set_diffpair_n_ib"></a>

#### set\_diffpair\_n\_ib

```python
@deprecated('Use set_ndp_ib() instead')
def set_diffpair_n_ib(bias_coarse: pyplane.Coach.BiasGenMasterCurrent,
                      fine_value)
```

Sets the bias current of the NDP (n type diff pair).

<a id="ne1.Coach.setup_ndp"></a>

#### setup\_ndp

```python
def setup_ndp() -> None
```

Sets up n-type diff pair.

<a id="ne1.Coach.set_ndp_v1"></a>

#### set\_ndp\_v1

```python
def set_ndp_v1(v1) -> float
```

Sets NDP V1

**Arguments**:

- `v1`: the voltage

**Returns**:

its quantized value

<a id="ne1.Coach.set_ndp_v2"></a>

#### set\_ndp\_v2

```python
def set_ndp_v2(v2) -> float
```

Sets NDP V2

**Arguments**:

- `v2`: the voltage

**Returns**:

its quantized value

<a id="ne1.Coach.set_ndp_ib"></a>

#### set\_ndp\_ib

```python
def set_ndp_ib(bias_coarse: pyplane.Coach.BiasGenMasterCurrent,
               fine_value) -> float
```

Sets the bias current of the NDP (n type diff pair).

**Arguments**:

- `bias_coarse`: A coarse value of current.
allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
- `fine_value`: 0-255 int fine value. 
0 should not really be used since the current is badly defined.

<a id="ne1.Coach.setup_bab"></a>

#### setup\_bab

```python
def setup_bab() -> None
```

Setup the Bump Anti Bump (BAB) circuit.

<a id="ne1.Coach.set_bab_v1"></a>

#### set\_bab\_v1

```python
def set_bab_v1(v1) -> float
```

Sets the V1 input of the BAB

**Arguments**:

- `v1`: the voltage

**Returns**:

the actual quantized voltage

<a id="ne1.Coach.set_bab_v2"></a>

#### set\_bab\_v2

```python
def set_bab_v2(v2) -> float
```

Sets the V2 input of the BAB

**Arguments**:

- `v2`: the voltage

**Returns**:

the actual quantized voltage

<a id="ne1.Coach.set_bab_ib"></a>

#### set\_bab\_ib

```python
def set_bab_ib(coarse_current_bab: pyplane.Coach.BiasGenMasterCurrent,
               fine_current_bab) -> float
```

Sets the bias current of the BAB bump-antibump circuit.

**Arguments**:

- `bias_coarse`: A coarse value of current.
allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
- `fine_value`: 0-255 int fine value. 
0 should not really be used since the current is badly defined.

**Returns**:

the bias current.
This function accounts for the W/L ratio of BAB bias FET.

<a id="ne1.Coach.NTA_I1_C2F_CHANNEL"></a>

#### NTA\_I1\_C2F\_CHANNEL

Iplus channel for NTA with output clamped to 1V

<a id="ne1.Coach.NTA_I2_C2F_CHANNEL"></a>

#### NTA\_I2\_C2F\_CHANNEL

Iminus channel for NTA with output clamped to 1V

<a id="ne1.Coach.setup_nta"></a>

#### setup\_nta

```python
def setup_nta() -> None
```

Sets up the NTA (n-type 5-T transamp).

<a id="ne1.Coach.set_nta_ib"></a>

#### set\_nta\_ib

```python
def set_nta_ib(bias_coarse: pyplane.Coach.BiasGenMasterCurrent,
               fine_value: int) -> float
```

Sets the bias current of the NTA.

**Arguments**:

- `bias_coarse`: A coarse value of current.
allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
- `fine_value`: 0-255 int fine value. 
0 should not really be used since the current is badly defined.

**Returns**:

the bias current.

<a id="ne1.Coach.set_nta_v1"></a>

#### set\_nta\_v1

```python
def set_nta_v1(v1) -> float
```

Sets NTA V1 input

**Arguments**:

- `v1`: volts

<a id="ne1.Coach.set_nta_v2"></a>

#### set\_nta\_v2

```python
def set_nta_v2(v2) -> float
```

Sets NTA V2 input

**Arguments**:

- `v2`: volts

<a id="ne1.Coach.PTA_I1_C2F_CHANNEL"></a>

#### PTA\_I1\_C2F\_CHANNEL

Iplus channel for PTA with output clamped to 1V

<a id="ne1.Coach.PTA_I2_C2F_CHANNEL"></a>

#### PTA\_I2\_C2F\_CHANNEL

Iminus channel for PTA with output clamped to 1V

<a id="ne1.Coach.setup_pta"></a>

#### setup\_pta

```python
def setup_pta() -> None
```

Sets up the PTA (p-type 5-T transamp).

<a id="ne1.Coach.set_pta_ib"></a>

#### set\_pta\_ib

```python
def set_pta_ib(bias_coarse: pyplane.Coach.BiasGenMasterCurrent,
               fine_value) -> float
```

Sets the bias current of the PTA.

**Arguments**:

- `bias_coarse`: A coarse value of current.
allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
- `fine_value`: 0-255 int fine value. 
0 should not really be used since the current is badly defined.

**Returns**:

the bias current.

<a id="ne1.Coach.set_pta_v1"></a>

#### set\_pta\_v1

```python
def set_pta_v1(v1) -> float
```

Sets PTA V1 input

**Arguments**:

- `v1`: volts

<a id="ne1.Coach.set_pta_v2"></a>

#### set\_pta\_v2

```python
def set_pta_v2(v2) -> float
```

Sets PTA V2 input

**Arguments**:

- `v2`: volts

<a id="ne1.Coach.setup_wrt"></a>

#### setup\_wrt

```python
def setup_wrt() -> None
```

Sets up the WRT (wide output range transamp). Note only the Vout node can be measured in open loop.

<a id="ne1.Coach.set_wrt_ib"></a>

#### set\_wrt\_ib

```python
def set_wrt_ib(bias_coarse: pyplane.Coach.BiasGenMasterCurrent, fine_value)
```

Sets the bias current of the WRT.

**Arguments**:

- `bias_coarse`: A coarse value of current.
allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
- `fine_value`: 0-255 int fine value. 
0 should not really be used since the current is badly defined.

<a id="ne1.Coach.set_wrt_v1"></a>

#### set\_wrt\_v1

```python
def set_wrt_v1(v1)
```

Sets PTA V1 input

**Arguments**:

- `v1`: volts

<a id="ne1.Coach.set_wrt_v2"></a>

#### set\_wrt\_v2

```python
def set_wrt_v2(v2)
```

Sets PTA V2 input

**Arguments**:

- `v2`: volts

<a id="ne1.Coach.measure_wrt_vout"></a>

#### measure\_wrt\_vout

```python
def measure_wrt_vout()
```

Returns the WRT output voltage.

<a id="ne1.Coach.setup_dvs"></a>

#### setup\_dvs

```python
def setup_dvs(on_off_ratio=2) -> None
```

Sets up the DVS pixel.

**Arguments**:

- `on_off_ratio`: the desired ratio of Ion/Id and Id/Ioff
See [Coach chip report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=share_link), Table 15, page 28 for event addresses.

**Returns**:

ipr,isf,icas,idiff,ion,ioff,irefr
The actual programmed bias currents in Amps

<a id="ne1.Coach.DVS_DIFF_FINE_VAL"></a>

#### DVS\_DIFF\_FINE\_VAL

Coarse bias of DVS pixel change detector

<a id="ne1.Coach.DVS_DIFF_CB"></a>

#### DVS\_DIFF\_CB

Nominal fine value of DVS change detector

<a id="ne1.Coach.DVS_DIFF_ON_OFF_RATIO"></a>

#### DVS\_DIFF\_ON\_OFF\_RATIO

Nominal value of DVS change detector current ratios

<a id="ne1.Coach.DVS_DEFAULT_BIASES"></a>

#### DVS\_DEFAULT\_BIASES

Default values of DVS pixel biases, each one is a tuple of (address, type, coarse, fine). You can find out a default value with  from `DVS_DEFAULT_BIASES['sf']`, for example.

<a id="ne1.Coach.setup_dvs_biases"></a>

#### setup\_dvs\_biases

```python
def setup_dvs_biases(on_off_ratio=2) -> None
```

Sets all the DVS biases to default values.

**Arguments**:

- `on_off_ratio`: the ratio of Ion/Id and Id/Ioff

**Returns**:

ipr,isf,icas,idiff,ion,ioff,irefr
The actual programmed bias currents in Amps

<a id="ne1.Coach.set_dvs_threshold_biases"></a>

#### set\_dvs\_threshold\_biases

```python
def set_dvs_threshold_biases(on_off_ratio: float) -> (float, float, float)
```

Sets just the DVS threshold biases for the change detector and comparators

**Arguments**:

- `on_off_ratio`: the ratio of Ion/Id and Id/Ioff

**Returns**:

idiff,ion,ioff

<a id="ne1.Coach.filter_dvs_events"></a>

#### filter\_dvs\_events

```python
def filter_dvs_events(
    coach_events_list: list[pyplane.CoachOutputEvent]
) -> tuple[np.ndarray, np.ndarray]
```

After a call to `request_events(t)`, `filter_dvs_events` returns the timestamps of ON and OFF events.

:param coach_events_list: the list of CoachOutputEvent returned by `read_events()`

If you want signed ON and OFF events to plot with timestamps, you can do
```            
    on_ts,off_ts=p.filter_dvs_events(coach_events)
    on_vals=+1*np.ones_like(on_ts)
    off_vals=-1*np.ones_like(off_ts)
```
:return (on_timestamps, off_timestamps)
    Each of them is a 1d float numpy array of event timestamps in seconds.

NOTE that addresses that are not DVS addresses are filtered out! 
There could be other neuron circuits that generate events, and if these dominate the output,
then there could be problems with overruns.

See [Coach chip report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=share_link), Table 15, page 28 for event addresses.


<a id="ne1.Coach.set_led_intensity"></a>

#### set\_led\_intensity

```python
def set_led_intensity(intensity: int) -> None
```

Set the intensity of the stimulus LED to a value in the range 0 to 255.

The LED should be plugged into the board pins next to the CoACH chip; gnd side is clearly labeled.

This function is synchronous; it waits for success message.
It can achieve up to about 1kHz update rate.

**Arguments**:

- `intensity`: the intensity 0-255 value

<a id="ne1.Coach.setup_ahn"></a>

#### setup\_ahn

```python
def setup_ahn() -> None
```

Sets up the Axon-Hillock circuit.

<a id="ne1.Coach.set_ahn_vpw_ib"></a>

#### set\_ahn\_vpw\_ib

```python
def set_ahn_vpw_ib(coarse_current: pyplane.Coach.BiasGenMasterCurrent,
                   fine_value: int) -> float
```

Set the AHN reset bias current.

:param coarse_current: the pyplane.Coach.BiasGenMasterCurrent
:param fine_value: the fine value, 0-255
:return the actual programmed current in Amps


<a id="ne1.Coach.read_ahn_vout"></a>

#### read\_ahn\_vout

```python
def read_ahn_vout() -> float
```

Reads and returns the AHN Vmem voltage.

<a id="ne1.Coach.request_coach_output_events"></a>

#### request\_coach\_output\_events

```python
def request_coach_output_events(t: float) -> None
```

Starts collecting events; Enable events to be read using `read_events()`.

Events are received for the duration specified in seconds by the argument.
The timestamps in CoachOutputEvents are in units of 1.024 milliseconds.

**Arguments**:

- `t` (`float`): the time in seconds, max 64

<a id="ne1.Coach.read_coach_output_events"></a>

#### read\_coach\_output\_events

```python
def read_coach_output_events() -> list[pyplane.CoachOutputEvent]
```

Return CoachOutputEvents read from a queue which is filled in the background once request_events() has been called. 

See [Coach chip report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=share_link), Table 15, page 28 for event addresses.

**Returns**:

`list[pyplane.CoachOutputEvent]`: list of `pyplane.CoachOutputEvent` events. 
Each event is an (int,int) tuple of (address,timestamp).
The timestamps in CoachOutputEvents are in units of 1.024 milliseconds.

<a id="ne1.Coach.capture_coach_output_events"></a>

#### capture\_coach\_output\_events

```python
def capture_coach_output_events(t: float) -> list[pyplane.CoachOutputEvent]
```

Reads AER events from Coach.

**Arguments**:

- `t`: how long to wait for events in seconds

**Returns**:

the event list
Each event is an (int,int) tuple of (address,timestamp) but in native CoachOutputEvent form (C++ pybind object).
    See [Coach chip report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=share_link), Table 15, page 28 for event addresses.
The timestamps in CoachOutputEvents are in units of 1.024 milliseconds.

<a id="ne1.Coach.coach_events_to_timestamps_addresses"></a>

#### coach\_events\_to\_timestamps\_addresses

```python
def coach_events_to_timestamps_addresses(
        es: list[pyplane.CoachOutputEvent]) -> tuple[np.ndarray, np.ndarray]
```

Converts list of CoachOutputEvent to tuple (`timestamp`, `addresses`).

**Arguments**:

- `es`: list of CoachOutputEvent

**Returns**:

(timestamps,addresses)
The timestamps are in seconds. 
`timestamps` and `addresses` are np.ndarray 1d arrays.

<a id="ne1.Coach.setup_foi"></a>

#### setup\_foi

```python
def setup_foi()
```

Sets up the FOI (follower-integrator).

<a id="ne1.Coach.set_foi_vin"></a>

#### set\_foi\_vin

```python
def set_foi_vin(v1)
```

Sets FOI input Vin

**Arguments**:

- `v1`: volts

<a id="ne1.Coach.foi_compensate_vin"></a>

#### foi\_compensate\_vin

```python
def foi_compensate_vin(v)
```

Computes the offset compensated input voltage for the FOI

**Arguments**:

- `v`: Input voltage to calculate compensation of

**Returns**:

The offset compensated input voltage for the FOI

<a id="ne1.Coach.set_foi_ib"></a>

#### set\_foi\_ib

```python
def set_foi_ib(bias_coarse: pyplane.Coach.BiasGenMasterCurrent,
               fine_value: int)
```

Sets the bias current of the FOI follower integrator.

**Arguments**:

- `bias_coarse`: A coarse value of current.
allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA.
See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
- `fine_value`: 0-255 int fine value.
0 should not really be used since the current is badly defined.

**Returns**:

the bias current.

<a id="ne1.Coach.measure_foi_waveform"></a>

#### measure\_foi\_waveform

```python
def measure_foi_waveform(interval: float)
```

Measure waveform response from follower integrator

**Arguments**:

- `interval`: Interval of measurement
Input waveform must first be set using set_voltage_waveform()

<a id="ne1.Coach.setup_c2f"></a>

#### setup\_c2f

```python
def setup_c2f() -> None
```

Sets up the C2F biases.
NOTE: the correct C2F channels must be selected for any measurements to make sense.
@see 
For example
```
    # configure wide-range TransAmp
    self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(                         pyplane.Coach.CurrentOutputSelect.SelectLine5,                         pyplane.Coach.VoltageOutputSelect.SelectLine1,                         pyplane.Coach.VoltageInputSelect.SelectLine2,                         pyplane.Coach.SynapseSelect.NoneSelected, 0)])

```

<a id="ne1.Coach.measure_c2f_freqs"></a>

#### measure\_c2f\_freqs

```python
def measure_c2f_freqs(duration=0.1) -> list
```

Measures all the C2F frequencies and returns the array of measurements.

**Arguments**:

- `duration`: how long to measure event rate for in seconds

**Returns**:

16 C2F frequencies in Hz

<a id="ne1.Coach.set_bias_from_tuple"></a>

#### set\_bias\_from\_tuple

```python
def set_bias_from_tuple(b)
```

Sets a bias from tuple of (address,type,course,fine) values. See `Coach.set_bias`.

**Returns**:

the bias current in A

<a id="ne1.Coach.set_bias"></a>

#### set\_bias

```python
def set_bias(bias_address: pyplane.Coach.BiasAddress,
             bias_type: pyplane.Coach.BiasType,
             coarse_current: pyplane.Coach.BiasGenMasterCurrent,
             fine_value: int) -> float
```

Set a particular bias. To use this class, import the pyplane class to access its constants. E.g.

```
        import pyplane
        from ne1 import Coach
        c=Coach()
        c.open
        c.set_bias(pyplane.Coach.BiasAddress.NDP_VB_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I30nA,
            30)
```

**Arguments**:

- `bias_address`: the particular bias, 
one of pyplane.Coach.BiasAddress, e.g. pyplane.Coach.BiasAddress.NDP_VB_N; see [BiasAddress in coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h).
See also Section 6.3/Table 7 of [Coach chip design report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=sharing).
- `bias_type`: the type of bias (N or P), 
see :py:class: typically pyplane.Coach.BiasType.N or pyplane.Coach.BiasType.P see [BiasType in coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h)
- `coarse_current`: one of pyplane.Coach.BiasGenMasterCurrent, e.g. pyplane.Coach.BiasGenMasterCurrent.I30nA; 
allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
- `fine_value`: 0-255 int fine value. 
0 should not really be used since the current is badly defined.

**Returns**:

the computed actual current in Amps as COARSE_CURRENTS[coarse_current]*fine_current/255

<a id="ne1.Coach.transient_response"></a>

#### transient\_response

```python
def transient_response(DAC: pyplane.DacChannel, ADC: pyplane.AdcChannel,
                       time_interval: float, V_step: float) -> list[float]
```

Acquire the transient response to a step function

**Arguments**:

- `DAC`: DAC channel to apply step function to
- `ADC`: ADC channel to read transient reponse from
- `time_interval`: Amount of time recorded after stimulation
- `V_step`: Voltage applied at the DAC
NB the method just sets the provided voltage V(t=0+) and starts to measure
immediatly. V(t=0-) is whatever is already present on the DAC.

From the pyplane API: Acquires a number of samples from the specified AdcChannel 
after applying a voltage step. Applies the values set using set_voltage_waveform() 
to the DacChannel given by the first argument and records samples from the AdcChannel 
given by the second argument at intervals given in seconds by the third argument. 
The first sample comes from before the voltage given by the fourth argument is applied; 
subsequent samples from subsequent time intervals. 
The results returned are in Volts or Amps, depending on the AdcChannel chosen.

**Returns**:

the list of voltages as floats

<a id="ne1.input_with_timeout"></a>

#### input\_with\_timeout

```python
def input_with_timeout(prompt, timeout=30)
```

get input with timeout

**Arguments**:

- `prompt`: the prompt to print
- `timeout`: timeout in seconds, or None to disable

**Raises**:

- `None`: TimeoutError if times out

**Returns**:

the input

<a id="ne1.yes_or_no_or_always"></a>

#### yes\_or\_no\_or\_always

```python
def yes_or_no_or_always(question, default='y', timeout=None)
```

Get Yes/No/Always answer with default choice and optional timeout

**Arguments**:

- `question`: prompt
- `default`: the default choice, i.e. 'y' or 'n' or 'a'
- `timeout`: the timeout in seconds, default is None

**Returns**:

'yes' or 'no' or 'always'

<a id="ne1.Timer"></a>

## Timer Objects

```python
class Timer()
```

<a id="ne1.Timer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(timer_name='', delay=None, show_hist=False, numpy_file=None)
```

Make a Timer() in a _with_ statement for a block of code.

The timer is started when the block is entered and stopped when exited.
The Timer _must_ be used in a with statement.

**Arguments**:

- `timer_name`: the str by which this timer is repeatedly called and which it is named when summary is printed on exit
- `delay`: set this to a value to simply accumulate this externally determined interval
- `show_hist`: whether to plot a histogram with pyplot
- `numpy_file`: optional numpy file path

<a id="ne1.Timer.print_timing_info"></a>

#### print\_timing\_info

```python
def print_timing_info(logger=None)
```

Prints the timing information accumulated for this Timer

**Arguments**:

- `logger`: write to the supplied logger, otherwise use the built-in logger

