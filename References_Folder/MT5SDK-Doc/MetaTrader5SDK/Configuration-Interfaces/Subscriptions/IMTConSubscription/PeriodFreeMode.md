[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / PeriodFreeMode

[Previous](PeriodCustom.md) | [Next](PeriodFreeCustom.md)

# IMTConSubscription::PeriodFreeMode

Get a trial (free) subscription period.

C++
    
    
    UINT  IMTConSubscription::PeriodFreeMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSubscription.PeriodFreeMode()

### Return Value

Trial subscription period. The period is passed as a value of the [IMTConSubscription::EnFreePeriod (#enfreeperiod)](Enumerations.md#enfreeperiod) enumeration.

# IMTConSubscription::PeriodFreeMode

Set a trial (free) subscription period.

C++
    
    
    MTAPIRES  IMTConSubscription::PeriodFreeMode(
       const UINT      mode     // Trial subscription period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.PeriodFreeMode(
       uint            mode     // Trial subscription period
       )

### Parameters

**mode**  
[in] Trial subscription period. The period is passed as a value of theIMTConSubscription::EnFreePeriodenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
