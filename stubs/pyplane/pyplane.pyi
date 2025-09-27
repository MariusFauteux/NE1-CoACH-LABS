"""
Interface to CoACH class-chip via Teensy based PLANE (Platform for Learning About Neuromorphic Engineering).
"""
from __future__ import annotations
import pybind11_stubgen.typing_ext
import typing
__all__ = ['AdcChannel', 'BitDepth', 'Coach', 'CoachInputEvent', 'CoachOutputEvent', 'CurrentRange', 'DacChannel', 'Plane', 'ResetType', 'TeensyStatus', 'get_version']
class AdcChannel:
    """
    Members:
    
      AOUT0
    
      AOUT1
    
      AOUT2
    
      AOUT3
    
      AOUT4
    
      AOUT5
    
      AOUT6
    
      AOUT7
    
      AOUT8
    
      AOUT9
    
      AOUT10
    
      AOUT11
    
      AOUT12
    
      AOUT13
    
      AOUT14
    
      AOUT15
    
      GO0_P
    
      GO0_N
    
      GO2_P
    
      GO2_N
    
      GO23
    
      GO22
    
      GO5
    
      GO3
    
      NCVDD1
    
      PLUG
    
      NCVDD3
    
      NCVDD2
    
      NCVDD5
    
      NCVDD4
    
      GO21_N
    
      GO20_N
    """
    AOUT0: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT0: 0>
    AOUT1: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT1: 1>
    AOUT10: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT10: 10>
    AOUT11: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT11: 11>
    AOUT12: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT12: 12>
    AOUT13: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT13: 13>
    AOUT14: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT14: 14>
    AOUT15: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT15: 15>
    AOUT2: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT2: 2>
    AOUT3: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT3: 3>
    AOUT4: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT4: 4>
    AOUT5: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT5: 5>
    AOUT6: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT6: 6>
    AOUT7: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT7: 7>
    AOUT8: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT8: 8>
    AOUT9: typing.ClassVar[AdcChannel]  # value = <AdcChannel.AOUT9: 9>
    GO0_N: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO0_N: 17>
    GO0_P: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO0_P: 16>
    GO20_N: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO20_N: 31>
    GO21_N: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO21_N: 30>
    GO22: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO22: 21>
    GO23: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO23: 20>
    GO2_N: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO2_N: 19>
    GO2_P: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO2_P: 18>
    GO3: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO3: 23>
    GO5: typing.ClassVar[AdcChannel]  # value = <AdcChannel.GO5: 22>
    NCVDD1: typing.ClassVar[AdcChannel]  # value = <AdcChannel.NCVDD1: 24>
    NCVDD2: typing.ClassVar[AdcChannel]  # value = <AdcChannel.NCVDD2: 27>
    NCVDD3: typing.ClassVar[AdcChannel]  # value = <AdcChannel.NCVDD3: 26>
    NCVDD4: typing.ClassVar[AdcChannel]  # value = <AdcChannel.NCVDD4: 29>
    NCVDD5: typing.ClassVar[AdcChannel]  # value = <AdcChannel.NCVDD5: 28>
    PLUG: typing.ClassVar[AdcChannel]  # value = <AdcChannel.PLUG: 25>
    __members__: typing.ClassVar[dict[str, AdcChannel]]  # value = {'AOUT0': <AdcChannel.AOUT0: 0>, 'AOUT1': <AdcChannel.AOUT1: 1>, 'AOUT2': <AdcChannel.AOUT2: 2>, 'AOUT3': <AdcChannel.AOUT3: 3>, 'AOUT4': <AdcChannel.AOUT4: 4>, 'AOUT5': <AdcChannel.AOUT5: 5>, 'AOUT6': <AdcChannel.AOUT6: 6>, 'AOUT7': <AdcChannel.AOUT7: 7>, 'AOUT8': <AdcChannel.AOUT8: 8>, 'AOUT9': <AdcChannel.AOUT9: 9>, 'AOUT10': <AdcChannel.AOUT10: 10>, 'AOUT11': <AdcChannel.AOUT11: 11>, 'AOUT12': <AdcChannel.AOUT12: 12>, 'AOUT13': <AdcChannel.AOUT13: 13>, 'AOUT14': <AdcChannel.AOUT14: 14>, 'AOUT15': <AdcChannel.AOUT15: 15>, 'GO0_P': <AdcChannel.GO0_P: 16>, 'GO0_N': <AdcChannel.GO0_N: 17>, 'GO2_P': <AdcChannel.GO2_P: 18>, 'GO2_N': <AdcChannel.GO2_N: 19>, 'GO23': <AdcChannel.GO23: 20>, 'GO22': <AdcChannel.GO22: 21>, 'GO5': <AdcChannel.GO5: 22>, 'GO3': <AdcChannel.GO3: 23>, 'NCVDD1': <AdcChannel.NCVDD1: 24>, 'PLUG': <AdcChannel.PLUG: 25>, 'NCVDD3': <AdcChannel.NCVDD3: 26>, 'NCVDD2': <AdcChannel.NCVDD2: 27>, 'NCVDD5': <AdcChannel.NCVDD5: 28>, 'NCVDD4': <AdcChannel.NCVDD4: 29>, 'GO21_N': <AdcChannel.GO21_N: 30>, 'GO20_N': <AdcChannel.GO20_N: 31>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BitDepth:
    """
    Members:
    
      BitDepth10
    
      BitDepth12
    """
    BitDepth10: typing.ClassVar[BitDepth]  # value = <BitDepth.BitDepth10: 10>
    BitDepth12: typing.ClassVar[BitDepth]  # value = <BitDepth.BitDepth12: 12>
    __members__: typing.ClassVar[dict[str, BitDepth]]  # value = {'BitDepth10': <BitDepth.BitDepth10: 10>, 'BitDepth12': <BitDepth.BitDepth12: 12>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Coach:
    class BiasAddress:
        """
        Members:
        
          BUFFER
        
          AHN_VPW_N
        
          ACN_VADPPTAU_N
        
          ACN_VADPWEIGHT_N
        
          ACN_VADPGAIN_N
        
          ACN_VADPTAU_P
        
          ACN_VADPCASC_N
        
          ACN_VREFR_N
        
          ACN_VLEAK_N
        
          ACN_VGAIN_N
        
          ACN_VDC_P
        
          LDS_VTAU_P
        
          LDS_VWEIGHT_P
        
          ATN_VADPPTAU_N
        
          ATN_VADPWEIGHT_N
        
          ATN_VADPGAIN_N
        
          ATN_VADPTAU_P
        
          ATN_VADPCASC_N
        
          ATN_VREFR_N
        
          ATN_VCC_N
        
          ATN_VSPKTHR_P
        
          ATN_VLEAK_N
        
          ATN_VGAIN_N
        
          ATN_VDC_P
        
          DPI_VTAU_P
        
          DPI_VWEIGHT_N
        
          DPI_VTHR_N
        
          PEX_VTAU_N
        
          ASN_VADPPTAU_N
        
          ASN_VADPWEIGHT_N
        
          ASN_VADPGAIN_N
        
          ASN_VADPTAU_P
        
          ASN_VADPCASC_N
        
          ASN_VCC_N
        
          ASN_VSPKTHR_P
        
          ASN_VLEAK_N
        
          ASN_VGAIN_N
        
          ASN_VDC_P
        
          DDI_VWEIGHT_N
        
          DDI_VTHR_N
        
          DDI_VTAU_P
        
          HHN_VBUF_N
        
          HHN_VAHPSAT_N
        
          HHN_VCAREST2_N
        
          HHN_VCABUF_N
        
          HHN_VCAREST_N
        
          HHN_VCAIN_P
        
          HHN_VKDSAT_N
        
          HHN_VPUWIDTH_N
        
          HHN_VKDTAU_N
        
          HHN_VTHRES_N
        
          HHN_VNASAT_N
        
          HHN_VDC_P
        
          HHN_VELEAK_N
        
          HHN_VNATAU_N
        
          HHN_VGLEAK_N
        
          HHN_VPADBIAS_N
        
          HHN_VPUTHRES_N
        
          SFP_VB_N
        
          DVS_REFR_P
        
          DVS_OFF_N
        
          DVS_ON_N
        
          DVS_DIFF_N
        
          DVS_SF_P
        
          DVS_CAS_N
        
          DVS_PR_P
        
          RR_BIAS_P
        
          C2F_HYS_P
        
          C2F_REF_L
        
          C2F_REF_H
        
          C2F_BIAS_P
        
          C2F_PWLK_P
        
          NTA_VB_N
        
          CSR_VT_N
        
          BAB_VB_N
        
          FOD_VB_N
        
          FOI_VB_N
        
          NDP_VB_N
        
          NSF_VB_N
        
          SOS_VB2_N
        
          PDP_VB_P
        
          PSF_VB_P
        
          PTA_VB_P
        
          SOS_VB1_N
        
          SRE_VB1_N
        
          SRE_VB2_N
        
          WRT_VB_N
        
          WTA_VB_N
        
          WTA_VEX_N
        
          WTA_VINH_N
        
          WTA_VGAIN_P
        """
        ACN_VADPCASC_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VADPCASC_N: 6>
        ACN_VADPGAIN_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VADPGAIN_N: 4>
        ACN_VADPPTAU_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VADPPTAU_N: 2>
        ACN_VADPTAU_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VADPTAU_P: 5>
        ACN_VADPWEIGHT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VADPWEIGHT_N: 3>
        ACN_VDC_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VDC_P: 10>
        ACN_VGAIN_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VGAIN_N: 9>
        ACN_VLEAK_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VLEAK_N: 8>
        ACN_VREFR_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ACN_VREFR_N: 7>
        AHN_VPW_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.AHN_VPW_N: 1>
        ASN_VADPCASC_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VADPCASC_N: 32>
        ASN_VADPGAIN_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VADPGAIN_N: 30>
        ASN_VADPPTAU_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VADPPTAU_N: 28>
        ASN_VADPTAU_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VADPTAU_P: 31>
        ASN_VADPWEIGHT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VADPWEIGHT_N: 29>
        ASN_VCC_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VCC_N: 33>
        ASN_VDC_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VDC_P: 37>
        ASN_VGAIN_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VGAIN_N: 36>
        ASN_VLEAK_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VLEAK_N: 35>
        ASN_VSPKTHR_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ASN_VSPKTHR_P: 34>
        ATN_VADPCASC_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VADPCASC_N: 17>
        ATN_VADPGAIN_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VADPGAIN_N: 15>
        ATN_VADPPTAU_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VADPPTAU_N: 13>
        ATN_VADPTAU_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VADPTAU_P: 16>
        ATN_VADPWEIGHT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VADPWEIGHT_N: 14>
        ATN_VCC_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VCC_N: 19>
        ATN_VDC_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VDC_P: 23>
        ATN_VGAIN_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VGAIN_N: 22>
        ATN_VLEAK_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VLEAK_N: 21>
        ATN_VREFR_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VREFR_N: 18>
        ATN_VSPKTHR_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.ATN_VSPKTHR_P: 20>
        BAB_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.BAB_VB_N: 111>
        BUFFER: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.BUFFER: 0>
        C2F_BIAS_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.C2F_BIAS_P: 107>
        C2F_HYS_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.C2F_HYS_P: 104>
        C2F_PWLK_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.C2F_PWLK_P: 108>
        C2F_REF_H: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.C2F_REF_H: 106>
        C2F_REF_L: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.C2F_REF_L: 105>
        CSR_VT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.CSR_VT_N: 110>
        DDI_VTAU_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DDI_VTAU_P: 40>
        DDI_VTHR_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DDI_VTHR_N: 39>
        DDI_VWEIGHT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DDI_VWEIGHT_N: 38>
        DPI_VTAU_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DPI_VTAU_P: 24>
        DPI_VTHR_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DPI_VTHR_N: 26>
        DPI_VWEIGHT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DPI_VWEIGHT_N: 25>
        DVS_CAS_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DVS_CAS_N: 101>
        DVS_DIFF_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DVS_DIFF_N: 99>
        DVS_OFF_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DVS_OFF_N: 97>
        DVS_ON_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DVS_ON_N: 98>
        DVS_PR_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DVS_PR_P: 102>
        DVS_REFR_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DVS_REFR_P: 96>
        DVS_SF_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.DVS_SF_P: 100>
        FOD_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.FOD_VB_N: 112>
        FOI_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.FOI_VB_N: 113>
        HHN_VAHPSAT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VAHPSAT_N: 42>
        HHN_VBUF_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VBUF_N: 41>
        HHN_VCABUF_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VCABUF_N: 44>
        HHN_VCAIN_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VCAIN_P: 46>
        HHN_VCAREST2_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VCAREST2_N: 43>
        HHN_VCAREST_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VCAREST_N: 45>
        HHN_VDC_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VDC_P: 52>
        HHN_VELEAK_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VELEAK_N: 53>
        HHN_VGLEAK_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VGLEAK_N: 55>
        HHN_VKDSAT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VKDSAT_N: 47>
        HHN_VKDTAU_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VKDTAU_N: 49>
        HHN_VNASAT_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VNASAT_N: 51>
        HHN_VNATAU_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VNATAU_N: 54>
        HHN_VPADBIAS_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VPADBIAS_N: 56>
        HHN_VPUTHRES_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VPUTHRES_N: 57>
        HHN_VPUWIDTH_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VPUWIDTH_N: 48>
        HHN_VTHRES_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.HHN_VTHRES_N: 50>
        LDS_VTAU_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.LDS_VTAU_P: 11>
        LDS_VWEIGHT_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.LDS_VWEIGHT_P: 12>
        NDP_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.NDP_VB_N: 114>
        NSF_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.NSF_VB_N: 115>
        NTA_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.NTA_VB_N: 109>
        PDP_VB_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.PDP_VB_P: 117>
        PEX_VTAU_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.PEX_VTAU_N: 27>
        PSF_VB_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.PSF_VB_P: 118>
        PTA_VB_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.PTA_VB_P: 119>
        RR_BIAS_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.RR_BIAS_P: 103>
        SFP_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.SFP_VB_N: 95>
        SOS_VB1_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.SOS_VB1_N: 120>
        SOS_VB2_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.SOS_VB2_N: 116>
        SRE_VB1_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.SRE_VB1_N: 121>
        SRE_VB2_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.SRE_VB2_N: 122>
        WRT_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.WRT_VB_N: 123>
        WTA_VB_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.WTA_VB_N: 124>
        WTA_VEX_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.WTA_VEX_N: 125>
        WTA_VGAIN_P: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.WTA_VGAIN_P: 127>
        WTA_VINH_N: typing.ClassVar[Coach.BiasAddress]  # value = <BiasAddress.WTA_VINH_N: 126>
        __members__: typing.ClassVar[dict[str, Coach.BiasAddress]]  # value = {'BUFFER': <BiasAddress.BUFFER: 0>, 'AHN_VPW_N': <BiasAddress.AHN_VPW_N: 1>, 'ACN_VADPPTAU_N': <BiasAddress.ACN_VADPPTAU_N: 2>, 'ACN_VADPWEIGHT_N': <BiasAddress.ACN_VADPWEIGHT_N: 3>, 'ACN_VADPGAIN_N': <BiasAddress.ACN_VADPGAIN_N: 4>, 'ACN_VADPTAU_P': <BiasAddress.ACN_VADPTAU_P: 5>, 'ACN_VADPCASC_N': <BiasAddress.ACN_VADPCASC_N: 6>, 'ACN_VREFR_N': <BiasAddress.ACN_VREFR_N: 7>, 'ACN_VLEAK_N': <BiasAddress.ACN_VLEAK_N: 8>, 'ACN_VGAIN_N': <BiasAddress.ACN_VGAIN_N: 9>, 'ACN_VDC_P': <BiasAddress.ACN_VDC_P: 10>, 'LDS_VTAU_P': <BiasAddress.LDS_VTAU_P: 11>, 'LDS_VWEIGHT_P': <BiasAddress.LDS_VWEIGHT_P: 12>, 'ATN_VADPPTAU_N': <BiasAddress.ATN_VADPPTAU_N: 13>, 'ATN_VADPWEIGHT_N': <BiasAddress.ATN_VADPWEIGHT_N: 14>, 'ATN_VADPGAIN_N': <BiasAddress.ATN_VADPGAIN_N: 15>, 'ATN_VADPTAU_P': <BiasAddress.ATN_VADPTAU_P: 16>, 'ATN_VADPCASC_N': <BiasAddress.ATN_VADPCASC_N: 17>, 'ATN_VREFR_N': <BiasAddress.ATN_VREFR_N: 18>, 'ATN_VCC_N': <BiasAddress.ATN_VCC_N: 19>, 'ATN_VSPKTHR_P': <BiasAddress.ATN_VSPKTHR_P: 20>, 'ATN_VLEAK_N': <BiasAddress.ATN_VLEAK_N: 21>, 'ATN_VGAIN_N': <BiasAddress.ATN_VGAIN_N: 22>, 'ATN_VDC_P': <BiasAddress.ATN_VDC_P: 23>, 'DPI_VTAU_P': <BiasAddress.DPI_VTAU_P: 24>, 'DPI_VWEIGHT_N': <BiasAddress.DPI_VWEIGHT_N: 25>, 'DPI_VTHR_N': <BiasAddress.DPI_VTHR_N: 26>, 'PEX_VTAU_N': <BiasAddress.PEX_VTAU_N: 27>, 'ASN_VADPPTAU_N': <BiasAddress.ASN_VADPPTAU_N: 28>, 'ASN_VADPWEIGHT_N': <BiasAddress.ASN_VADPWEIGHT_N: 29>, 'ASN_VADPGAIN_N': <BiasAddress.ASN_VADPGAIN_N: 30>, 'ASN_VADPTAU_P': <BiasAddress.ASN_VADPTAU_P: 31>, 'ASN_VADPCASC_N': <BiasAddress.ASN_VADPCASC_N: 32>, 'ASN_VCC_N': <BiasAddress.ASN_VCC_N: 33>, 'ASN_VSPKTHR_P': <BiasAddress.ASN_VSPKTHR_P: 34>, 'ASN_VLEAK_N': <BiasAddress.ASN_VLEAK_N: 35>, 'ASN_VGAIN_N': <BiasAddress.ASN_VGAIN_N: 36>, 'ASN_VDC_P': <BiasAddress.ASN_VDC_P: 37>, 'DDI_VWEIGHT_N': <BiasAddress.DDI_VWEIGHT_N: 38>, 'DDI_VTHR_N': <BiasAddress.DDI_VTHR_N: 39>, 'DDI_VTAU_P': <BiasAddress.DDI_VTAU_P: 40>, 'HHN_VBUF_N': <BiasAddress.HHN_VBUF_N: 41>, 'HHN_VAHPSAT_N': <BiasAddress.HHN_VAHPSAT_N: 42>, 'HHN_VCAREST2_N': <BiasAddress.HHN_VCAREST2_N: 43>, 'HHN_VCABUF_N': <BiasAddress.HHN_VCABUF_N: 44>, 'HHN_VCAREST_N': <BiasAddress.HHN_VCAREST_N: 45>, 'HHN_VCAIN_P': <BiasAddress.HHN_VCAIN_P: 46>, 'HHN_VKDSAT_N': <BiasAddress.HHN_VKDSAT_N: 47>, 'HHN_VPUWIDTH_N': <BiasAddress.HHN_VPUWIDTH_N: 48>, 'HHN_VKDTAU_N': <BiasAddress.HHN_VKDTAU_N: 49>, 'HHN_VTHRES_N': <BiasAddress.HHN_VTHRES_N: 50>, 'HHN_VNASAT_N': <BiasAddress.HHN_VNASAT_N: 51>, 'HHN_VDC_P': <BiasAddress.HHN_VDC_P: 52>, 'HHN_VELEAK_N': <BiasAddress.HHN_VELEAK_N: 53>, 'HHN_VNATAU_N': <BiasAddress.HHN_VNATAU_N: 54>, 'HHN_VGLEAK_N': <BiasAddress.HHN_VGLEAK_N: 55>, 'HHN_VPADBIAS_N': <BiasAddress.HHN_VPADBIAS_N: 56>, 'HHN_VPUTHRES_N': <BiasAddress.HHN_VPUTHRES_N: 57>, 'SFP_VB_N': <BiasAddress.SFP_VB_N: 95>, 'DVS_REFR_P': <BiasAddress.DVS_REFR_P: 96>, 'DVS_OFF_N': <BiasAddress.DVS_OFF_N: 97>, 'DVS_ON_N': <BiasAddress.DVS_ON_N: 98>, 'DVS_DIFF_N': <BiasAddress.DVS_DIFF_N: 99>, 'DVS_SF_P': <BiasAddress.DVS_SF_P: 100>, 'DVS_CAS_N': <BiasAddress.DVS_CAS_N: 101>, 'DVS_PR_P': <BiasAddress.DVS_PR_P: 102>, 'RR_BIAS_P': <BiasAddress.RR_BIAS_P: 103>, 'C2F_HYS_P': <BiasAddress.C2F_HYS_P: 104>, 'C2F_REF_L': <BiasAddress.C2F_REF_L: 105>, 'C2F_REF_H': <BiasAddress.C2F_REF_H: 106>, 'C2F_BIAS_P': <BiasAddress.C2F_BIAS_P: 107>, 'C2F_PWLK_P': <BiasAddress.C2F_PWLK_P: 108>, 'NTA_VB_N': <BiasAddress.NTA_VB_N: 109>, 'CSR_VT_N': <BiasAddress.CSR_VT_N: 110>, 'BAB_VB_N': <BiasAddress.BAB_VB_N: 111>, 'FOD_VB_N': <BiasAddress.FOD_VB_N: 112>, 'FOI_VB_N': <BiasAddress.FOI_VB_N: 113>, 'NDP_VB_N': <BiasAddress.NDP_VB_N: 114>, 'NSF_VB_N': <BiasAddress.NSF_VB_N: 115>, 'SOS_VB2_N': <BiasAddress.SOS_VB2_N: 116>, 'PDP_VB_P': <BiasAddress.PDP_VB_P: 117>, 'PSF_VB_P': <BiasAddress.PSF_VB_P: 118>, 'PTA_VB_P': <BiasAddress.PTA_VB_P: 119>, 'SOS_VB1_N': <BiasAddress.SOS_VB1_N: 120>, 'SRE_VB1_N': <BiasAddress.SRE_VB1_N: 121>, 'SRE_VB2_N': <BiasAddress.SRE_VB2_N: 122>, 'WRT_VB_N': <BiasAddress.WRT_VB_N: 123>, 'WTA_VB_N': <BiasAddress.WTA_VB_N: 124>, 'WTA_VEX_N': <BiasAddress.WTA_VEX_N: 125>, 'WTA_VINH_N': <BiasAddress.WTA_VINH_N: 126>, 'WTA_VGAIN_P': <BiasAddress.WTA_VGAIN_P: 127>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class BiasGenMasterCurrent:
        """
        Members:
        
          I60pA
        
          I460pA
        
          I3_8nA
        
          I30nA
        
          I240nA
        """
        I240nA: typing.ClassVar[Coach.BiasGenMasterCurrent]  # value = <BiasGenMasterCurrent.I240nA: 2048>
        I30nA: typing.ClassVar[Coach.BiasGenMasterCurrent]  # value = <BiasGenMasterCurrent.I30nA: 1536>
        I3_8nA: typing.ClassVar[Coach.BiasGenMasterCurrent]  # value = <BiasGenMasterCurrent.I3_8nA: 1024>
        I460pA: typing.ClassVar[Coach.BiasGenMasterCurrent]  # value = <BiasGenMasterCurrent.I460pA: 512>
        I60pA: typing.ClassVar[Coach.BiasGenMasterCurrent]  # value = <BiasGenMasterCurrent.I60pA: 0>
        __members__: typing.ClassVar[dict[str, Coach.BiasGenMasterCurrent]]  # value = {'I60pA': <BiasGenMasterCurrent.I60pA: 0>, 'I460pA': <BiasGenMasterCurrent.I460pA: 512>, 'I3_8nA': <BiasGenMasterCurrent.I3_8nA: 1024>, 'I30nA': <BiasGenMasterCurrent.I30nA: 1536>, 'I240nA': <BiasGenMasterCurrent.I240nA: 2048>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class BiasType:
        """
        Members:
        
          P
        
          N
        """
        N: typing.ClassVar[Coach.BiasType]  # value = <BiasType.N: 1>
        P: typing.ClassVar[Coach.BiasType]  # value = <BiasType.P: 0>
        __members__: typing.ClassVar[dict[str, Coach.BiasType]]  # value = {'P': <BiasType.P: 0>, 'N': <BiasType.N: 1>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class CurrentOutputSelect:
        """
        Members:
        
          SelectLine0
        
          SelectLine1
        
          SelectLine2
        
          SelectLine3
        
          SelectLine4
        
          SelectLine5
        
          SelectLine6
        """
        SelectLine0: typing.ClassVar[Coach.CurrentOutputSelect]  # value = <CurrentOutputSelect.SelectLine0: 0>
        SelectLine1: typing.ClassVar[Coach.CurrentOutputSelect]  # value = <CurrentOutputSelect.SelectLine1: 8192>
        SelectLine2: typing.ClassVar[Coach.CurrentOutputSelect]  # value = <CurrentOutputSelect.SelectLine2: 16384>
        SelectLine3: typing.ClassVar[Coach.CurrentOutputSelect]  # value = <CurrentOutputSelect.SelectLine3: 24576>
        SelectLine4: typing.ClassVar[Coach.CurrentOutputSelect]  # value = <CurrentOutputSelect.SelectLine4: 32768>
        SelectLine5: typing.ClassVar[Coach.CurrentOutputSelect]  # value = <CurrentOutputSelect.SelectLine5: 40960>
        SelectLine6: typing.ClassVar[Coach.CurrentOutputSelect]  # value = <CurrentOutputSelect.SelectLine6: 49152>
        __members__: typing.ClassVar[dict[str, Coach.CurrentOutputSelect]]  # value = {'SelectLine0': <CurrentOutputSelect.SelectLine0: 0>, 'SelectLine1': <CurrentOutputSelect.SelectLine1: 8192>, 'SelectLine2': <CurrentOutputSelect.SelectLine2: 16384>, 'SelectLine3': <CurrentOutputSelect.SelectLine3: 24576>, 'SelectLine4': <CurrentOutputSelect.SelectLine4: 32768>, 'SelectLine5': <CurrentOutputSelect.SelectLine5: 40960>, 'SelectLine6': <CurrentOutputSelect.SelectLine6: 49152>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class SynapseSelect:
        """
        Members:
        
          NoneSelected
        
          LDS
        
          DPI
        
          DDI
        """
        DDI: typing.ClassVar[Coach.SynapseSelect]  # value = <SynapseSelect.DDI: 12>
        DPI: typing.ClassVar[Coach.SynapseSelect]  # value = <SynapseSelect.DPI: 4>
        LDS: typing.ClassVar[Coach.SynapseSelect]  # value = <SynapseSelect.LDS: 8>
        NoneSelected: typing.ClassVar[Coach.SynapseSelect]  # value = <SynapseSelect.NoneSelected: 0>
        __members__: typing.ClassVar[dict[str, Coach.SynapseSelect]]  # value = {'NoneSelected': <SynapseSelect.NoneSelected: 0>, 'LDS': <SynapseSelect.LDS: 8>, 'DPI': <SynapseSelect.DPI: 4>, 'DDI': <SynapseSelect.DDI: 12>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class VoltageInputSelect:
        """
        Members:
        
          NoneSelected
        
          SelectLine0
        
          SelectLine1
        
          SelectLine2
        """
        NoneSelected: typing.ClassVar[Coach.VoltageInputSelect]  # value = <VoltageInputSelect.NoneSelected: 0>
        SelectLine0: typing.ClassVar[Coach.VoltageInputSelect]  # value = <VoltageInputSelect.SelectLine0: 512>
        SelectLine1: typing.ClassVar[Coach.VoltageInputSelect]  # value = <VoltageInputSelect.SelectLine1: 1024>
        SelectLine2: typing.ClassVar[Coach.VoltageInputSelect]  # value = <VoltageInputSelect.SelectLine2: 1536>
        __members__: typing.ClassVar[dict[str, Coach.VoltageInputSelect]]  # value = {'NoneSelected': <VoltageInputSelect.NoneSelected: 0>, 'SelectLine0': <VoltageInputSelect.SelectLine0: 512>, 'SelectLine1': <VoltageInputSelect.SelectLine1: 1024>, 'SelectLine2': <VoltageInputSelect.SelectLine2: 1536>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class VoltageOutputSelect:
        """
        Members:
        
          NoneSelected
        
          SelectLine0
        
          SelectLine1
        
          SelectLine2
        """
        NoneSelected: typing.ClassVar[Coach.VoltageOutputSelect]  # value = <VoltageOutputSelect.NoneSelected: 0>
        SelectLine0: typing.ClassVar[Coach.VoltageOutputSelect]  # value = <VoltageOutputSelect.SelectLine0: 4096>
        SelectLine1: typing.ClassVar[Coach.VoltageOutputSelect]  # value = <VoltageOutputSelect.SelectLine1: 2048>
        SelectLine2: typing.ClassVar[Coach.VoltageOutputSelect]  # value = <VoltageOutputSelect.SelectLine2: 6144>
        __members__: typing.ClassVar[dict[str, Coach.VoltageOutputSelect]]  # value = {'NoneSelected': <VoltageOutputSelect.NoneSelected: 0>, 'SelectLine0': <VoltageOutputSelect.SelectLine0: 4096>, 'SelectLine1': <VoltageOutputSelect.SelectLine1: 2048>, 'SelectLine2': <VoltageOutputSelect.SelectLine2: 6144>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    ACN_ADPEN_ASI: typing.ClassVar[int] = 16
    ACN_DCEN_ASBI: typing.ClassVar[int] = 32
    ASN_DCEN_ASBI: typing.ClassVar[int] = 256
    ATN_ADPEN_ASI: typing.ClassVar[int] = 128
    ATN_DCEN_ASBI: typing.ClassVar[int] = 64
    SRE_VEN_VSI: typing.ClassVar[int] = 1
    WTA_VHEN_SI: typing.ClassVar[int] = 2
    @staticmethod
    def generate_pulse_event() -> CoachInputEvent:
        """
        Generate a pulse event suitable for passing to send_coach_event().
        """
    def generate_aerc_event(self, arg0: Coach.VoltageOutputSelect, arg1: Coach.VoltageInputSelect, arg2: Coach.SynapseSelect, arg3: int) -> CoachInputEvent:
        """
        Generate an AER control event suitable for passing to send_coach_event().
        """
    def generate_biasgen_event(self, arg0: Coach.BiasType, arg1: Coach.BiasGenMasterCurrent, arg2: int) -> CoachInputEvent:
        """
        Generate a biasgen event suitable for passing to send_coach_event().
        """
