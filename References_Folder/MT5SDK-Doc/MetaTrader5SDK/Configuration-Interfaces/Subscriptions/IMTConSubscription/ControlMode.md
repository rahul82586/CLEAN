[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / ControlMode

[Previous](URLAgreement.md) | [Next](PeriodMode.md)

# IMTConSubscription::ControlMode

Get a subscription management mode in client terminals (allowed actions).

C++
    
    
    UINT  IMTConSubscription::ControlMode()  const

.NET (Gateway/Manager API)
    
    
    EnControlMode  CIMTConSubscription.ControlMode()

### Return Value

Subscription management mode. Passed as a value of the [IMTConSubscription::EnControlMode (#encontrolmode)](Enumerations.md#encontrolmode) enumeration.

# IMTConSubscription::ControlMode

Set a subscription management mode in client terminals (allowed actions).

C++
    
    
    MTAPIRES  IMTConSubscription::ControlMode(
       const UINT      mode     // Management mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.ControlMode(
       EnControlMode   mode     // Management mode
       )

### Parameters

**mode**  
[in] Subscription management mode. Passed as a value of theIMTConSubscription::EnControlModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
