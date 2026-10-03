[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeMode

[Previous](MaxInvestors.md) | [Next](FeePeriod.md)

# IMTConFund::FeeMode

Get the fund management and success fee calculation mode.

C++
    
    
    UINT  IMTConFund::FeeMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.FeeMode()

### Return Value

Fund management and success fee calculation modes as a value of the [IMTConFund::EnFeeMode (#enfeemode)](Enumerations.md#enfeemode) enumeration.

# IMTConFund::FeeMode

Set the fund management and success fee calculation mode.

C++
    
    
    MTAPIRES  IMTConFund::FeeMode(
       const UINT  mode      // Calculation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeMode(
       uint        mode      // Calculation mode
       )

### Parameters

**mode**  
[in] Fund management and success fee calculation modes as a value of theIMTConFund::EnFeeModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
