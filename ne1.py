# Utilities for NE1 labs, mainly the Coach() class for working with CoACH chip using pyplane
# Author: Tobi Delbruck, 2017-2023 (with logging and yes/no code lifted from v2e and other projects)

# use lines below for debugging a pyplane build that is not in your startup folder
import sys
sys.path.append('/home/tobi/GitLab/CoACH_Teensy_interface/build/pc/pyplane')
import pyplane # suceeeds if the .so is on that build folder


import os
import platform
import glob
import time
import signal
import time
import numpy as np
from matplotlib import pyplot as plt
import pyplane # unfortunately we cannot import the nested classes like BiasAddress; see https://stackoverflow.com/questions/22885489/python-import-nested-classes-shorthand
from engineering_notation import EngNumber as ef
# printing values in engineering format, e.g. ef(2.3e-9)='2.3n'
from deprecated import deprecated  # to mark methods here as deprecated, note this comes from Deprecated package https://pypi.org/project/Deprecated/
import logging
# general logger. Produces nice output format with live hyperlinks for pycharm users
# to use it, just call log=get_logger() at the top of your Python file
# all these loggers share the same logger name 'NE1'

_LOGGING_LEVEL = logging.INFO  # usually INFO is good


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""
    # see https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output/7995762#7995762

    # \x1b[ (ESC[) is the CSI introductory sequence for ANSI https://en.wikipedia.org/wiki/ANSI_escape_code
    # The control sequence CSI n m, named Select Graphic Rendition (SGR), sets display attributes.
    grey = "\x1b[2;37m"  # 2 faint, 37 gray
    yellow = "\x1b[33;21m"
    cyan = "\x1b[0;36m"  # 0 normal 36 cyan
    green = "\x1b[31;21m"  # dark green
    red = "\x1b[31;21m"  # bold red
    bold_red = "\x1b[31;1m"
    light_blue = "\x1b[1;36m"
    blue = "\x1b[1;34m"
    reset = "\x1b[0m"
    # File "{file}", line {max(line, 1)}'.replace("\\", "/")
    format = '[%(levelname)s]: %(asctime)s - %(name)s - %(message)s (File "%(pathname)s", line %(lineno)d, in %(funcName)s)'

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: cyan + format + reset,
        logging.WARNING: red + format + reset,
        logging.ERROR: bold_red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        # replace \ with / for pycharm links
        return formatter.format(record).replace("\\", "/")


def get_logger():
    """
    Use get_logger to define a logger with useful color output and info and warning turned on according to the global LOGGING_LEVEL.

    :returns: the logger.
    """
    # logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    # tobi changed so all have same name so we can uniformly affect all of them
    logger = logging.getLogger('NE1')
    logger.setLevel(_LOGGING_LEVEL)
    # create console handler if this logger does not have handler yet
    if len(logger.handlers) == 0:
        ch = logging.StreamHandler()
        ch.setFormatter(CustomFormatter())
        logger.addHandler(ch)
    return logger


log = get_logger()

# def import_ne1_modules():
#     import inspect,importlib
#     frame = inspect.currentframe().
#     importlib.import_module('pyplane')
#     try:
#         locals = frame.f_locals
#     finally:
#         del frame


# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
from functools import lru_cache
@lru_cache(maxsize=None)
class Coach():
    """
    A wrapper for pyplane to make it easier to use in Python notebooks. 
    NOTE Coach() is a singleton - you can only create one instance of it in a Python run.

    The main methods are open(), close(), and setup_XXX() methods. These setup experiments and simplify the measurements.

    There are also methods for setting up measuring the C2F output frequencies and for setting biases.
    """

    # the default USB port that Teensy appears on https://rfc1149.net/blog/2013/03/05/what-is-the-difference-between-devttyusbx-and-devttyacmx/
    DEFAULT_USB_PORT = '/dev/ttyACM0'
    """ The default USB port that Plane PCB appears on, usually. """
    # POSSIBLE_DEVICES=('/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyUSB0', '/dev/ttyUSB1')
    # the most recent firmware version. If board has different version user is warned
    _FIRMWARE_VERSION_LATEST = (1, 12, 5)
    """ The most recent version of Plane PCB firmware. """

    def __init__(self, logging_level=_LOGGING_LEVEL):
        """ Make or return existing CoACH device. Coach() is a wrapper for pyplane to make it easier to use in Python notebooks.

            The main methods are open(), close(), and setup_XXX() methods. These setup experiments and simplify the measurements.

            There are also methods for setting up measuring the C2F output frequencies and for setting biases.

        :param logging_level: set the logging level, e.g. logging.DEBUG. Default is logging.INFO
        """
        # create a Plane object
        # we only make the pyplane object to use it to talk to CoACH chip when we open it
        self.plane = None # perhaps destroy existing plane object, which should close any serial interface to it
        self.open_flag = False
        log.setLevel(logging_level)

    def __del__(self):
        """We override the default destructor to make sure the Pyplane object is deleted"""
        if self.is_open():
            log.info(f'board was open, closing plane before deleting it')
            self.close()

# NOTE open/close/find

    def open(self, usbport: str = None) -> None:
        """ Opens the CoACH Plane PCB

        :param usbport: the name of the Teensy USB port, if None, then try to scan for Teensyduino
        
        :raises: RunTimeError if board cannot be opened or there is a timeout or there is a firmware mismatch
        """
        if self.is_open():
            log.info('was already open')
            return
        self.open_flag = False

        self.plane = pyplane.Plane()
        plane_version = pyplane.get_version()
        if plane_version != self._FIRMWARE_VERSION_LATEST:
            log.warning(f'The pyplane version {plane_version} is different than the latest firmware version {self._FIRMWARE_VERSION_LATEST}; you might be running obsolete pyplane PC library')

        dev = self.find_coach() if usbport is None else usbport
        if dev is None:
            raise RuntimeError(
                f'no CoACH board found on USB bus. Did you forget to attach it? \nPlease check https://code.ini.uzh.ch/CoACH/CoACH-labs/-/blob/master/readme.md#troubleshooting-your-coach-chip-setup.')
        try:
            log.debug(f'Trying to open {dev}')
            self.plane.open(dev)  # open the serial port
            fw_version = self.get_firmware_version()
            if fw_version != self._FIRMWARE_VERSION_LATEST:
                if fw_version == (255, 255, 255):
                    raise TimeoutError(
                        f'TimeoutError: {dev} firmware version is (255,255,255) which means it timed out; \n *** Please check if your firmware is out of date or you will experience timeout problems! *****\n Ask your TA for help; see https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface')
                if sum(fw_version) < sum(self._FIRMWARE_VERSION_LATEST):
                    log.error(
                        f'******** Board firmware version {fw_version} is not the latest firmware version {self._FIRMWARE_VERSION_LATEST}; \n *** Please update firmware or you will experience timeout problems! *****\n See https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface')
                elif sum(fw_version) > sum(self._FIRMWARE_VERSION_LATEST):
                    log.error(
                        f'******** Your board firmware version {fw_version} is NEWER than the supposed latest firmware version {self._FIRMWARE_VERSION_LATEST}; \n *** Please ask your TAs to update _FIRMWARE_VERSION')
            else:
                log.debug(
                    f'The board firmware version {fw_version} is the same as the latest firmware version {self._FIRMWARE_VERSION_LATEST}')
                log.info(
                    f'Opened CoACH at {dev} with firmware version {fw_version}')
                self.open_flag = True
        except (RuntimeError, TimeoutError) as e:
            raise RuntimeError(
                f'{dev} did not open; got {e}.\nPlease check https://code.ini.uzh.ch/CoACH/CoACH-labs/-/blob/master/readme.md#troubleshooting-your-coach-chip-setup.')

    def find_coach(self) -> str:
        """ Finds the CoACH board USB device if it is there.

        :return: the device name, e.g. /dev/ttyACM0, or None if it is not found
        """
        uname = platform.uname().system
        if uname == "Linux":
            from pyudev import Context, Monitor
            VID = '16c0'
            PID = '0483'
            VENDOR_NAMES = ('Teensyduino')

            ctx = Context()
            # devs=ctx.list_devices()
            # devs=ctx.list_devices(ID_BUS='usb')
            # devs=ctx.list_devices(subsystem='tty', ID_BUS='usb')
            devs = ctx.list_devices(subsystem='tty')

            device_count = 0
            for d in devs:
                log.debug(f'checking {d} if it is CoACH board')
                device_count += 1
                device_node = d.device_node
                if device_node == '/dev/ttyACM0':
                    log.debug(
                        f'Found probable CoACH at d.sys_name={d} with d.device_node={d.device_node}')
                    return d.device_node
                try:
                    vendor_name = d.properties['ID_VENDOR']
                    vid = d.properties['ID_VENDOR_ID']
                    pid = d.properties['ID_MODEL_ID']
                except KeyError:
                    continue
                log.debug(
                    f'Found {device_node} which is a {vendor_name} device with VID:PID={vid}:{pid}')
                if vendor_name in VENDOR_NAMES and vid == VID and pid == PID:
                    log.info(f'Found CoaACH at {device_node}')
                    return device_node
            if device_count == 0:
                log.error(f'pyudev did not enumerate any tty USB devices')
            else:
                log.warning(
                    f'could not find the Coach board among the {device_count} USB devices')
            return None
        elif uname == "Darwin":
            devs = glob.glob("/dev/cu.usb*")
            if len(devs) < 1:
                raise ValueError("could not find the CoACH board")
            elif len(devs) > 1:
                raise ValueError("too many USB serial devices connected, cannot guess which is the CoACH board")
            return devs[0]
        else:
            raise ValueError("Unsupported Operating System")

    def is_open(self) -> bool:
        """ check if board is open

        :return: True if open and firmware version is not error timeout value
        """
        if self.plane is None or not self.open_flag:
            return False
        if self.open_flag and self.get_firmware_version() == (255, 255, 255):
            return False
        return True

    def close(self) -> None:
        """Closes the board. Deletes the pyplane.Plane() object. """
        if not self.plane is None:
            log.info('closing device (deleting pyplane.Plane() object')
            del self.plane
            time.sleep(.5) # to give time for cleanup
        self.plane=None

    def check_open(self) -> None:
        """ Checks if open and opens if not. """
        if not self.is_open():
            self.open()

    def get_firmware_version(self) -> tuple:
        """ returns the firmware version

        :return: a 3-tuple, e.g. (1,24,12)
        """
        if self.plane is None:
            log.error('Not open; use open() first')
            return
        return self.plane.get_firmware_version()

    def get_pyplane(self) -> pyplane.Plane:
        """ Returns the low level pyplane object"""
        return self.plane

    def reset_soft(self) -> None:
        """Do a soft reset. This 
        1. turns off AER output, LEDs, DAC outputs
        2. sets analog read resolution to 12 bits 
        3. Sets read averaging to 4

        """
        self.check_open()
        self.plane.reset(pyplane.ResetType.Soft)

    def reset_hard(self) -> None:
        """
        Do a hard reset. This operation requires several seconds. It
        
            1. Asks the Teensy to initiate a full reset of the Teensy and everything resettable on the board.
            2. Waits for the Teensy to say that it can do a hard reset (boards <v0.4 cannot). (The Teensy then waits to give us a chance to close the USB connection before it actually performs the reset).
            3. Closes the USB connection.
            4. Waits for what we hope will be long enough for the Teensy to reset (this is of course racy)
            5. Tries to reconnect to the Teensy using the same device name with which it was opened.
            6. Checks that the board that it has now connected to has the same serial number as the board that it was connected to before the reset.

        NOTE: This call will block the Coach board from being accessed for at least 5 seconds
        """
        self.check_open()
        log.warning('Doing a HARD reset. Board will be disconnected from host.')
        self.plane.reset(pyplane.ResetType.Hard)

    def set_debug(self, yes:bool)->None:
        """ Enables or disables debug mode for pyplane.
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
        :param yes: set True to turn on debugging.
        """
        self.check_open()
        self.get_pyplane().debug=yes



    # NOTE NFET

    def setup_nfet(self) -> None:
        """ Setup the nfet for measurement"""
        self.check_open()
        self.check_open()
        # configure muxes to measure NFET
        events = [pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine5,
            pyplane.Coach.VoltageOutputSelect.NoneSelected,
            pyplane.Coach.VoltageInputSelect.SelectLine2,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)]

        self.plane.send_coach_events(events)
        log.debug('setup NFET measurement')

    def set_nfet_vg(self, v) -> float:
        """ set the nfet gate voltage

        :return: the actual voltage set after DAC quantization
        """
        self.check_open()
        self.plane.set_voltage(pyplane.DacChannel.AIN0, v)
        return self.plane.get_set_voltage(pyplane.DacChannel.AIN0)

    def set_nfet_vb(self, v) -> int:
        """ does nothing, since nfet bulk is always zero"""
        if v != 0:
            log.warning(
                f'The NFET bulk is ground by definition; you cannot set it to {v}V')
        pass  # does nothing, the bulk is always ground for nfets
        return 0

    def set_nfet_vs(self, v) -> float:
        """ set the nfet source voltage"""
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.GO20, v)
        return v

    def set_nfet_vd(self, v) -> float:
        """ set the nfet drain voltage"""
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.GO22, v)
        return v

    def measure_nfet_id(self) -> float:
        """ measure the nfet drain current and return it

        :return: the current in amps
        """
        self.check_open()
        i = self.plane.read_current(pyplane.AdcChannel.GO22)
        return i

    def measure_nfet_is(self) -> float:
        """ measure the nfet source current and return it

        :return: the current in amps
        """
        self.check_open()
        i = self.plane.read_current(pyplane.AdcChannel.GO20_N)
        return i

