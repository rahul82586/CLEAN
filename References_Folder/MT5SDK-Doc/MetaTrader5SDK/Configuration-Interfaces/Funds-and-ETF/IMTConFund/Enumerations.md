[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / Enumerations

[Previous](../IMTConFund.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConFund](../IMTConFund.md) class contains the following enumerations:

  * [IMTConFund::EnFlags (#enflags)](Enumerations.md#enflags)
  * [IMTConFund::EnType (#entype)](Enumerations.md#entype)
  * [IMTConFund::EnRecalculation (#enrecalculation)](Enumerations.md#enrecalculation)
  * [IMTConFund::EnFeeMode (#enfeemode)](Enumerations.md#enfeemode)
  * [IMTConFund::EnFeePeriod (#enfeeperiod)](Enumerations.md#enfeeperiod)
  * [IMTConFund::EnFeeAssests (#enfeeassests)](Enumerations.md#enfeeassests)
  * [IMTConFund::EnFeeSuccessCalc (#enfeesuccesscalc)](Enumerations.md#enfeesuccesscalc)
  * [IMTConFund::EnFeeSuccessModes (#enfeesuccessmodes)](Enumerations.md#enfeesuccessmodes)
  * [IMTConFund::EnFeeSuccessHWMType (#enfeesuccesshwmtype)](Enumerations.md#enfeesuccesshwmtype)



<a id="enflags"></a>
## IMTConFund::EnFlags (#enflags)

IMTConFund::EnFlags provides a list of additional fund properties.

ID | Value | Description  
FLAG_NONE | 0x00000000 | No flags.  
FLAG_ENABLED | 0x00000001 | Configuration enabled.  
FLAG_ALL |  | End of enumeration. It corresponds to enabling of all flags.  
  
The enumeration is used in the [IMTConFund::Flags](Flags.md) method.

<a id="entype"></a>
## IMTConFund::EnType (#entype)

Fund types are enumerated in IMTConFund::EnType.

ID | Value | Description  
TYPE_OPEN_END | 0 | Open-end fund.  
TYPE_CLOSED_END | 1 | Closed-end fund.  
TYPE_FIRST |  | Beginning of enumeration. Corresponds to TYPE_OPEN_END.  
TYPE_LAST |  | End of enumeration. Corresponds to TYPE_CLOSED_END.  
  
The enumeration is used in the [IMTConFund::Type](Type.md) method.

<a id="enrecalculation"></a>
## IMTConFund::EnRecalculation (#enrecalculation)

IMTConFund::EnRecalculation provides a list of fund chart recalculation modes.

ID | Value | Description  
RECALCULATION_MINUTELY | 0 | Every minute.  
RECALCULATION_HOURLY | 1 | Every hour.  
RECALCULATION_DAILY | 2 | Every day.  
RECALCULATION_MANUAL | 3 | Manual.  
RECALCULATION_FIRST |  | Beginning of enumeration. Corresponds to RECALCULATION_MINUTELY.  
RECALCULATION_LAST |  | End of enumeration. Corresponds to RECALCULATION_MANUAL.  
  
The enumeration is used in the [IMTConFund::Recalculation](Recalculation.md) method.

<a id="enfeemode"></a>
## IMTConFund::EnFeeMode (#enfeemode)

IMTConFund::EnFeeMode provides a list of fund management and success fee calculation modes.

ID | Value | Description  
FEE_MODE_AUTOMATIC | 0 | Automatic, calculated by the platform.  
FEE_MODE_REPORT | 1 | Manual, based on external data.  
FEE_MODE_FIRST |  | Beginning of enumeration. Corresponds to FEE_MODE_AUTOMATIC.  
FEE_MODE_LAST |  | End of enumeration. Corresponds to FEE_MODE_REPORT.  
  
The enumeration is used in the [IMTConFund::FeeMode](FeeMode.md) method.

<a id="enfeeperiod"></a>
## IMTConFund::EnFeePeriod (#enfeeperiod)

IMTConFund::EnFeePeriod provides a list of fund management and success fee calculation periods.

ID | Value | Description  
FEE_PERIOD_DAILY | 0 | Daily.  
FEE_PERIOD_MONTHLY | 1 | Monthly.  
FEE_PERIOD_QUARTERLY | 2 | Quarterly.  
FEE_PERIOD_ANNUAL | 3 | Annually.  
FEE_PERIOD_FIRST |  | Beginning of enumeration. Corresponds to FEE_PERIOD_DAILY.  
FEE_PERIOD_LAST |  | End of enumeration. Corresponds to FEE_PERIOD_ANNUAL.  
  
The enumeration is used in the [IMTConFund::FeePeriod](FeePeriod.md) method.

<a id="enfeeassests"></a>
## IMTConFund::EnFeeAssests (#enfeeassests)

IMTConFund::EnFeeAssests provides a list of fund management fee calculation modes.

ID | Value | Description  
FEE_ASSETS_END | 0 | Use the asset value as of the end of the period.  
FEE_ASSETS_BEGIN | 1 | Use the asset value as of the beginning of the period.  
FEE_ASSETS_AVERAGE | 2 | Use the average asset value over the period.  
FEE_PERIOD_FIRST |  | Beginning of enumeration. Corresponds to FEE_ASSETS_END.  
FEE_PERIOD_LAST |  | End of enumeration. Corresponds to FEE_ASSETS_END.  
  
The enumeration is used in [IMTConFund::FeeManagementAssets](FeeManagementAssets.md) method.

<a id="enfeesuccesscalc"></a>
## IMTConFund::EnFeeSuccessCalc (#enfeesuccesscalc)

IMTConFund::EnFeeSuccessCalc provides a list of success fee calculation modes.

ID | Value | Description  
FEE_SUCCESS_CALC_HURDLE_HWM_SOFT | 0 | Calculate based on the total returns for the period.  
FEE_SUCCESS_CALC_HURDLE_HWM_HARD | 1 | Calculate based on the returns above the hurdle rate.  
FEE_SUCCESS_CALC_FIRST |  | Beginning of enumeration. Corresponds to FEE_SUCCESS_CALC_HURDLE_HWM_SOFT.  
FEE_SUCCESS_CALC_LAST |  | End of enumeration. Corresponds to FEE_SUCCESS_CALC_HURDLE_HWM_HARD.  
  
The enumeration is used in the [IMTConFund::FeeSuccessCalc](FeeSuccessCalc.md) method.

<a id="enfeesuccessmodes"></a>
## IMTConFund::EnFeeSuccessModes (#enfeesuccessmodes)

IMTConFund::EnFeeSuccessModes provides a list of success fee calculation modes.

ID | Value | Description  
FEE_SUCCESS_MODE_BEFORE_MF | 0 | Before management fee calculation.  
FEE_SUCCESS_MODE_AFTER_MF | 1 | After management fee calculation.  
FEE_SUCCESS_CALC_FIRST |  | Beginning of enumeration. Corresponds to FEE_SUCCESS_CALC_HURDLE_HWM_SOFT.  
FEE_SUCCESS_CALC_LAST |  | End of enumeration. Corresponds to FEE_SUCCESS_CALC_HURDLE_HWM_HARD.  
  
The enumeration is used in the [IMTConFund::FeeSuccessMode](FeeSuccessMode.md) method.

<a id="enfeesuccesshwmtype"></a>
## IMTConFund::EnFeeSuccessHWMType (#enfeesuccesshwmtype)

The IMTConFund::EnFeeSuccessHWMType enumeration provides a list of modes for determining the fund management success.

ID | Value | Description  
FEE_SUCCESS_HWM_TYPE_FULL | 0 | Exceeding the hurdle rate for the entire period.  
FEE_SUCCESS_HWM_TYPE_QUATER | 1 | Exceeding the hurdle rate for the last quarter.  
FEE_SUCCESS_HWM_TYPE_YEAR | 2 | Exceeding the hurdle rate for the last year.  
FEE_SUCCESS_CALC_FIRST |  | Beginning of enumeration. Corresponds to FEE_SUCCESS_HWM_TYPE_FULL.  
FEE_SUCCESS_CALC_LAST |  | End of enumeration. Corresponds to FEE_SUCCESS_HWM_TYPE_YEAR.  
  
The enumeration is used in the [IMTConFund::FeeSuccessHWM](FeeSuccessHWM.md) method.
