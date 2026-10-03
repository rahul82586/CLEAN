[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / PeriodFreeCustom

[Previous](PeriodFreeMode.md) | [Next](Flags.md)

# IMTConSubscription::PeriodFreeCustom

Get a custom value for a trial (free) subscription period.

C++
    
    
    UINT  IMTConSubscription::PeriodFreeCustom()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSubscription.PeriodFreeCustom()

### Return Value

Custom trial subscription period in days.

### Note

The method is used if the [IMTConSubscription::FREE_PERIOD_CUSTOM (#enfreeperiod)](Enumerations.md#enfreeperiod) mode is selected for a subscription.

# IMTConSubscription::PeriodFreeCustom

Set a custom value for a trial (free) subscription period.

C++
    
    
    MTAPIRES  IMTConSubscription::PeriodFreeCustom(
       const UINT      days     // Subscription period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.PeriodFreeCustom(
       uint            days     // Subscription period
       )

### Parameters

**days**  
[in] Custom trial subscription period in days.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The method is used if the [IMTConSubscription::FREE_PERIOD_CUSTOM (#enfreeperiod)](Enumerations.md#enfreeperiod) mode is selected for a subscription.