# NOTE NFET and PFET arrays (NFA and PFA)

    # the length in um of the NFETs in the NFA are (N+1)*NFA_LENGTHS_UNIT_UM where N is the C2F channel number
    NFA_LENGTHS_UNIT_UM = 0.18

    def setup_nfa(self) -> None:
        """Sets up the NFET array.  

        Set the common gate voltages with `set_nfa_vg()` and read
        the drain currents with `measure_c2f_freqs()`. 

        The 16 C2F channels are the 16 FETs.

        The FET lengths are  in `(N+1)*NFA_LENGTHS_UNIT_UM` where `N` is the C2F channel number.
        """
        self.check_open()
        self.setup_c2f()
        import pyplane

        # configure nfet array C2Fs
        # they are on C2F select line 0
        # the gate voltage input is on Select 2
        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine0,
            pyplane.Coach.VoltageOutputSelect.SelectLine1,
            pyplane.Coach.VoltageInputSelect.SelectLine2,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)])

    def set_nfa_vg(self, vgn) -> float:
        """Sets the NFET array gate voltage

        :param vgn: the gate voltage
        :return: the quantized voltage
        """
        self.check_open()
        return self.plane.set_voltage(pyplane.DacChannel.AIN1, vgn)

    def setup_pfa(self) -> None:
        """Sets up the PFET array.  

        Set the common gate voltages with `set_nfa_vg()` and read
        the drain currents with `measure_c2f_freqs()`. 

        The 16 C2F channels are the 16 FETs.

        The FET lengths are  in `(N+1)*NFA_LENGTHS_UNIT_UM` where `N` is the C2F channel number.
        """
        self.check_open()
        self.setup_c2f()
        import pyplane

        # configure pfet array C2Fs
        # they are on C2F select line 1 (Table 8 of https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=sharing)
        # the gate voltage input is on Select 1 (Table 3 of chip_architecture.pdf https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=sharing)
        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine1,
            pyplane.Coach.VoltageOutputSelect.SelectLine1,
            pyplane.Coach.VoltageInputSelect.SelectLine1,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)])  # TODO not checked yet

    def set_pfa_vg(self, vgp) -> float:
        """Sets the PFET array gate voltage

        :param vgp: the gate voltage
        :return: the quantized voltage
        """
        self.check_open()
        # TODO not checked
        return self.plane.set_voltage(pyplane.DacChannel.AIN2, vgp)


# NOTE PFET


    def setup_pfet(self) -> None:
        """ setup the PFET for measurement"""
        self.check_open()
        # configure muxes to measure PFET
        events = [pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine5,
            pyplane.Coach.VoltageOutputSelect.NoneSelected,
            pyplane.Coach.VoltageInputSelect.SelectLine1,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)]

        self.plane.send_coach_events(events)
        log.debug('setup PFET measurement')

    def set_pfet_vg(self, v) -> float:
        """ set the pfet gate voltage

        :return: the actual voltage set after DAC quantization
        """
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN0, v)
        return v

    def set_pfet_vb(self, v) -> float:
        """ set the pfet bulk voltage"""
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN1, v)
        return v

    def set_pfet_vs(self, v) -> float:
        """ set the pfet source voltage"""
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.GO23, v)
        return v

    def set_pfet_vd(self, v) -> float:
        """ set the pfet drain voltage"""
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.GO21, v)
        return v

    def measure_pfet_id(self) -> float:
        """ measure the pfet source current and return it

        :return: the current in amps
        """
        self.check_open()
        i = self.plane.read_current(
            pyplane.AdcChannel.GO23)  # note here we measure the PFET current at its drain
        return i

    def measure_pfet_is(self) -> float:
        """ measure the pfet source current and return it

        :return: the current in amps
        """
        self.check_open()
        i = self.plane.read_current(
            pyplane.AdcChannel.GO21_N)  # note here we measure the PFET current at its source
        return i

# NOTE diff pair (n type) NDP
    NDP_I1_C2F_CHANNEL = 0
    NDP_I2_C2F_CHANNEL = 1

    @deprecated('Use setup_ndp() instead')
    def setup_diffpair_n(self):
        """ Sets up n-type diff pair  """

        self.setup_ndp()

    @deprecated('Use set_ndp_v1() instead')
    def set_diffpair_n_v1(self, v1):
        """ Sets NDP V1

        :param v1: the voltage
        :return: its quantized value
        """
        return self.set_ndp_v1(v1)

    @deprecated('Use set_ndp_v2() instead')
    def set_diffpair_n_v2(self, v2: float):
        """ Sets NDP V2

        :param v2: the voltage
        :return: its quantized value
        """
        return self.set_ndp_v2(v2)

    @deprecated('Use set_ndp_ib() instead')
    def set_diffpair_n_ib(self, bias_coarse: pyplane.Coach.BiasGenMasterCurrent, fine_value):
        """Sets the bias current of the NDP (n type diff pair). """
        return self.set_ndp_ib(bias_coarse, fine_value)

# NOTE synonyms for NDP
    def setup_ndp(self) -> None:
        """ Sets up n-type diff pair. """
        self.check_open()
        self.setup_c2f()

        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine5,
            pyplane.Coach.VoltageOutputSelect.NoneSelected,
            pyplane.Coach.VoltageInputSelect.SelectLine2,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)])

    def set_ndp_v1(self, v1) -> float:
        """ Sets NDP V1

        :param v1: the voltage
        :return: its quantized value
        """
        self.check_open()
        return self.plane.set_voltage(pyplane.DacChannel.AIN5, v1)  # V1 = 0.6

    def set_ndp_v2(self, v2) -> float:
        """ Sets NDP V2

        :param v2: the voltage
        :return: its quantized value
        """
        self.check_open()
        return self.plane.set_voltage(pyplane.DacChannel.AIN6, v2)  # V2 = 0.2

    def set_ndp_ib(self, bias_coarse: pyplane.Coach.BiasGenMasterCurrent, fine_value) -> float:
        """Sets the bias current of the NDP (n type diff pair).

        :param bias_coarse: A coarse value of current.
            allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
            See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
        :param fine_value: 0-255 int fine value. 
            0 should not really be used since the current is badly defined.
        """
        self.check_open()
        ib = self.set_bias(pyplane.Coach.BiasAddress.NDP_VB_N,
                           pyplane.Coach.BiasType.N,
                           bias_coarse, int(fine_value))
        return ib

