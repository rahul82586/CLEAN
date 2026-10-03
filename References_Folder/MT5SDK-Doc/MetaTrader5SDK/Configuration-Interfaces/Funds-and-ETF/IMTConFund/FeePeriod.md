[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeePeriod

[Previous](FeeMode.md) | [Next](FeeAccount.md)

# IMTConFund::FeePeriod

Get the fund management and success fee calculation period.

C++
    
    
    UINT  IMTConFund::FeePeriod()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.FeePeriod()

### Return Value

Fund management and success fee calculation period, as a value of the [IMTConFund::EnFeePeriod (#enfeeperiod)](Enumerations.md#enfeeperiod) enumeration.

# IMTConFund::FeePeriod

Set the fund management and success fee calculation period.

C++
    
    
    MTAPIRES  IMTConFund::FeePeriod(
       const UINT  period    // Calculation period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeePeriod(
       uint        period    // Calculation period
       )

### Parameters

**period**  
[in]Fund management and success fee calculation period, as a value of theIMTConFund::EnFeePeriodenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