class CoachInputEvent:
    def __init__(self, arg0: int) -> None:
        ...
    @property
    def event(self) -> int:
        ...
class CoachOutputEvent:
    address: int
    timestamp: int
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    def as_tuple(self) -> tuple[int, int]:
        ...
class CurrentRange:
    """
    Members:
    
      High
    
      Low
    """
    High: typing.ClassVar[CurrentRange]  # value = <CurrentRange.High: 0>
    Low: typing.ClassVar[CurrentRange]  # value = <CurrentRange.Low: 4096>
    __members__: typing.ClassVar[dict[str, CurrentRange]]  # value = {'High': <CurrentRange.High: 0>, 'Low': <CurrentRange.Low: 4096>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DacChannel:
    """
    Members:
    
      AIN0
    
      AIN1
    
      AIN2
    
      AIN3
    
      AIN4
    
      AIN5
    
      AIN6
    
      AIN7
    
      AIN8
    
      AIN9
    
      AIN10
    
      AIN11
    
      AIN12
    
      AIN13
    
      AIN14
    
      AIN15
    
      GO23
    
      GO22
    
      GO5
    
      GO3
    
      GO2
    
      GO4
    
      GO1
    
      GO0
    
      DAC1
    
      DAC2
    
      DAC3
    
      DAC4
    
      PLUG
    
      GO21
    
      GO20
    
      TP
    """
    AIN0: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN0: 0>
    AIN1: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN1: 1>
    AIN10: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN10: 10>
    AIN11: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN11: 11>
    AIN12: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN12: 12>
    AIN13: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN13: 13>
    AIN14: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN14: 14>
    AIN15: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN15: 15>
    AIN2: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN2: 2>
    AIN3: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN3: 3>
    AIN4: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN4: 4>
    AIN5: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN5: 5>
    AIN6: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN6: 6>
    AIN7: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN7: 7>
    AIN8: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN8: 8>
    AIN9: typing.ClassVar[DacChannel]  # value = <DacChannel.AIN9: 9>
    DAC1: typing.ClassVar[DacChannel]  # value = <DacChannel.DAC1: 24>
    DAC2: typing.ClassVar[DacChannel]  # value = <DacChannel.DAC2: 25>
    DAC3: typing.ClassVar[DacChannel]  # value = <DacChannel.DAC3: 26>
    DAC4: typing.ClassVar[DacChannel]  # value = <DacChannel.DAC4: 27>
    GO0: typing.ClassVar[DacChannel]  # value = <DacChannel.GO0: 23>
    GO1: typing.ClassVar[DacChannel]  # value = <DacChannel.GO1: 22>
    GO2: typing.ClassVar[DacChannel]  # value = <DacChannel.GO2: 20>
    GO20: typing.ClassVar[DacChannel]  # value = <DacChannel.GO20: 30>
    GO21: typing.ClassVar[DacChannel]  # value = <DacChannel.GO21: 29>
    GO22: typing.ClassVar[DacChannel]  # value = <DacChannel.GO22: 17>
    GO23: typing.ClassVar[DacChannel]  # value = <DacChannel.GO23: 16>
    GO3: typing.ClassVar[DacChannel]  # value = <DacChannel.GO3: 19>
    GO4: typing.ClassVar[DacChannel]  # value = <DacChannel.GO4: 21>
    GO5: typing.ClassVar[DacChannel]  # value = <DacChannel.GO5: 18>
    PLUG: typing.ClassVar[DacChannel]  # value = <DacChannel.PLUG: 28>
    TP: typing.ClassVar[DacChannel]  # value = <DacChannel.TP: 31>
    __members__: typing.ClassVar[dict[str, DacChannel]]  # value = {'AIN0': <DacChannel.AIN0: 0>, 'AIN1': <DacChannel.AIN1: 1>, 'AIN2': <DacChannel.AIN2: 2>, 'AIN3': <DacChannel.AIN3: 3>, 'AIN4': <DacChannel.AIN4: 4>, 'AIN5': <DacChannel.AIN5: 5>, 'AIN6': <DacChannel.AIN6: 6>, 'AIN7': <DacChannel.AIN7: 7>, 'AIN8': <DacChannel.AIN8: 8>, 'AIN9': <DacChannel.AIN9: 9>, 'AIN10': <DacChannel.AIN10: 10>, 'AIN11': <DacChannel.AIN11: 11>, 'AIN12': <DacChannel.AIN12: 12>, 'AIN13': <DacChannel.AIN13: 13>, 'AIN14': <DacChannel.AIN14: 14>, 'AIN15': <DacChannel.AIN15: 15>, 'GO23': <DacChannel.GO23: 16>, 'GO22': <DacChannel.GO22: 17>, 'GO5': <DacChannel.GO5: 18>, 'GO3': <DacChannel.GO3: 19>, 'GO2': <DacChannel.GO2: 20>, 'GO4': <DacChannel.GO4: 21>, 'GO1': <DacChannel.GO1: 22>, 'GO0': <DacChannel.GO0: 23>, 'DAC1': <DacChannel.DAC1: 24>, 'DAC2': <DacChannel.DAC2: 25>, 'DAC3': <DacChannel.DAC3: 26>, 'DAC4': <DacChannel.DAC4: 27>, 'PLUG': <DacChannel.PLUG: 28>, 'GO21': <DacChannel.GO21: 29>, 'GO20': <DacChannel.GO20: 30>, 'TP': <DacChannel.TP: 31>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Plane:
    max_settable_voltage_V: typing.ClassVar[float] = 1.7999999523162842
    min_acquire_transient_response_interval_10bit_s: typing.ClassVar[float] = 6.000000212225132e-06
    min_acquire_transient_response_interval_12bit_s: typing.ClassVar[float] = 2.2000000171829015e-05
    min_acquire_waveform_interval_10bit_s: typing.ClassVar[float] = 8.199999865610152e-05
    min_acquire_waveform_interval_12bit_s: typing.ClassVar[float] = 9.7999996796716e-05
    teensy_ref_voltage_V: typing.ClassVar[float] = 3.312999963760376
    debug: bool
    def __init__(self) -> None:
        ...
    def acquire_transient_response(self, arg0: DacChannel, arg1: AdcChannel, arg2: float, arg3: float) -> list[float]:
        """
        Acquires a number of samples from the specified AdcChannel after applying a voltage step.
        Applies the values set using set_voltage_waveform() to the DacChannel given by the first argument and records samples from the AdcChannel given by the second argument at intervals given in seconds by the third argument.
        The first sample comes from before the voltage given by the fourth argument is applied; subsequent samples from subsequent time intervals.
        The results returned are in Volts or Amps, depending on the AdcChannel chosen.
        """
    def acquire_waveform(self, arg0: DacChannel, arg1: AdcChannel, arg2: float) -> list[float]:
        """
        Acquires a number of samples from the specified AdcChannel.
        Applies the values set using set_voltage_waveform() to the DacChannel given by the first argument and records samples from the AdcChannel given by the second argument at intervals given in seconds by the third argument.
        The results returned are in Volts or Amps, depending on the AdcChannel chosen.
        """
    def get_bit_depth(self) -> BitDepth:
        """
        Returns the value set by set_bit_depth(). Does not read from the board.
        """
    def get_device_name(self) -> str:
        """
        Return the name of the device that was opened.
        """
    def get_firmware_version(self) -> tuple[int, int, int]:
        """
        Return a three-element tuple comprising major, minor, and patch version of the Teensy firmware, or (-1, -1, -1) if the version cannot be ascertained.
        """
    def get_led_intensity(self) -> int:
        """
        Returns what was set using set_led_intensity(). Does not read from the board.
        """
    def get_max_current(self, arg0: AdcChannel) -> float:
        """
        Returns the maximum current, in Amps, that can be set for the given AdcChannel.
        """
    def get_set_current(self, arg0: AdcChannel) -> float:
        """
        Returns what was written using set_current(). Does not read from the board.
        """
    def get_set_voltage(self, arg0: DacChannel) -> float:
        """
        Returns what was written using set_voltage(). Does not read from the board.
        """
    def get_teensy_sn(self) -> int:
        """
        Return the Teensy's serial number.
        """
    def get_voltage_waveform(self) -> list[float]:
        """
        Returns the waveform written using set_voltage_waveform(). Does not read from the board.
        """
    def open(self, arg0: str) -> None:
        """
        Open communication with the Teensy on the PLANE board via the named device, on Linux typically /dev/ttyACM0.
        Calling open twice is a no-op if the same device is requested, and an error if a different device is requested.
        Errors in open() are reported by throwing a RuntimeError.
        """
    def read_c2f_output(self, arg0: float) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        Read all of the C2F values over a duration specified in seconds by the argument.
        """
    def read_current(self, arg0: AdcChannel) -> float:
        """
        Read one particular current AdcChannel. The return value is in Amps.
        """
    def read_events(self) -> list[CoachOutputEvent]:
        """
        Return CoachOutputEvents read from a queue which is filled in the background once request_events() has been called.
        The timestamps in CoachOutputEvents are in units of 1.024 milliseconds.
        """
    def read_voltage(self, arg0: AdcChannel) -> float:
        """
        Read one particular voltage AdcChannel. The return value is in Volts.
        """
    def request_events(self, arg0: float) -> None:
        """
        Starts collecting events; Enable events to be read using read_events().
        Events are received for the duration specified in seconds by the argument.
        The timestamps in CoachOutputEvents are in units of 1.024 milliseconds.

        :param arg0: the time in seconds, max 64
        
        :return: list of CoachOutputEvent
        """
    def reset(self, arg0: ResetType) -> TeensyStatus:
        """
        Resets the (Teensy,) CoACH chip, DACs and current sensors (and blinks the LEDs).
        If ResetType.Soft is specified, the Teensy is not reset. If ResetType.Hard is specified, the Teensy is reset. This takes several seconds to execute.
        Returns a TeensyStatus which can be Success, HardResetFailed, or, on v0.3 boards, HardResetNotSupported.
        """
    def send_coach_events(self, arg0: list[CoachInputEvent]) -> None:
        """
        Send a list of CoachInputEvent prepared by one of the Coach.generate_*_event() functions to the CoACH chip.
        """
    def set_bit_depth(self, arg0: BitDepth) -> None:
        """
        Set number of bits used for ADC conversions.
        Can be BitDepth.BitDepth10 or BitDepth.BitDepth12 (default).
        """
    def set_current(self, arg0: AdcChannel, arg1: DacChannel, arg2: float) -> float:
        """
        Set the current, given in Amps, on the given AdcChannel.
        The valid range depends on the channel, and for GO23, GO22, GO21_N and GO20_N on the state of the switches. Even within this range, it may not be possible to set the requested current, in which case a RuntimeError exception will be thrown. Callers should be prepared to catch such exceptions.
        Returns the current, in Amps, that was set.
        """
    def set_led_intensity(self, arg0: int) -> None:
        """
        Set the intensity of the stimulus LED to a value in the range 0 to 255.
        """
    def set_voltage(self, arg0: DacChannel, arg1: float) -> float:
        """
        Set the voltage, given in Volts, on the given DacChannel. The maximum is given by max_settable_voltage_V.
        Returns the voltage, in Volts, that was set.
        """
    def set_voltage_waveform(self, arg0: list[float]) -> None:
        """
        Sets the waveform to apply in request_readings() and acquire_transient_response() by specifying a list of voltages, given in Volts.
        """
class ResetType:
    """
    Members:
    
      Soft
    
      Hard
    """
    Hard: typing.ClassVar[ResetType]  # value = <ResetType.Hard: 1>
    Soft: typing.ClassVar[ResetType]  # value = <ResetType.Soft: 0>
    __members__: typing.ClassVar[dict[str, ResetType]]  # value = {'Soft': <ResetType.Soft: 0>, 'Hard': <ResetType.Hard: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TeensyStatus:
    """
    Members:
    
      Success
    
      HardResetFailed
    
      IncorrectCurrentSwitchRange
    
      CurrentCannotBeSet
    
      CurrentOutsideSearchRange
    
      UnknownCommand
    
      AerHandshakeFailed
    
      HardResetImminent
    
      HardResetNotSupported
    
      InvalidBitDepth
    """
    AerHandshakeFailed: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.AerHandshakeFailed: 6>
    CurrentCannotBeSet: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.CurrentCannotBeSet: 3>
    CurrentOutsideSearchRange: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.CurrentOutsideSearchRange: 4>
    HardResetFailed: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.HardResetFailed: 1>
    HardResetImminent: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.HardResetImminent: 7>
    HardResetNotSupported: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.HardResetNotSupported: 8>
    IncorrectCurrentSwitchRange: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.IncorrectCurrentSwitchRange: 2>
    InvalidBitDepth: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.InvalidBitDepth: 9>
    Success: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.Success: 0>
    UnknownCommand: typing.ClassVar[TeensyStatus]  # value = <TeensyStatus.UnknownCommand: 5>
    __members__: typing.ClassVar[dict[str, TeensyStatus]]  # value = {'Success': <TeensyStatus.Success: 0>, 'HardResetFailed': <TeensyStatus.HardResetFailed: 1>, 'IncorrectCurrentSwitchRange': <TeensyStatus.IncorrectCurrentSwitchRange: 2>, 'CurrentCannotBeSet': <TeensyStatus.CurrentCannotBeSet: 3>, 'CurrentOutsideSearchRange': <TeensyStatus.CurrentOutsideSearchRange: 4>, 'UnknownCommand': <TeensyStatus.UnknownCommand: 5>, 'AerHandshakeFailed': <TeensyStatus.AerHandshakeFailed: 6>, 'HardResetImminent': <TeensyStatus.HardResetImminent: 7>, 'HardResetNotSupported': <TeensyStatus.HardResetNotSupported: 8>, 'InvalidBitDepth': <TeensyStatus.InvalidBitDepth: 9>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
def get_version() -> tuple[int, int, int]:
    ...