# NOTE bump circuit BAB
    BAB_I1_C2F_CHANNEL = 5
    BAB_I2_C2F_CHANNEL = 6
    BAB_IOUT_C2F_CHANNEL = 7

    def setup_bab(self) -> None:
        """ Setup the Bump Anti Bump (BAB) circuit."""
        self.check_open()
        self.setup_c2f()

        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine5,
            pyplane.Coach.VoltageOutputSelect.NoneSelected,
            pyplane.Coach.VoltageInputSelect.SelectLine2,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)])

    def set_bab_v1(self, v1) -> float:
        """Sets the V1 input of the BAB

        :param v1: the voltage
        :return: the actual quantized voltage
        """
        self.check_open()
        return self.plane.set_voltage(pyplane.DacChannel.AIN12, v1)

    def set_bab_v2(self, v2) -> float:
        """Sets the V2 input of the BAB

        :param v2: the voltage
        :return: the actual quantized voltage
        """
        self.check_open()
        return self.plane.set_voltage(pyplane.DacChannel.AIN13, v2)

    def set_bab_ib(self, coarse_current_bab: pyplane.Coach.BiasGenMasterCurrent, fine_current_bab) -> float:
        """Sets the bias current of the BAB bump-antibump circuit. 

        :param bias_coarse: A coarse value of current.
            allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
            See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
        :param fine_value: 0-255 int fine value. 
            0 should not really be used since the current is badly defined.
        :return: the bias current.
            This function accounts for the W/L ratio of BAB bias FET.
        """
        w_bab = 3  # the Ib FET in BAB has W/L ratio of 3 compared the W/L ratio of the bias circuit. Its bias current will be larger than the returned bias current by approximately this ratio
        Ib_bab = w_bab*self.set_bias(
            pyplane.Coach.BiasAddress.BAB_VB_N,
            pyplane.Coach.BiasType.N,
            coarse_current=coarse_current_bab, fine_value=fine_current_bab)
        return Ib_bab

    def setup_r2r_buffer(self)->None:
        ''' Sets up the rail to rail buffer for all analog outputs'''
        # setup output rail-to-rail buffer
        self.set_bias(
            pyplane.Coach.BiasAddress.RR_BIAS_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I240nA, 255)
        log.debug('setup rail to rail (RR) output analog voltage buffer')


# NOTE n-type transamp (NTA)

    NTA_I1_C2F_CHANNEL = 11  # Iplus channel for NTA with output clamped to 1V
    NTA_I2_C2F_CHANNEL = 12  # Iminus channel for NTA with output clamped to 1V

    # the Vout ADC channel for the 3d NTA that is open-circuited
    NTA_VOUT_ADC_CHANNEL = pyplane.AdcChannel.AOUT13

    def setup_nta(self) -> None:
        """Sets up the NTA (n-type 5-T transamp)."""
        self.check_open()
        self.setup_c2f()

        # setup output p-type rail-to-rail buffer
        self.setup_r2r_buffer()

        # configure N type TransAmp
        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine5,
            pyplane.Coach.VoltageOutputSelect.SelectLine1,
            pyplane.Coach.VoltageInputSelect.SelectLine2,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)])

        log.debug('setup NTA')

    def set_nta_ib(self, bias_coarse: pyplane.Coach.BiasGenMasterCurrent, fine_value: int) -> float:
        """Sets the bias current of the NTA.

        :param bias_coarse: A coarse value of current.
            allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
            See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
        :param fine_value: 0-255 int fine value. 
            0 should not really be used since the current is badly defined.
        :return: the bias current.
        """
        self.check_open()
        ib = self.set_bias(pyplane.Coach.BiasAddress.NTA_VB_N,
                           pyplane.Coach.BiasType.N,
                           bias_coarse, int(fine_value))
        return ib

    def set_nta_v1(self, v1) -> float:
        """Sets NTA V1 input

        :param v1: volts 
        """
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN3, v1)
        return v

    def set_nta_v2(self, v2) -> float:
        """ Sets NTA V2 input

        :param v2: volts
        """
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN4, v2)
        return v

    def measure_nta_vout(self) -> float:
        self.check_open()
        v = self.plane.read_voltage(pyplane.AdcChannel.AOUT13)
        return v

# NOTE p-type transamp (PTA)

    PTA_I1_C2F_CHANNEL = 13  # Iplus channel for PTA with output clamped to 1V
    PTA_I2_C2F_CHANNEL = 14  # Iminus channel for PTA with output clamped to 1V

    # the Vout ADC channel for the 3d PTA that is open-circuited
    PTA_VOUT_ADC_CHANNEL = pyplane.AdcChannel.AOUT12

    def setup_pta(self) -> None:
        """Sets up the PTA (p-type 5-T transamp)."""
        self.check_open()
        self.setup_c2f()

        # setup output p-type rail-to-rail buffer
        self.setup_r2r_buffer()

        # configure P type TransAmp
        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine5,
            pyplane.Coach.VoltageOutputSelect.SelectLine1,
            pyplane.Coach.VoltageInputSelect.SelectLine1,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)])

        log.debug('setup PTA')

    def set_pta_ib(self, bias_coarse: pyplane.Coach.BiasGenMasterCurrent, fine_value) -> float:
        """Sets the bias current of the PTA.

        :param bias_coarse: A coarse value of current.
            allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
            See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
        :param fine_value: 0-255 int fine value. 
            0 should not really be used since the current is badly defined.
        :return: the bias current.
        """
        self.check_open()
        ib = self.set_bias(pyplane.Coach.BiasAddress.PTA_VB_P,
                           pyplane.Coach.BiasType.P,
                           bias_coarse, int(fine_value))
        return ib

    def set_pta_v1(self, v1) -> float:
        """Sets PTA V1 input

        :param v1: volts 
        """
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN7, v1)
        return v

    def set_pta_v2(self, v2) -> float:
        """ Sets PTA V2 input

        :param v2: volts
        """
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN8, v2)
        return v

    def measure_pta_vout(self) -> float:
        self.check_open()
        v = self.plane.read_voltage(pyplane.AdcChannel.AOUT13)
        return v

# NOTE n-type wide output range transamp (WRT)

    # the Vout ADC channel for the 3d PTA that is open-circuited
    WRT_VOUT_ADC_CHANNEL = pyplane.AdcChannel.AOUT11

    def setup_wrt(self) -> None:
        """Sets up the WRT (wide output range transamp). Note only the Vout node can be measured in open loop."""
        self.check_open()
        self.setup_c2f()

        # setup output rail-to-rail buffer
        self.setup_r2r_buffer()

        # configure wide-range TransAmp
        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine5,
            pyplane.Coach.VoltageOutputSelect.SelectLine1,
            pyplane.Coach.VoltageInputSelect.SelectLine2,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)])

        log.debug('setup WRT')

    def set_wrt_ib(self, bias_coarse: pyplane.Coach.BiasGenMasterCurrent, fine_value):
        """Sets the bias current of the WRT.

        :param bias_coarse: A coarse value of current.
            allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
            See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
        :param fine_value: 0-255 int fine value. 
            0 should not really be used since the current is badly defined.
        """
        self.check_open()
        ib = self.set_bias(pyplane.Coach.BiasAddress.WRT_VB_N,
                           pyplane.Coach.BiasType.N,
                           bias_coarse, int(fine_value))
        return ib

    def set_wrt_v1(self, v1):
        """Sets PTA V1 input

        :param v1: volts 
        """
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN7, v1)
        return v

    def set_wrt_v2(self, v2):
        """ Sets PTA V2 input

        :param v2: volts
        """
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN8, v2)
        return v

    def measure_wrt_vout(self):
        """Returns the WRT output voltage."""
        self.check_open()
        v = self.plane.read_voltage(self.WRT_VOUT_ADC_CHANNEL)
        return v

