# intended for either running from command line or testing with pytest
# pip install pytest
# Either
# from root of CoACH-labs, do "pytest"
# or use vscode testing facility to show you all these tests that you can run one by one

from ne1 import * # import Coach() class
import logging
import pyplane
from deprecated import deprecated
import pytest
import time
from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm, trange
from engineering_notation import EngNumber as ef # format numbers in engineering format quickly, e.g. ef(2e-9)='2n'


@pytest.mark.serial  #https://github.com/pytest-dev/pytest-xdist/issues/84
def test_coach_singleton():
    """ Tests to make sure Coach() is really a singleton"""
    coach=Coach(logging_level=logging.DEBUG) 
    coach.open()
    coach=Coach(logging_level=logging.DEBUG) 
    coach.open()
    coach.close()



@pytest.mark.serial  #https://github.com/pytest-dev/pytest-xdist/issues/84
def test_open_close():
    coach=Coach(logging_level=logging.DEBUG) # NOTE change to INFO to reduce clutter - create a Coach object called p; you will use it to talk to class chip, change to logging.DEBUG for troubleshooting
    coach.open()
    coach.close()

@pytest.mark.serial
def test_dac_and_current_adc():
    coach=Coach(logging_level=logging.DEBUG)
    # c.find_coach()
    coach.open()
    coach.close()

    coach.open()
    coach.setup_nfet()
    coach.set_nfet_vs(0)
    coach.set_nfet_vd(1)
    for vgn in np.linspace(.4,.6,10):
        vgn_set=coach.set_nfet_vg(vgn) # set gate voltage and get the quantized value
        idn=coach.measure_nfet_id() # measure drain current
        isn=coach.measure_nfet_is() # measure source current
        print(f'vgn={ef(vgn_set)}V: idn={ef(idn)}A isn={ef(isn)}A')
    coach.close() # release hooks, probably not needed

@pytest.mark.serial
def test_nta():
    from ne1 import Coach
    import pyplane
    import logging

    coach=Coach(logging_level=logging.DEBUG)
    # c.find_coach()
    # c.open()
    coach.setup_nta()
    print(type(pyplane.Coach.BiasAddress.NTA_VB_N))
    coach.set_bias(pyplane.Coach.BiasAddress.NDP_VB_N,
            pyplane.Coach.BiasType.N,
            pyplane.Coach.BiasGenMasterCurrent.I30nA,
            30)
    coach.set_nta_v1(.8)
    coach.set_nta_v2(.8)
    coach.measure_nta_vout()

def autoclose_plot(t_show_plot=30):
    print(f'automatically closing plot in {t_show_plot}s...')
    plt.pause(t_show_plot)
    plt.close()


def test_repeat_request_read_event_reduce_dvs_threshold(request):
    """ Tests multiple calls to get events"""
    ratio=3                      # the initial value of Ion/Idiff and Idiff/Ioff 
    ratio_decrease_factor=.9       # by what factor to decrease it each iteration
    t_capture_total_s=1            # total capture time
    n_max=1000000                   # max number of events per capture_coach_output_events to try to avoid bombing python machine
    t_settle=3                      # time in seconds after changing threshold
    led_intensity=5                 # in case the cover is off and we have LED
    print(f'Testing repeated captures from DVS with decreasing threshold values starting from {ratio} and decreasing by powers of {ratio_decrease_factor} until we capture {n_max} events')
    c=Coach(logging_level=logging.INFO)
    c.open()
    c.reset_soft()
    c.set_led_intensity(led_intensity)
    # c.set_debug(True) # uncomment to see detailed communication logging in pyplane
    ipr,isf,icas,idiff,ion,ioff,irefr=c.setup_dvs(on_off_ratio=ratio)

    # c.get_pyplane().debug=True      # effect not clear, not documented
    n_captured=0

    ratios=[]
    events_hz=[]
    done=False
    while not done:
        print(f'setting up DVS with on/off threshold ratio {ratio:.2f}')
        idiff,ion,ioff=c.set_dvs_threshold_biases(on_off_ratio=ratio)
        time.sleep(t_settle)
        n_captured=0
        ev=c.capture_coach_output_events(t_capture_total_s)
        n_captured=len(ev)
        timestamps, addresses=c.coach_events_to_timestamps_addresses(ev)
        on_ts,off_ts=c.filter_dvs_events(ev)
        if n_captured>n_max:
            print(f'**** terminating after capturing {n_captured:,} events which is larger than {n_max:,} limit')
            break
        hz=n_captured/t_capture_total_s
        events_hz.append(hz)
        print(f'ratios ion/idiff {(ion/idiff):.2f} idiff/ioff {(idiff/ioff):.2f}: captured {n_captured:,} events at rate {ef(hz)}Hz')
        if len(timestamps>=2):
            print(f'timestamp first={timestamps[0]} last={timestamps[-1]}, duration={timestamps[-1]-timestamps[0]}')
            plt.plot(np.arange(0,len(on_ts)), on_ts,'x')
            plt.plot(np.arange(0,len(off_ts)),off_ts,'o')
            plt.legend(['ON','OFF'])
            plt.xlabel('event [#]')
            plt.ylabel('ts [s]')
            plt.pause(10)
            plt.cla()
        ratios.append(ion/idiff)
        ratio=np.power(ratio,ratio_decrease_factor)
    print(f'****** ended run after capturing {n_captured:,} events which is larger than n_max={n_max:,} limit')
    print('done capturing, plotting data. ********** CLOSE PLOT TO TERMINATE TEST **************** ')
    plt.plot(ratios,events_hz,'o-')
    plt.xlabel('ratio (actual quantized) $I_{on}/I_{diff}$')
    plt.ylabel('event rate (Hz)')
    plt.title(f'********** CLOSE PLOT TO TERMINATE TEST *********** \n{request.node.name} ')
    autoclose_plot()


