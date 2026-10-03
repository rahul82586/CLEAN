[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeSuccessMode

[Previous](FeeSuccessCalc.md) | [Next](FeeSuccessValue.md)

# IMTConFund::FeeSuccessMode

Get the time for calculating the success fee in relation to the management fee charges.

C++
    
    
    UINT  IMTConFund::FeeSuccessMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.FeeSuccessMode()

### Return Value

The time for calculating the success fee in relation to the management fee charges. Passed 

# IMTConFund::FeeSuccessMode

Set the time for calculating the success fee in relation to the management fee charges.

C++
    
    
    MTAPIRES  IMTConFund::FeeSuccessMode(
       const UINT  mode      // Calculation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeSuccessMode(
       uint        mode      // Calculation mode
       )

### Parameters

**mode**  
[in] The time for calculating the success fee in relation to the management fee charges. Passed as a value of theIMTConFund::EnFeeSuccessModesenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
