[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeSuccessValue

[Previous](FeeSuccessMode.md) | [Next](FeeSuccessHWM.md)

# IMTConFund::FeeSuccessValue

Get the success fee amount.

C++
    
    
    double  IMTConFund::FeeSuccessValue()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConFund.FeeSuccessValue()

### Return Value

Success fee as a percentage of the total returns for the current period or of the profit above the Hurdle Rate (determined by the [IMTConFund::FeeSuccessCalc](FeeSuccessCalc.md) property). 

# IMTConFund::FeeSuccessValue

Set the success fee amount.

C++
    
    
    MTAPIRES  IMTConFund::FeeSuccessValue(
       const double  value      // Fee
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeSuccessValue(
       double        value      // Fee
       )

### Parameters

**value**  
[in] Success fee as a percentage of the total returns for the current period or of the profit above the Hurdle Rate (determined by theIMTConFund::FeeSuccessCalcproperty).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