@pytest.mark.serial
def test_dvs_turn_off_pr_use_sf_input(request):
    """ 
    Modulates the SF bias to generate events, biases DVS to really hold its output constant.
    This test does not work because each bias change produces a huge storm of events even when there is
    no change in bias current.
    """
    coach=Coach(logging_level=logging.DEBUG)
    try:
        coach.open()
        coach.setup_dvs()
        # override default PR biases
        
        # turn off cascode bias to force PR output high
        coach.set_bias(pyplane.Coach.BiasAddress.DVS_CAS_N,pyplane.Coach.BiasType.N,pyplane.Coach.BiasGenMasterCurrent.I60pA,00)
        print('turned off cascode bias, sleeping for 1s to settle output')
        time.sleep(1)
        
        t=8
        dt=0.1 # max update rate is about 20Hz, so take 10Hz
        ts=np.arange(0,t,dt)
        cycles=2
        prb_dc=128.
        prb_ac=100.
        contrast=float(prb_dc+prb_ac)/float(prb_dc-prb_ac)
        log.info(f'Isf contrast is max/min={ef(contrast)} which is ln contast={ef(np.log(contrast))} e-folds')
        fine_values=prb_dc+prb_ac*np.sin(cycles*2*np.pi*ts/t)
        coach.set_bias(pyplane.Coach.BiasAddress.DVS_SF_P,pyplane.Coach.BiasType.P,pyplane.Coach.BiasGenMasterCurrent.I30nA,int(prb_dc))
        # coach.request_events(1) # flush events
        # time.sleep(1)
        # es=coach.read_events(1) # finish flushing events, stop collecting events
        coach.request_coach_output_events(t) # now start AER again and collect for t seconds
        for fine_value in tqdm(fine_values,mininterval=5):
            coach.set_bias(pyplane.Coach.BiasAddress.DVS_SF_P,pyplane.Coach.BiasType.P,pyplane.Coach.BiasGenMasterCurrent.I30nA,int(fine_value))
            time.sleep(dt)
        es=coach.read_coach_output_events() # read collected events
        # assert len(es)>0, 'Coach did not return any events'
        if (n:=len(es))==0: 
            print('Coach did not return any events')
            return
        
        print(f'Coach returned {n} events')
        timestamps,addresses=coach.coach_events_to_timestamps_addresses(es)
        
        on_ts,off_ts=coach.filter_dvs_events(es)
        on_vals=+1*np.ones_like(on_ts)
        off_vals=-1*np.ones_like(off_ts)

        plt.subplot(2,1,1)
        plt.plot(ts,fine_values,'x-')
        plt.xlabel('time (s)')
        plt.ylabel('I_sf fine value')
        plt.ylim(bottom=0) # show absolute values to see contrast
        plt.title('****** Close plot to continue tests **********')

        plt.subplot(2,1,2)
        
        plt.plot(timestamps,addresses,'kx',on_ts,on_vals,'go', off_ts,off_vals,'ro')
        plt.xlabel('time (s)')
        plt.ylabel('addresses and ON/OFF events')
        plt.legend(['address','ON','OFF'])

        plt.title(f'********** CLOSE PLOT TO TERMINATE TEST *********** \n{request.node.name} ')
        print(f'********** CLOSE PLOT TO TERMINATE TEST ***********')

        autoclose_plot()

    finally:
        coach.close()