# NOTE disable all AER sources (neurons, DVS pixel)
    def disable_all_aer_event_sources(self) -> None:
        # disable synapses
        self.set_bias(
            pyplane.Coach.BiasAddress.LDS_VTAU_P,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.DPI_VTAU_P,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.DDI_VTAU_P,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        # disable axon-hillock neuron, set reset to max to prevent input from making spikes
        self.set_bias(
            pyplane.Coach.BiasAddress.AHN_VPW_N,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        # disable thresholded neuron
        self.set_bias(
            pyplane.Coach.BiasAddress.ATN_VLEAK_N,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.ATN_VDC_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.ATN_VGAIN_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.ATN_VSPKTHR_P,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        # disable sigma-delta neuron
        self.set_bias(
            pyplane.Coach.BiasAddress.ASN_VLEAK_N,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.ASN_VDC_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.ASN_VGAIN_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        # disable exp neuron
        self.set_bias(
            pyplane.Coach.BiasAddress.ACN_VLEAK_N,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.ACN_VGAIN_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.ACN_VDC_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.ACN_VREFR_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I240nA, 255)

        # disable Hodgkin-Huxley neuron
        self.set_bias(
            pyplane.Coach.BiasAddress.HHN_VBUF_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.HHN_VCABUF_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.HHN_VDC_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.HHN_VELEAK_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        # disable DVS pixels
        self.set_bias(
            pyplane.Coach.BiasAddress.DVS_DIFF_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.DVS_CAS_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.DVS_ON_N,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.DVS_OFF_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.DVS_SF_P,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.DVS_PR_P,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        self.set_bias(
            pyplane.Coach.BiasAddress.DVS_REFR_P,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 0)

        log.debug('disabled all AER neuron and DVS sources by biasing them off')


################################################################ NOTE DVS pixel

    DVS_ON_ADDRESS=5
    DVS_OFF_ADDRESS=6
    
    def setup_dvs(self, on_off_ratio=2, settle_duration=5) -> None:
        """ Sets up the DVS pixel. 

        :param on_off_ratio: the desired ratio of Ion/Id and Id/Ioff
        :param settle_duration: how long to settle in seconds,  since we are turning on DVS pixel that was totally disabled
        
        See [Coach chip report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=share_link), Table 15, page 28 for event addresses.
        
        :return: ipr,isf,icas,idiff,ion,ioff,irefr
            The actual programmed bias currents in Amps

        """
        self.check_open()
        # self.reset_soft()
        self.disable_all_aer_event_sources()
        ipr,isf,icas,idiff,ion,ioff,irefr=self.setup_dvs_biases(on_off_ratio=on_off_ratio)
        # select lines and neuron latches - set mysterious misc flag to 0, TODO not clear what is the effect, seems to be a synapse switch selection
        # select lines and neuron latches
        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine6,
            pyplane.Coach.VoltageOutputSelect.SelectLine2,
            pyplane.Coach.VoltageInputSelect.NoneSelected,
            pyplane.Coach.SynapseSelect.NoneSelected, 0)])

        log.info(f'sleeping {settle_duration} seconds for DVS to settle')
        time.sleep(settle_duration)
        log.info('setup DVS pixel')
        return ipr,isf,icas,idiff,ion,ioff,irefr

    DVS_DIFF_FINE_VAL=16 
    """ Coarse bias of DVS pixel change detector """
    DVS_DIFF_CB=pyplane.Coach.BiasGenMasterCurrent.I30nA
    """ Nominal fine value of DVS change detector """
    DVS_DIFF_ON_OFF_RATIO=2
    """ Nominal value of DVS change detector current ratios """
    DVS_DEFAULT_BIASES={
        'pr': (pyplane.Coach.BiasAddress.DVS_PR_P,      pyplane.Coach.BiasType.P, pyplane.Coach.BiasGenMasterCurrent.I3_8nA,     200), 
        'sf': (pyplane.Coach.BiasAddress.DVS_SF_P,      pyplane.Coach.BiasType.P, pyplane.Coach.BiasGenMasterCurrent.I60pA,    64 ),
        'cas': (pyplane.Coach.BiasAddress.DVS_CAS_N,    pyplane.Coach.BiasType.N, pyplane.Coach.BiasGenMasterCurrent.I240nA,    25),
        'diff': (pyplane.Coach.BiasAddress.DVS_DIFF_N,  pyplane.Coach.BiasType.P, DVS_DIFF_CB, DVS_DIFF_FINE_VAL),
        'on': (pyplane.Coach.BiasAddress.DVS_DIFF_N,    pyplane.Coach.BiasType.P, DVS_DIFF_CB, DVS_DIFF_FINE_VAL*DVS_DIFF_ON_OFF_RATIO),
        'off': (pyplane.Coach.BiasAddress.DVS_DIFF_N,   pyplane.Coach.BiasType.P, DVS_DIFF_CB, DVS_DIFF_FINE_VAL/DVS_DIFF_ON_OFF_RATIO),
        'refr': (pyplane.Coach.BiasAddress.DVS_REFR_P,  pyplane.Coach.BiasType.P, pyplane.Coach.BiasGenMasterCurrent.I60pA,     255)
        }
    """ Default values of DVS pixel biases, each one is a tuple of (address, type, coarse, fine). You can find out a default value with  from `DVS_DEFAULT_BIASES['sf']`, for example. """
        
    def setup_dvs_biases(self, on_off_ratio=2) -> None:
        """Sets all the DVS biases to default values.
        :param on_off_ratio: the ratio of Ion/Id and Id/Ioff
        :return: ipr,isf,icas,idiff,ion,ioff,irefr
            The actual programmed bias currents in Amps
        """
        # change bias buffer bias 
        ibuffer=self.set_bias(pyplane.Coach.BiasAddress.BUFFER,pyplane.Coach.BiasType.N,
                              pyplane.Coach.BiasGenMasterCurrent.I240nA,255)
        
        def set_dvs_bias(name)->float:
            return self.set_bias_from_tuple(self.DVS_DEFAULT_BIASES[name])

        # photoreceptor and source follower
        ipr= set_dvs_bias('pr')  # bias PR strongly
        isf=set_dvs_bias('sf')  # lowpass filter output with source follower

        # Cascode
        icas=set_dvs_bias('cas') # bias cascode hard to make sure it is working

        # change detector
        idiff,ion,ioff=self.set_dvs_threshold_biases(on_off_ratio)

        # refractory period
        irefr=set_dvs_bias('refr')
        
        s='\nbias\t\t\tcurrent(A)\n'
        def printi(a,b):
            return f'{a}\t\t\t{ef(b)}\n'
        s+=printi('pr',ipr)
        s+=printi('sf',isf)
        s+=printi('cas',icas)
        s+=printi('idiff',idiff)
        s+=printi('ion',ion)
        s+=printi('ioff',ioff)
        s+=printi('irefr',irefr)
        s+=f'ion/idiff={(ion/idiff):.1f}, idiff/ioff={(idiff/ioff):.1f}\n'
        log.info(s)
        return ipr,isf,icas,idiff,ion,ioff,irefr

    def set_dvs_threshold_biases(self,on_off_ratio:float)-> (float,float,float):
        """
        Sets just the DVS threshold biases for the change detector and comparators
        
        :param on_off_ratio: the ratio of Ion/Id and Id/Ioff
        :return: idiff,ion,ioff
        """
        # change amplifier, ON and OFF thresholds
        # choose fine value to maximize range f of on/diff and diff/off ratios
        # diff*f<=255 and diff/f>=1
        # f<=255/diff and f<=diff
        # diff=255/diff
        # diff^2=255
        # diff=sqrt(255)=15.9=16
        if on_off_ratio*self.DVS_DIFF_FINE_VAL>255 or self.DVS_DIFF_FINE_VAL/on_off_ratio<1:
            raise ValueError(f'The on_off_ratio is too large or too small; the limit is about 16')
        on_val=int(self.DVS_DIFF_FINE_VAL*on_off_ratio)
        off_val=int(self.DVS_DIFF_FINE_VAL/on_off_ratio)
        def set_dvs_bias(name):
            return self.set_bias_from_tuple(self.DVS_DEFAULT_BIASES[name])

        idiff=set_dvs_bias('diff')
        ion=self.set_bias(pyplane.Coach.BiasAddress.DVS_ON_N, pyplane.Coach.BiasType.P, self.DVS_DIFF_CB, on_val)
        ioff=self.set_bias(pyplane.Coach.BiasAddress.DVS_OFF_N,pyplane.Coach.BiasType.P, self.DVS_DIFF_CB, off_val)
        # log.info(f'Set DVS ion/idiff={(ion/idiff):.1f}, idiff/ioff={(idiff/ioff):.1f}')
        return idiff,ion,ioff
    
    def filter_dvs_events(self, coach_events_list:list) -> tuple:
        """ After a call to `request_events(t)`, `filter_dvs_events` returns the timestamps of ON and OFF events.
        
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
        """
        timestamps,addresses=self.coach_events_to_timestamps_addresses(coach_events_list)
        on_timestamps=timestamps[addresses==Coach.DVS_ON_ADDRESS]
        off_timestamps=timestamps[addresses==Coach.DVS_OFF_ADDRESS]
        n_on=len(on_timestamps)
        n_off=len(off_timestamps)
        n_tot=len(coach_events_list)
        if n_on + n_off < n_tot:
            log.warning(f' #on ({n_on}) + # off ({n_off}) = {(n_on+n_off):,} != n_tot ({n_tot}) - filtered out events')
        return np.array(on_timestamps),np.array(off_timestamps)


    def set_led_intensity(self, intensity: int) -> None:
        """
        Set the intensity of the stimulus LED to a value in the range 0 to 255.
        The LED should be plugged into the board pins next to the CoACH chip; gnd side is clearly labeled.

        This function is synchronous; it waits for success message.
        It can achieve up to about 1kHz update rate.
        
        :param intensity: the intensity 0-255 value - float values are truncated to int value
        """
        self.check_open()
        self.plane.set_led_intensity(int(intensity))

######################################################################### NOTE events

    def request_coach_output_events(self, t: float) -> None:
        """
        Starts collecting events; Enable events to be read using `read_events()`.
        Events are received for the duration specified in seconds by the argument.
        The timestamps in CoachOutputEvents are in units of 1.024 milliseconds.

        :param t: the time in seconds, max 64
        :type t: float
        """
        self.plane.request_events(t)

    def read_coach_output_events(self) -> list:
        """
        Return CoachOutputEvents read from a queue which is filled in the background once request_events() has been called. 
                See [Coach chip report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=share_link), Table 15, page 28 for event addresses.


        :return: list of `pyplane.CoachOutputEvent` events. 
            Each event is an (int,int) tuple of (address,timestamp).
                The timestamps in CoachOutputEvents are in units of 1.024 milliseconds.
        :rtype: list[pyplane.CoachOutputEvent]
        """
        events = self.plane.read_events()
        log.debug(f'read_events() got {len(events)} events')
        return events

    def capture_coach_output_events(self, t: float) -> list:
        """ Reads AER events from Coach.

        :param t: how long to wait for events in seconds
        :return: the event list
            Each event is an (int,int) tuple of (address,timestamp) but in native CoachOutputEvent form (C++ pybind object).
                    See [Coach chip report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=share_link), Table 15, page 28 for event addresses.
                The timestamps in CoachOutputEvents are in units of 1.024 milliseconds.
        """
        assert t > 0 and t < 64, 't must be greater than >0 and <=64 seconds'
        t_eps=.01 # extra time to wait to read the events
        self.check_open()
        log.debug(
            f'Starting  a request to collect events for {t}s, will block for this time')
        try:
            self.request_coach_output_events(t)
            time.sleep(t+t_eps)
            return self.read_coach_output_events()
        except Exception as e:
            log.error(f'got exception in request_events/read_events: Exception is {e}')
            raise(e)
    
    def coach_events_to_timestamps_addresses(self, es:list)->tuple:
        """ Converts list of CoachOutputEvent to tuple (`timestamp`, `addresses`).
        :param es: list of CoachOutputEvent
        :return: (timestamps,addresses)
            The timestamps are in seconds. 
            `timestamps` and `addresses` are np.ndarray 1d arrays.

        """
        log.debug(f'Number of events returned: {len(es):,}')
        # print('Timestamp\t\tAddress')
        timestamps=[]
        addresses=[]
        for e in es:
            # print(f'{e.timestamp}\t\t{e.address}')
            timestamps.append(float(e.timestamp)/1024.) # convert the int timestamp (in 1.024ms units) to seconds
            addresses.append(int(e.address))
        timestamps=np.array(timestamps)
        addresses=np.array(addresses)
        return timestamps,addresses

# NOTE follower-integrator (FOI)

    def setup_foi(self):
        """Sets up the FOI (follower-integrator)."""
        self.check_open()
        # self.setup_c2f()

        self.plane.set_bit_depth(pyplane.BitDepth(10))
        self.plane.send_coach_events(
            [
                pyplane.Coach.generate_aerc_event(
                    pyplane.Coach.CurrentOutputSelect.SelectLine0,
                    pyplane.Coach.VoltageOutputSelect.SelectLine1,
                    pyplane.Coach.VoltageInputSelect.SelectLine2,
                    pyplane.Coach.SynapseSelect.NoneSelected,
                    0,
                )
            ]
        )

        log.debug("setup FOI")

    def set_foi_vin(self, v1):
        """Sets FOI input Vin

        :param v1: volts
        """
        self.check_open()
        v = self.plane.set_voltage(pyplane.DacChannel.AIN9, v1)
        return v

    def measure_foi_vout(self):
        self.check_open()
        v = self.plane.read_voltage(pyplane.AdcChannel.AOUT10)
        return v

    def foi_compensate_vin(self, v):
        """Computes the offset compensated input voltage for the FOI

        :param v: Input voltage to calculate compensation of

        :return: The offset compensated input voltage for the FOI
        """
        _ = self.set_foi_vin(v)
        time.sleep(0.5)
        Vo = self.measure_foi_vout()
        Voff = Vo - v
        Vcorr = v - Voff

        return Vcorr

    def set_foi_ib(
        self, bias_coarse: pyplane.Coach.BiasGenMasterCurrent, fine_value: int
    ):
        """Sets the bias current of the FOI follower integrator.

        :param bias_coarse: A coarse value of current.
            allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA.
            See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
        :param fine_value: 0-255 int fine value.
            0 should not really be used since the current is badly defined.
        :return: the bias current.
        """
        self.check_open()

        wl = 3
        ib = self.set_bias(
            pyplane.Coach.BiasAddress.FOI_VB_N,
            pyplane.Coach.BiasType.N,
            bias_coarse,
            int(fine_value),
        )

        return wl * ib

    def measure_foi_waveform(self, interval: float):
        """Measure waveform response from follower integrator
        
        Input waveform must first be set using py:meth:`Coach.set_waveform()`

        :param interval: Interval of each measurement in seconds

        :return: a vector of float voltages
        """
        self.check_open()
        vout = self.plane.acquire_waveform(
            pyplane.DacChannel.AIN9, pyplane.AdcChannel.AOUT10, interval
        )

        return vout

    def set_waveform(self, wf:list):
        self.check_open()
        """ 
        Sets the waveform for driving the DAC output.
        
        :param: wf: a List of float voltages
        """
        self.plane.set_voltage_waveform(wf)


# NOTE: winner-takes-all (WTA)

    WTA_VIN_CHANNELS = [
        pyplane.DacChannel.AIN0,
        pyplane.DacChannel.AIN1,
        pyplane.DacChannel.AIN2,
        pyplane.DacChannel.AIN3,
        pyplane.DacChannel.AIN4,
        pyplane.DacChannel.AIN5,
        pyplane.DacChannel.AIN6,
        pyplane.DacChannel.AIN7,
        pyplane.DacChannel.AIN8,
        pyplane.DacChannel.AIN9,
        pyplane.DacChannel.AIN10,
        pyplane.DacChannel.AIN11,
        pyplane.DacChannel.AIN12,
        pyplane.DacChannel.AIN13,
        pyplane.DacChannel.AIN14,
        pyplane.DacChannel.AIN15
    ]

    WTA_LVOUT_CHANNELS = [
        pyplane.AdcChannel.AOUT15,
        pyplane.AdcChannel.AOUT14,
        pyplane.AdcChannel.AOUT13,
        pyplane.AdcChannel.AOUT12,
        pyplane.AdcChannel.AOUT11,
        pyplane.AdcChannel.AOUT10,
        pyplane.AdcChannel.AOUT9,
        pyplane.AdcChannel.AOUT8,
        pyplane.AdcChannel.AOUT7,
        pyplane.AdcChannel.AOUT6,
        pyplane.AdcChannel.AOUT5,
        pyplane.AdcChannel.AOUT4,
        pyplane.AdcChannel.AOUT3,
        pyplane.AdcChannel.AOUT2,
        pyplane.AdcChannel.AOUT1,
        pyplane.AdcChannel.AOUT0
    ]

    def setup_wta_iout(self):
        """Sets up the WTA (winner-takes-all) to read from Iout"""
        self.check_open()

        self.plane.send_coach_events(
            [
                pyplane.Coach.generate_aerc_event(
                    pyplane.Coach.CurrentOutputSelect.SelectLine2,
                    pyplane.Coach.VoltageOutputSelect.SelectLine0,
                    pyplane.Coach.VoltageInputSelect.SelectLine0,
                    pyplane.Coach.SynapseSelect.NoneSelected,
                    0
                )
            ]
        )
        log.debug("setup WTA to read Iout")


    def setup_wta_iall(self):
        """Sets up the WTA (winner-takes-all) to read from Iall"""
        self.check_open()

        self.plane.send_coach_events(
            [
                pyplane.Coach.generate_aerc_event(
                    pyplane.Coach.CurrentOutputSelect.SelectLine3,
                    pyplane.Coach.VoltageOutputSelect.SelectLine0,
                    pyplane.Coach.VoltageInputSelect.SelectLine0,
                    pyplane.Coach.SynapseSelect.NoneSelected,
                    0
                )
            ]
        )
        log.debug("setup WTA to read Iall")


    def set_wta_bias_fine(self, fine) -> float:
        self.check_open()
        Ib = self.set_bias(
                pyplane.Coach.BiasAddress.WTA_VB_N,
                pyplane.Coach.BiasType.N,
                pyplane.Coach.BiasGenMasterCurrent.I460pA,
                int(fine)
            )

        return 3 * Ib

    
    def set_wta_vgain(self, V):
        self.check_open()

        if (not 0 <= V <= 1.8):
            raise ValueError("V lies outside of the permitted range [0.0, 1.8]V")

        # fine for P type
        fine = int(((1.8 - V) * 255) / 1.8)
        log.info(f"fine: {fine}")

        Ib = self.set_bias(
            pyplane.Coach.BiasAddress.WTA_VGAIN_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA,
            fine
        )
        # bias current needs to be able to be as low as possible
        return Ib * 3


    def set_wta_vex(self, V):
        self.check_open()

        if (not 0 <= V <= 1.8):
            raise ValueError("V lies outside of the permitted range [0.0, 1.8]V")

        # fine for N type
        fine = int((V * 255) / 1.8)
        # log.info(f"fine: {fine}")

        Ib = self.set_bias(
            pyplane.Coach.BiasAddress.WTA_VEX_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I30nA,
            fine
        )
        return Ib * 3

    
    def set_wta_vinh(self, V):
        self.check_open()

        if (not 0 <= V <= 1.8):
            raise ValueError("V lies outside of the permitted range [0.0, 1.8]V")

        # fine for N type
        fine = int((V * 255) / 1.8)
        # log.info(f"fine: {fine}")

        Ib = self.set_bias(
            pyplane.Coach.BiasAddress.WTA_VINH_N,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I30nA,
            fine
        )
        return Ib * 3


# diff-pair integrator (DPI)


    def setup_dpi(self) -> None:
        """Sets up the DPI (diff-pair integrator)."""
        self.check_open()
        # self.setup_c2f()

        self.plane.send_coach_events(
            [
                pyplane.Coach.generate_aerc_event(
                    pyplane.Coach.CurrentOutputSelect.SelectLine5,
                    pyplane.Coach.VoltageOutputSelect.SelectLine2,
                    pyplane.Coach.VoltageInputSelect.NoneSelected,
                    pyplane.Coach.SynapseSelect.DPI,
                    0
                )
            ]
        )

        log.debug("setup DPI")

    def set_dpi_baseline(self)->None:
        ''' Sets DPI synapse baseline DPI_VTAU_P, DPI_VTHR_N, DPI_VWEIGHT_N, PEX_VTAU_N biases.'''
        self.set_bias(
            pyplane.Coach.BiasAddress.DPI_VTAU_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA,
            25
        )

        self.set_bias(
            pyplane.Coach.BiasAddress.DPI_VTHR_N,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA,
            30
        )

        self.set_bias(
            pyplane.Coach.BiasAddress.DPI_VWEIGHT_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I30nA,
            100
        )

        self.set_bias(
            pyplane.Coach.BiasAddress.PEX_VTAU_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA,
            10
        )

    def measure_dpi_vsyn(self) -> float:
        ''' Reads and returns the DPI VSyn voltage
        :return: the voltage
        '''
        self.check_open()
        v = self.plane.read_voltage(pyplane.AdcChannel.AOUT14)
        return v

    def send_dpi_pulse(self):
        ''' Sends pulse to stimulate DPI synapse'''
        self.check_open()
        self.plane.send_coach_events([pyplane.Coach.generate_pulse_event()])
        return

    class DPI_C2F:
        ''' Class to calibrate the DPI C2F converters. 
        Constructing this class calibrates the C2F converters and stores the calibration in self.fit variable.
        Then users can use the `DPI_C2F.f2i` method to convert a C2F frequency to a current
        '''
        def __init__(self, super) -> None:
            ''' Construct the instance and calibrates.
            :param super: existing Coach() instance
            :return: None
            '''
            self.coach = super

            fine_values = np.arange(1, 255, 5)
            Ib_cal = []
            c2f_calI1 = []

            self.coach.setup_ndp()

            for idx, f in enumerate(fine_values):
                cur = self.coach.set_bias(
                    pyplane.Coach.BiasAddress.NDP_VB_N,
                    pyplane.Coach.BiasType.N,
                    pyplane.Coach.BiasGenMasterCurrent.I30nA, int(f)
                )
                Ib_cal.append(cur)

                self.coach.set_ndp_v1(.6)
                self.coach.set_ndp_v2(.2)
                time.sleep(.1)
                c2f_freqs = self.coach.measure_c2f_freqs(.1)
                c2f_calI1.append(c2f_freqs[0])

            self.fit = np.polyfit(c2f_calI1, Ib_cal, 2)

            self.coach.setup_dpi()

        def f2i(self, freq):
            ''' 
            Convert a frequency in Hz to current in A
            :param freq: the C2F frequency
            :return: the current in amps
            '''
            return np.polyval(self.fit, freq)


# AHN
    def setup_ahn(self) -> None:
        """ Sets up the Axon-Hillock circuit. """
        self.check_open()
        self.disable_all_aer_event_sources()
        # select lines and neuron latches
        self.plane.send_coach_events([pyplane.Coach.generate_aerc_event(
            pyplane.Coach.CurrentOutputSelect.SelectLine6,
            pyplane.Coach.VoltageOutputSelect.SelectLine2,
            pyplane.Coach.VoltageInputSelect.NoneSelected,
            pyplane.Coach.SynapseSelect.NoneSelected, 320)])
        # enable axon-hillock neuron
        # can't set AHN reset too high or it will prevent spiking, since it will be larger than fixed input current
        self.set_bias(
            pyplane.Coach.BiasAddress.AHN_VPW_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 5)  # set a small current but large enough that it makes finite width spikes
        self.setup_r2r_buffer()
        log.info('setup AHN (axon hillock neuron)')

    def set_ahn_vpw_ib(self, coarse_current: pyplane.Coach.BiasGenMasterCurrent, fine_value: int) -> float:
        """ Set the AHN reset bias current.
        :param coarse_current: the pyplane.Coach.BiasGenMasterCurrent
        :param fine_value: the fine value, 0-255
        :return the actual programmed current in Amps
        """
        self.check_open()
        ib = self.set_bias(
            pyplane.Coach.BiasAddress.AHN_VPW_N,
            pyplane.Coach.BiasType.N,
            coarse_current, fine_value)
        return 3 * ib

    def read_ahn_vout(self) -> float:
        """ Reads and returns the AHN Vmem voltage."""
        self.check_open()
        return self.plane.read_voltage(pyplane.AdcChannel.AOUT11)

# i&f neuron

    def setup_ief(self):
        self.check_open()
        self.disable_all_aer_event_sources()

        self.set_bias(
                pyplane.Coach.BiasAddress.ACN_VLEAK_N,
                pyplane.Coach.BiasType.N,
                pyplane.Coach.BiasGenMasterCurrent.I60pA,
                2
                )

        self.set_bias(
                pyplane.Coach.BiasAddress.ACN_VGAIN_N,
                pyplane.Coach.BiasType.N,
                pyplane.Coach.BiasGenMasterCurrent.I60pA,
                6
                )

        self.set_bias(
                pyplane.Coach.BiasAddress.ACN_VDC_P,
                pyplane.Coach.BiasType.P,
                pyplane.Coach.BiasGenMasterCurrent.I30nA,
                3
                )

        self.set_bias(
                pyplane.Coach.BiasAddress.ACN_VREFR_N,
                pyplane.Coach.BiasType.N,
                pyplane.Coach.BiasGenMasterCurrent.I30nA,
                8
                )

        self.setup_r2r_buffer()

        log.info("setup I&F neuron")

    def read_i2f_transient_vout(self, time_interval=0.00025, vstep=1):
        self.check_open()
        DAC = pyplane.DacChannel.DAC1
        ADC = pyplane.AdcChannel.AOUT10
        ret = self.transient_response(DAC, ADC, time_interval, vstep)
        return ret

####################################################################### NOTE C2F

    def setup_c2f(self) -> None:
        """ Sets up the C2F biases. 
                NOTE: the correct C2F channels must be selected for any measurements to make sense.
                @see 
                For example
                ```
                    # configure wide-range TransAmp
                    self.plane.send_coach_events([pyplane.Coach.generate_aerc_event( \
                        pyplane.Coach.CurrentOutputSelect.SelectLine5, \
                        pyplane.Coach.VoltageOutputSelect.SelectLine1, \
                        pyplane.Coach.VoltageInputSelect.SelectLine2, \
                        pyplane.Coach.SynapseSelect.NoneSelected, 0)])

                ```
        """
        self.check_open()
        self.set_bias(
            pyplane.Coach.BiasAddress.C2F_HYS_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I60pA, 100)

        self.set_bias(
            pyplane.Coach.BiasAddress.C2F_BIAS_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I240nA, 255)

        self.set_bias(
            pyplane.Coach.BiasAddress.C2F_PWLK_P,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I240nA, 255)

        self.set_bias(
            pyplane.Coach.BiasAddress.C2F_REF_L,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I30nA, 255)

        self.set_bias(
            pyplane.Coach.BiasAddress.C2F_REF_H,
            pyplane.Coach.BiasType.P,
            pyplane.Coach.BiasGenMasterCurrent.I30nA, 255)

    def measure_c2f_freqs(self, duration=0.1) -> list:
        """ Measures all the C2F frequencies and returns the array of measurements.

        :param duration: how long to measure event rate for in seconds
        :return: 16 C2F frequencies in Hz
        """
        self.check_open()
        c2f_calI1_temp = self.plane.read_c2f_output(duration)
        return c2f_calI1_temp  # an array with 16 elements, the frequencies in Hz

################################################################## NOTE biasgen BG

    from enum import Enum
    BIAS_COARSE_CURRENTS = {pyplane.Coach.BiasGenMasterCurrent.I60pA: 60e-12,
                            pyplane.Coach.BiasGenMasterCurrent.I460pA: 460e-12,
                            pyplane.Coach.BiasGenMasterCurrent.I3_8nA: 3.8e-9,
                            pyplane.Coach.BiasGenMasterCurrent.I30nA: 30e-9,
                            pyplane.Coach.BiasGenMasterCurrent.I240nA: 240e-9
                            }

    # TODO below inner classes might work later with dict to map to pyplane constants so that correct arguments can be passed to pyplane function
    # class BiasCoarse(Enum):
    #     I60pA = pyplane.Coach.BiasGenMasterCurrent.I60pA
    #     I460pA = pyplane.Coach.BiasGenMasterCurrent.I460pA
    #     I3_8nA = pyplane.Coach.BiasGenMasterCurrent.I3_8nA
    #     I30nA = pyplane.Coach.BiasGenMasterCurrent.I30nA
    #     I240nA = pyplane.Coach.BiasGenMasterCurrent.I240nA

    # class BiasType(Enum):
    #     N = pyplane.Coach.BiasType.N
    #     P = pyplane.Coach.BiasType.P

    # class BiasAddress(Enum):
    #     """Defines all biases that can be set.

    #     :param Enum: choose one of them to set
    #     """
    #     BUFFER=pyplane.Coach.BiasAddress.BUFFER
    #     AHN_VPW_N=pyplane.Coach.BiasAddress.AHN_VPW_N
    #     ACN_VADPPTAU_N=pyplane.Coach.BiasAddress.ACN_VADPPTAU_N
    #     ACN_VADPWEIGHT_N=pyplane.Coach.BiasAddress.ACN_VADPWEIGHT_N
    #     ACN_VADPGAIN_N=pyplane.Coach.BiasAddress.ACN_VADPGAIN_N
    #     ACN_VADPTAU_P=pyplane.Coach.BiasAddress.ACN_VADPTAU_P
    #     ACN_VADPCASC_N=pyplane.Coach.BiasAddress.ACN_VADPCASC_N
    #     ACN_VREFR_N=pyplane.Coach.BiasAddress.ACN_VREFR_N
    #     ACN_VLEAK_N=pyplane.Coach.BiasAddress.ACN_VLEAK_N
    #     ACN_VGAIN_N=pyplane.Coach.BiasAddress.ACN_VGAIN_N
    #     ACN_VDC_P=pyplane.Coach.BiasAddress.ACN_VDC_P
    #     LDS_VTAU_P=pyplane.Coach.BiasAddress.LDS_VTAU_P
    #     LDS_VWEIGHT_P=pyplane.Coach.BiasAddress.LDS_VWEIGHT_P
    #     ATN_VADPPTAU_N=pyplane.Coach.BiasAddress.ATN_VADPPTAU_N
    #     ATN_VADPWEIGHT_N=pyplane.Coach.BiasAddress.ATN_VADPWEIGHT_N
    #     ATN_VADPGAIN_N=pyplane.Coach.BiasAddress.ATN_VADPGAIN_N
    #     ATN_VADPTAU_P=pyplane.Coach.BiasAddress.ATN_VADPTAU_P
    #     ATN_VADPCASC_N=pyplane.Coach.BiasAddress.ATN_VADPCASC_N
    #     ATN_VREFR_N=pyplane.Coach.BiasAddress.ATN_VREFR_N
    #     ATN_VCC_N=pyplane.Coach.BiasAddress.ATN_VCC_N
    #     ATN_VSPKTHR_P=pyplane.Coach.BiasAddress.ATN_VSPKTHR_P
    #     ATN_VLEAK_N=pyplane.Coach.BiasAddress.ATN_VLEAK_N
    #     ATN_VGAIN_N=pyplane.Coach.BiasAddress.ATN_VGAIN_N
    #     ATN_VDC_P=pyplane.Coach.BiasAddress.ATN_VDC_P
    #     DPI_VTAU_P=pyplane.Coach.BiasAddress.DPI_VTAU_P
    #     DPI_VWEIGHT_N=pyplane.Coach.BiasAddress.DPI_VWEIGHT_N
    #     DPI_VTHR_N=pyplane.Coach.BiasAddress.DPI_VTHR_N
    #     PEX_VTAU_N=pyplane.Coach.BiasAddress.PEX_VTAU_N
    #     ASN_VADPPTAU_N=pyplane.Coach.BiasAddress.ASN_VADPPTAU_N
    #     ASN_VADPWEIGHT_N=pyplane.Coach.BiasAddress.ASN_VADPWEIGHT_N
    #     ASN_VADPGAIN_N=pyplane.Coach.BiasAddress.ASN_VADPGAIN_N
    #     ASN_VADPTAU_P=pyplane.Coach.BiasAddress.ASN_VADPTAU_P
    #     ASN_VADPCASC_N=pyplane.Coach.BiasAddress.ASN_VADPCASC_N
    #     ASN_VCC_N=pyplane.Coach.BiasAddress.ASN_VCC_N
    #     ASN_VSPKTHR_P=pyplane.Coach.BiasAddress.ASN_VSPKTHR_P
    #     ASN_VLEAK_N=pyplane.Coach.BiasAddress.ASN_VLEAK_N
    #     ASN_VGAIN_N=pyplane.Coach.BiasAddress.ASN_VGAIN_N
    #     ASN_VDC_P=pyplane.Coach.BiasAddress.ASN_VDC_P
    #     DDI_VWEIGHT_N=pyplane.Coach.BiasAddress.DDI_VWEIGHT_N
    #     DDI_VTHR_N=pyplane.Coach.BiasAddress.DDI_VTHR_N
    #     DDI_VTAU_P=pyplane.Coach.BiasAddress.DDI_VTAU_P
    #     HHN_VBUF_N=pyplane.Coach.BiasAddress.HHN_VBUF_N
    #     HHN_VAHPSAT_N=pyplane.Coach.BiasAddress.HHN_VAHPSAT_N
    #     HHN_VCAREST2_N=pyplane.Coach.BiasAddress.HHN_VCAREST2_N
    #     HHN_VCABUF_N=pyplane.Coach.BiasAddress.HHN_VCABUF_N
    #     HHN_VCAREST_N=pyplane.Coach.BiasAddress.HHN_VCAREST_N
    #     HHN_VCAIN_P=pyplane.Coach.BiasAddress.HHN_VCAIN_P
    #     HHN_VKDSAT_N=pyplane.Coach.BiasAddress.HHN_VKDSAT_N
    #     HHN_VPUWIDTH_N=pyplane.Coach.BiasAddress.HHN_VPUWIDTH_N
    #     HHN_VKDTAU_N=pyplane.Coach.BiasAddress.HHN_VKDTAU_N
    #     HHN_VTHRES_N=pyplane.Coach.BiasAddress.HHN_VTHRES_N
    #     HHN_VNASAT_N=pyplane.Coach.BiasAddress.HHN_VNASAT_N
    #     HHN_VDC_P=pyplane.Coach.BiasAddress.HHN_VDC_P
    #     HHN_VELEAK_N=pyplane.Coach.BiasAddress.HHN_VELEAK_N
    #     HHN_VNATAU_N=pyplane.Coach.BiasAddress.HHN_VNATAU_N
    #     HHN_VGLEAK_N=pyplane.Coach.BiasAddress.HHN_VGLEAK_N
    #     HHN_VPADBIAS_N=pyplane.Coach.BiasAddress.HHN_VPADBIAS_N
    #     HHN_VPUTHRES_N=pyplane.Coach.BiasAddress.HHN_VPUTHRES_N
    #     SFP_VB_N=pyplane.Coach.BiasAddress.SFP_VB_N
    #     DVS_REFR_P=pyplane.Coach.BiasAddress.DVS_REFR_P
    #     DVS_OFF_N=pyplane.Coach.BiasAddress.DVS_OFF_N
    #     DVS_ON_N=pyplane.Coach.BiasAddress.DVS_ON_N
    #     DVS_DIFF_N=pyplane.Coach.BiasAddress.DVS_DIFF_N
    #     DVS_SF_P=pyplane.Coach.BiasAddress.DVS_SF_P
    #     DVS_CAS_N=pyplane.Coach.BiasAddress.DVS_CAS_N
    #     DVS_PR_P=pyplane.Coach.BiasAddress.DVS_PR_P
    #     RR_BIAS_P=pyplane.Coach.BiasAddress.RR_BIAS_P
    #     C2F_HYS_P=pyplane.Coach.BiasAddress.C2F_HYS_P
    #     C2F_REF_L=pyplane.Coach.BiasAddress.C2F_REF_L
    #     C2F_REF_H=pyplane.Coach.BiasAddress.C2F_REF_H
    #     C2F_BIAS_P=pyplane.Coach.BiasAddress.C2F_BIAS_P
    #     C2F_PWLK_P=pyplane.Coach.BiasAddress.C2F_PWLK_P
    #     NTA_VB_N=pyplane.Coach.BiasAddress.NTA_VB_N
    #     CSR_VT_N=pyplane.Coach.BiasAddress.CSR_VT_N
    #     BAB_VB_N=pyplane.Coach.BiasAddress.BAB_VB_N
    #     FOD_VB_N=pyplane.Coach.BiasAddress.FOD_VB_N
    #     FOI_VB_N=pyplane.Coach.BiasAddress.FOI_VB_N
    #     NDP_VB_N=pyplane.Coach.BiasAddress.NDP_VB_N
    #     NSF_VB_N=pyplane.Coach.BiasAddress.NSF_VB_N
    #     SOS_VB2_N=pyplane.Coach.BiasAddress.SOS_VB2_N
    #     PDP_VB_P=pyplane.Coach.BiasAddress.PDP_VB_P
    #     PSF_VB_P=pyplane.Coach.BiasAddress.PSF_VB_P
    #     PTA_VB_P=pyplane.Coach.BiasAddress.PTA_VB_P
    #     SOS_VB1_N=pyplane.Coach.BiasAddress.SOS_VB1_N
    #     SRE_VB1_N=pyplane.Coach.BiasAddress.SRE_VB1_N
    #     SRE_VB2_N=pyplane.Coach.BiasAddress.SRE_VB2_N
    #     WRT_VB_N=pyplane.Coach.BiasAddress.WRT_VB_N
    #     WTA_VB_N=pyplane.Coach.BiasAddress.WTA_VB_N
    #     WTA_VEX_N=pyplane.Coach.BiasAddress.WTA_VEX_N
    #     WTA_VINH_N=pyplane.Coach.BiasAddress.WTA_VINH_N
    #     WTA_VGAIN_P=pyplane.Coach.BiasAddress.WTA_VGAIN_P

    def set_bias_from_tuple(self,b):
        """ Sets a bias from tuple of (address,type,course,fine) values. See `Coach.set_bias`.
        :return: the bias current in A
        """
        return self.set_bias(b[0],b[1], b[2], b[3])

    def set_bias(self, bias_address: pyplane.Coach.BiasAddress,
                 bias_type: pyplane.Coach.BiasType,
                 coarse_current: pyplane.Coach.BiasGenMasterCurrent,
                 fine_value: int) -> float:
        """ Set a particular bias. To use this class, import the pyplane class to access its constants. E.g.
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
        :param bias_address: the particular bias, 
            one of pyplane.Coach.BiasAddress, e.g. pyplane.Coach.BiasAddress.NDP_VB_N; see [BiasAddress in coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h).
            See also Section 6.3/Table 7 of [Coach chip design report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=sharing).
        :param bias_type: the type of bias (N or P), 
            see :py:class: typically pyplane.Coach.BiasType.N or pyplane.Coach.BiasType.P see [BiasType in coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h)
        :param coarse_current: one of pyplane.Coach.BiasGenMasterCurrent, e.g. pyplane.Coach.BiasGenMasterCurrent.I30nA; 
            allowed values are I60pA, I460pA, I3_8nA, I30nA, I240nA. 
            See [coach.h](https://code.ini.uzh.ch/CoACH/CoACH_Teensy_interface/-/blob/master/src/pc/coach.h);
        :param fine_value: 0-255 int fine value. 
            0 should not really be used since the current is badly defined.

        :return: the computed actual current in Amps as COARSE_CURRENTS[coarse_current]*fine_current/255
        """
        assert isinstance(
            bias_address, pyplane.Coach.BiasAddress), f'bias_address "{bias_address}" is incorrect type, should be a pyplane.Coach.BiasAddress'
        assert isinstance(
            bias_type, pyplane.Coach.BiasType), f'bias_type "{bias_type}" should be a pyplane.Coach.BiasType'
        assert isinstance(
            coarse_current, pyplane.Coach.BiasGenMasterCurrent), f'coarse_current "{coarse_current}" should be a pyplane.Coach.BiasGenMasterCurrent'
        assert (fine_value >= 0) and (fine_value <=
                                      255), f'The fine value "{fine_value}" should be from 0-255'

        # (Tobi) actually it does seem to turn it off with this biasgen chip implementation
        # if fine_value == 0:
        #     log.warning(
        #         f'fine_value={fine_value} turns off bias current with undefined outcome')
        if isinstance(fine_value, float) and not fine_value.is_integer():
            old_fine_val = fine_value
            fine_value = int(fine_value)
            log.warning(
                f'the fine_value {old_fine_val} was truncated to {fine_value}')
        fine_value = int(fine_value)
        self.check_open()
        log.debug(f'sending coach events')
        self.plane.send_coach_events([pyplane.Coach.generate_biasgen_event(
            bias_address, bias_type, coarse_current, fine_value)])
        cur = self.BIAS_COARSE_CURRENTS[coarse_current]*fine_value/255
        log.debug(
            f'set bias {bias_address} to current {ef(cur)}A (coarse current {coarse_current} and fine value {fine_value})')
        return cur

        # pyplane.Coach.BiasAddress.NDP_VB_N, \
        # pyplane.Coach.BiasType.N, \
        # pyplane.Coach.BiasGenMasterCurrent.I30nA, fine_current)])

    def measure_waveform(self, dac_channel:pyplane.DacChannel, adc_channel:pyplane.AdcChannel , interval: float):
        """Measure voltage waveform response in response to transient voltage input.
        
        Input waveform must first be set using :py:meth:`Coach.set_waveform()`

        For channel definitions, see [Class chip documentation](https://drive.google.com/drive/folders/1VBPKVfS9zwu_I2ExR1D0jU2eCSgleoQG?usp=drive_link). 
        Each circuit schematic includes the DAC and ADC channels.

        Also, the pyplane.Coach.VoltageOutputSelect.SelectLine1 and pyplane.Coach.VoltageInputSelect 
        must be sent using get_pyplane().send_coach_events(). 
        See Tables 3 (ADC outputs) and 5 (DAC inputs) in [CoACH Chip architecture report](https://drive.google.com/file/d/1ljX2ACBuOxAENr4ZQkguyslIfM6LT5ks/view?usp=drive_link).


        :param dac_channel: channel that sets voltage.
        :param adc_channel: channel to measure.
        :param interval: Interval of each measurement in seconds.

        :return: a vector of float voltages
        """
        vout = self.plane.acquire_waveform(
            dac_channel, adc_channel, interval
        )

        return vout
    

    def transient_response(self, DAC:pyplane.DacChannel, ADC:pyplane.AdcChannel, time_interval: float, V_step: float)->list:
        """Acquire the transient response to a step function

        :param DAC: DAC channel to apply step function to
        :param ADC: ADC channel to read transient reponse from
        :param time_interval: Amount of time recorded after stimulation
        :param V_step: Voltage applied at the DAC

        NB the method just sets the provided voltage V(t=0+) and starts to measure
        immediatly. V(t=0-) is whatever is already present on the DAC.

        From the pyplane API: Acquires a number of samples from the specified AdcChannel 
        after applying a voltage step. Applies the values set using set_voltage_waveform() 
        to the DacChannel given by the first argument and records samples from the AdcChannel 
        given by the second argument at intervals given in seconds by the third argument. 
        The first sample comes from before the voltage given by the fourth argument is applied; 
        subsequent samples from subsequent time intervals. 
        The results returned are in Volts or Amps, depending on the AdcChannel chosen.
        
        :return: the list of voltages as floats
        """

        res = self.plane.acquire_transient_response(DAC, ADC, time_interval, V_step)
        return res


############################################# NOTE input utilities


# useful utilities to ask question at console terminal with default answer and timeout
def alarm_handler(signum, frame):
    raise TimeoutError


def input_with_timeout(prompt, timeout=30):
    """ get input with timeout

    :param prompt: the prompt to print
    :param timeout: timeout in seconds, or None to disable

    :returns: the input
    :raises: TimeoutError if times out
    """
    # set signal handler
    if timeout is not None:
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(timeout)  # produce SIGALRM in `timeout` seconds
    try:
        time.sleep(.5)  # get input to be printed after logging
        return input(prompt)
    except TimeoutError as to:
        raise to
    finally:
        if timeout is not None:
            signal.alarm(0)  # cancel alarm


def yes_or_no_or_always(question, default='y', timeout=None):
    """ Get Yes/No/Always answer with default choice and optional timeout

    :param question: prompt
    :param default: the default choice, i.e. 'y' or 'n' or 'a'
    :param timeout: the timeout in seconds, default is None

    :returns: 'yes' or 'no' or 'always'
    """
    if default is not None and (default != 'y' and default != 'n'):
        raise ValueError(
            f'bad option for default: {default}; must be "y" or "n")')
    yes = 'Yes' if default == 'y' else 'yes'
    no = 'No' if default == 'n' else 'no'
    always = 'always'
    while "the answer is invalid":
        try:
            to_str = '' if timeout is None or os.name == 'nt' else f'(Timeout {default} in {timeout}s)'
            if os.name == 'nt':
                log.warning('cannot use timeout signal on windows')
                time.sleep(.1)  # make the warning come out first
                reply = str(
                    input(f'{question} {to_str} ({yes}/{no}): ')).lower().strip()
            else:
                reply = str(input_with_timeout(
                    f'{question} {to_str} ({yes}/{no}/{always}): ', timeout=timeout)).lower().strip()
        except TimeoutError:
            log.warning(f'timeout expired, returning default={default} answer')
            reply = ''
        if len(reply) == 0 or reply == '':
            return yes.lower() if default == 'y' else no.lower()
        elif reply[0].lower() == 'y':
            return yes.lower()
        elif reply[0].lower() == 'n':
            return no.lower()
        elif reply[0].lower() == 'a':
            return always.lower()




timers = {}
times = {}
class Timer:
    def __init__(self, timer_name='', delay=None, show_hist=False, numpy_file=None):
        """ Make a Timer() in a _with_ statement for a block of code.
        The timer is started when the block is entered and stopped when exited.
        The Timer _must_ be used in a with statement.

        :param timer_name: the str by which this timer is repeatedly called and which it is named when summary is printed on exit
        :param delay: set this to a value to simply accumulate this externally determined interval
        :param show_hist: whether to plot a histogram with pyplot
        :param numpy_file: optional numpy file path
        """
        self.timer_name = timer_name
        self.show_hist = show_hist
        self.numpy_file = numpy_file
        self.delay=delay

        if self.timer_name not in timers.keys():
            timers[self.timer_name] = self
        if self.timer_name not in times.keys():
            times[self.timer_name]=[]

    def __enter__(self):
        if self.delay is None:
            self.start = time.time()
        return self

    def __exit__(self, *args):
        if self.delay is None:
            self.end = time.time()
            self.interval = self.end - self.start  # measured in seconds
        else:
            self.interval=self.delay
        times[self.timer_name].append(self.interval)

    def print_timing_info(self, logger=None):
        """ Prints the timing information accumulated for this Timer

        :param logger: write to the supplied logger, otherwise use the built-in logger
        """
        if len(times)==0:
            log.error(f'Timer {self.timer_name} has no statistics; was it used without a "with" statement?')
            return
        a = np.array(times[self.timer_name])
        timing_mean = np.mean(a) # todo use built in print method for timer
        timing_std = np.std(a)
        timing_median = np.median(a)
        timing_min = np.min(a)
        timing_max = np.max(a)
        s='{} n={}: {}s +/- {}s (median {}s, min {}s max {}s)'.format(self.timer_name, len(a),
                                                                      ef(timing_mean), ef(timing_std),
                                                                      ef(timing_median), ef(timing_min),
                                                                      ef(timing_max))

        if logger is not None:
            logger.info(s)
        else:
            log.info(s)

def print_timing_info():
    for k,v in times.items():  # k is the name, v is the list of times
        a = np.array(v)
        timing_mean = np.mean(a)
        timing_std = np.std(a)
        timing_median = np.median(a)
        timing_min = np.min(a)
        timing_max = np.max(a)
        log.info('== Timing statistics from all Timer ==\n{} n={}: {}s +/- {}s (median {}s, min {}s max {}s)'.format(k, len(a),
                                                                          ef(timing_mean), ef(timing_std),
                                                                          ef(timing_median), ef(timing_min),
                                                                          ef(timing_max)))
        if timers[k].numpy_file is not None:
            try:
                log.info(f'saving timing data for {k} in numpy file {timers[k].numpy_file}')
                log.info('there are {} times'.format(len(a)))
                np.save(timers[k].numpy_file, a)
            except Exception as e:
                log.error(f'could not save numpy file {timers[k].numpy_file}; caught {e}')

        if timers[k].show_hist:

            def plot_loghist(x, bins):
                hist, bins = np.histogram(x, bins=bins) # histogram x linearly
                if len(bins)<2 or bins[0]<=0:
                    log.error(f'cannot plot histogram since bins={bins}')
                    return
                logbins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins)) # use resulting bin ends to get log bins
                plt.hist(x, bins=logbins) # now again histogram x, but with the log-spaced bins, and plot this histogram
                plt.xscale('log')

            dt = np.clip(a,1e-6, None)
            # logbins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))
            try:
                plot_loghist(dt,bins=100)
                plt.xlabel('interval[ms]')
                plt.ylabel('frequency')
                plt.title(k)
                plt.show()
            except Exception as e:
                log.error(f'could not plot histogram: got {e}')
