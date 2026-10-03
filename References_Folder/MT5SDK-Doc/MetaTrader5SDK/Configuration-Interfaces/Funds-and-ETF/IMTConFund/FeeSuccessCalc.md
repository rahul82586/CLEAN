[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeSuccessCalc

[Previous](FeeManagementAssets.md) | [Next](FeeSuccessMode.md)

# IMTConFund::FeeSuccessCalc

Get the success fee calculation mode.

C++
    
    
    UINT  IMTConFund::FeeSuccessCalc()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.FeeSuccessCalc()

### Return Value

Success fee calculation mode as a value of the [IMTConFund::EnFeeSuccessCalc (#enfeesuccesscalc)](Enumerations.md#enfeesuccesscalc) enumeration.

# IMTConFund::FeeSuccessCalc

Set the success fee calculation mode.

C++
    
    
    MTAPIRES  IMTConFund::FeeSuccessCalc(
       const UINT  mode      // Calculation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeSuccessCalc(
       uint        mode      // Calculation mode
       )

### Parameters

**mode**  
[in] Success fee calculation mode as a value of theIMTConFund::EnFeeSuccessCalcenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