@pytest.mark.serial
def test_dvs_led_wiggle():
    """ Modulates the set SF but don't wiggle, see if it makes events"""
    led_dc=128.
    led_ac=120.
    use_square=True # set True to use square wave, False for sine
    t_total=3
    t_settle=10
    led_freq=10
    dt=0.002 # max LED update rate is about 1kHz
    on_off_ratio=2.1
    
    def predicted_dvs_event_threshold(on_off_ratio:float)->float:
        kappa=.8
        A=(22*22)/(5*5)
        predicated_threshold=(1/(A*kappa))*np.log(on_off_ratio)
        return predicated_threshold

    contrast=float(led_dc+led_ac)/float(led_dc-led_ac)
    ln_contrast=np.log(contrast)
    print(f'LED contrast is max/min={ef(contrast)} which is ln contrast={ef(ln_contrast)} e-folds')
    theta=predicted_dvs_event_threshold(on_off_ratio=on_off_ratio)
    predicted_num_events=ln_contrast/theta
    print(f'Using on_off_ratio={on_off_ratio:.3f}, predicted DVS threshold theta={theta:.2f} efolds/event so we predict {predicted_num_events:.1f} events per edge')

    coach=Coach(logging_level=logging.INFO)
    coach.open()
    coach.reset_soft()
    coach.setup_dvs(on_off_ratio=on_off_ratio)
    coach.set_led_intensity(led_dc)
    print(f'settling for {t_settle}s')
    for i in trange(t_settle):
        time.sleep(1)
    t_range=np.arange(0,t_total,dt)
    # ev_start=coach.capture_coach_output_events(.1) # clear out any initial events, handshake with circuits with pending events
    # print(f'cleared out {len(ev_start)} events')

    if not use_square:
        led_values=led_dc+led_ac*np.sin(2*np.pi*led_freq*t_range) # sine wave
    else:
        from scipy.signal import square as square
        led_values=led_dc+led_ac*square(2*np.pi*led_freq*t_range) # square wave
    
    led_values=led_values.astype(int)
    # es=p.capture_events(t) # max is 64 (64k ms)
    # coach.set_bias(pyplane.Coach.BiasAddress.DVS_SF_P,pyplane.Coach.BiasType.P,pyplane.Coach.BiasGenMasterCurrent.I30nA,int(prb_dc))
    # time.sleep(1)
    on_ts=np.empty(0)
    off_ts=np.empty(0)
    print(f'starting capture for {t_total}s')
    coach.request_coach_output_events(t_total)
    for t,led_val in zip(t_range,led_values):
        coach.set_led_intensity(led_val)
        time.sleep(dt)
    print('done')
    ev=coach.read_coach_output_events()
    print(f'got {len(ev)} events')
    timestamps, addresses=coach.coach_events_to_timestamps_addresses(ev)
    on_ts,off_ts=coach.filter_dvs_events(ev)
    on_vals=+1*np.ones_like(on_ts)
    off_vals=-1*np.ones_like(off_ts)
    
    print('you must be running X server to see the plot')
    plt.subplot(2,1,1)
    plt.step(t_range,led_values,'-')
    plt.xlabel('time (s)')
    plt.ylabel('LED value')
    plt.ylim(bottom=0) # show absolute values to see contrast
    plt.title('**** Close plot to continue *****')
    plt.subplot(2,1,2)
    
    plt.plot(timestamps,addresses,'kx',on_ts,on_vals,'go', off_ts,off_vals,'ro')
    plt.xlabel('time (s)')
    plt.ylabel('addresses and ON/OFF events')
    plt.legend(['address','ON','OFF'])
    plt.title('DVS pixel events')
    autoclose_plot(30)


@pytest.mark.serial
def test_led():
    """ Tests PCB LED for stimulating DVS. Plug any LED into the LED jumper next to the board. The Gnd side is clearly labeled. """
    coach=Coach(logging_level=logging.INFO)
    print('ramp LED up and down')
    for j in tqdm(range(10),unit='cycle'):
        for i in range(0,255,10):
            coach.set_led_intensity(i)
            time.sleep(.01)
        for i in range(255,0,-5):
            coach.set_led_intensity(i)
            time.sleep(.01)
    coach.set_led_intensity(0)
    print('flash as fast as possible')
    t_flash=5
    t_start=time.time()
    while time.time()-t_start<t_flash:
        with Timer('LED ON/OFF') as timer:
            coach.set_led_intensity(255)
            coach.set_led_intensity(0)
    timer.print_timing_info()

   
