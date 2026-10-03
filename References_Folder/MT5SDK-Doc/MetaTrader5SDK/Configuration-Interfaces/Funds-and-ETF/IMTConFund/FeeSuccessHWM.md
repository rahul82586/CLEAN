[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeSuccessHWM

[Previous](FeeSuccessValue.md) | [Next](FeeSuccessHurdleRate.md)

# IMTConFund::FeeSuccessHWM

Get the period for which the excess of the hurdle rate is determined when assessing the fund management success.

C++
    
    
    UINT  IMTConFund::FeeSuccessHWM()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.FeeSuccessHWM()

### Return Value

Period 

# IMTConFund::FeeSuccessHWM

Set the period for which the excess of the hurdle rate is determined when assessing the fund management success.

C++
    
    
    MTAPIRES  IMTConFund::FeeSuccessHWM(
       const UINT  mode      // Period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeSuccessHWM(
       uint        mode      // Period
       )

### Parameters

**mode**  
[in] Period as theIMTConFund::EnFeeSuccessHWMTypeenumeration value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
