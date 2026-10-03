[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / PeriodCustom

[Previous](PeriodMode.md) | [Next](PeriodFreeMode.md)

# IMTConSubscription::PeriodCustom

Get a custom subscription period.

C++
    
    
    UINT  IMTConSubscription::PeriodCustom()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSubscription.PeriodCustom()

### Return Value

Custom subscription period in days.

### Note

The method is used if the [IMTConSubscription::PERIOD_CUSTOM (#enperiod)](Enumerations.md#enperiod) mode is selected for a subscription.

# IMTConSubscription::PeriodCustom

Set a custom subscription period.

C++
    
    
    MTAPIRES  IMTConSubscription::PeriodCustom(
       const UINT      days     // Subscription period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.PeriodCustom(
       uint            days     // Subscription period
       )

### Parameters

**days**  
[in] Custom subscription period in days.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The method is used if the [IMTConSubscription::PERIOD_CUSTOM (#enperiod)](Enumerations.md#enperiod) mode is selected for a subscription.