@pytest.mark.serial
def test_dvs_bias_loading_but_no_change(request):
    """ Reloads the same SF bias to generate coupling events"""
    coach=Coach(logging_level=logging.INFO)
    try:
        coach.open()
        coach.setup_dvs()
        t=16
        dt=0.1 # max update rate is about 20Hz, so take 10Hz
        ts=np.arange(0,t,dt)
        cycles=2
        prb_dc=128.
        prb_ac=0.
        contrast=float(prb_dc+prb_ac)/float(prb_dc-prb_ac)
        log.info(f'Isf contrast is max/min={ef(contrast)} which is ln contast={ef(np.log(contrast))} e-folds')
        fine_values=prb_dc+prb_ac*np.sin(cycles*2*np.pi*ts/t)
        # es=p.capture_events(t) # max is 64 (64k ms)
        coach.request_coach_output_events(t)
        coach.set_bias(pyplane.Coach.BiasAddress.DVS_SF_P,pyplane.Coach.BiasType.P,pyplane.Coach.BiasGenMasterCurrent.I30nA,int(prb_dc))
        time.sleep(1)
        for fine_value in tqdm(fine_values,mininterval=5):
            coach.set_bias(pyplane.Coach.BiasAddress.DVS_SF_P,pyplane.Coach.BiasType.P,pyplane.Coach.BiasGenMasterCurrent.I30nA,int(fine_value))
            time.sleep(dt)
        es=coach.read_coach_output_events()
        assert len(es)>0, 'Coach did not return any events'
        timestamps,addresses=coach.coach_events_to_timestamps_addresses(es)
        
        on_ts,off_ts=coach.filter_dvs_events(es)
        on_vals=+1*np.ones_like(on_ts)
        off_vals=-1*np.ones_like(off_ts)

        plt.subplot(2,1,1)
        plt.title(f'********** CLOSE PLOT TO TERMINATE TEST *********** \n{request.node.name} ')
        plt.plot(ts,fine_values,'x-')
        plt.xlabel('time (s)')
        plt.ylabel('I_sf fine value')
        plt.ylim(bottom=0) # show absolute values to see contrast
        plt.subplot(2,1,2)
        
        plt.plot(timestamps,addresses,'kx',on_ts,on_vals,'go', off_ts,off_vals,'ro')
        plt.xlabel('time (s)')
        plt.ylabel('addresses and ON/OFF events')
        plt.legend(['address','ON','OFF'])
        print(f'********** CLOSE PLOT TO TERMINATE TEST ***********')

        autoclose_plot()

    finally:
        coach.close()

@pytest.mark.serial
def test_setup_dvs():
    coach=Coach()
    coach.setup_dvs()
    coach.close()

@pytest.mark.serial
def test_ahn(): # axon hillock test
    ### NOTE you must be running a DISPLAY (e.g. Xserver) for the pyplot window to show
    ## you must close the window to continue test
    coach=Coach(logging_level=logging.DEBUG)
    try:
        coach.open()
        coach.reset_soft()
        coach.disable_all_aer_event_sources()
        coach.setup_ahn()
        t=8
        dt=.01
        # es=p.capture_events(5) # max is 64 (64k ms) # should make about 2-3 spikes
        coach.request_coach_output_events(t)
        ts=np.arange(0,t,dt)
        vin_dummy=np.zeros_like(ts)
        coach.set_waveform(vin_dummy)
        vms=coach.measure_waveform(pyplane.DacChannel.DAC1, pyplane.AdcChannel.AOUT11,dt)  # TODO should use a waveform measurement call that measures waveform on device for accurate timing
        # vms=[]
        # for t in tqdm(ts):
        #     vms.append(coach.read_ahn_vout())
        #     time.sleep(dt)
        vms=np.array(vms)
        es=coach.read_coach_output_events()
        timestamps, addresses = coach.coach_events_to_timestamps_addresses(es)
        plt.subplot(2,1,1)
        plt.plot(ts,vms)
        plt.xlabel('time (s)')
        plt.ylabel('Vmem (V)')
        plt.xlim([0,ts[-1]])
        plt. title('Close this window to continue')
        plt.subplot(2,1,2)
        plt.plot(timestamps,addresses,'x')
        plt.xlabel('time (s)')
        plt.ylabel('address')
        plt.xlim([0,ts[-1]])
        autoclose_plot()
        assert len(es)>0, 'AHN (axon hillock) did not return any events'
    finally:
        coach.close()



def test_plt():
    ### NOTE you must be running a DISPLAY (e.g. Xserver) for the pyplot window to show
    # and you must close the plot for test to continue
    from matplotlib import pyplot as plt
    import numpy as np
    x=np.linspace(0,1,100)
    y=x
    plt.plot(x,y)
    plt. title('Close this window to terminate test')
    autoclose_plot()

if __name__=='__main__':
    test_open_close()