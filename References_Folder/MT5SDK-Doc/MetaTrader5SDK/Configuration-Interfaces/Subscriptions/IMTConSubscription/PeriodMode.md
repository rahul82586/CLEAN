[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / PeriodMode

[Previous](ControlMode.md) | [Next](PeriodCustom.md)

# IMTConSubscription::PeriodMode

Get a subscription period.

C++
    
    
    UINT  IMTConSubscription::PeriodMode()  const

.NET (Gateway/Manager API)
    
    
    EnPeriod  CIMTConSubscription.PeriodMode()

### Return Value

Subscription period. The period is passed as a value of the [IMTConSubscription::EnPeriod (#enperiod)](Enumerations.md#enperiod) enumeration.

# IMTConSubscription::PeriodMode

Set a subscription period.

C++
    
    
    MTAPIRES  IMTConSubscription::PeriodMode(
       const UINT      mode     // Subscription period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.PeriodMode(
       EnPeriod        mode     // Subscription period
       )

### Parameters

**mode**  
[in] Subscription period. The period is passed as a value of theIMTConSubscription::EnPeriodenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
