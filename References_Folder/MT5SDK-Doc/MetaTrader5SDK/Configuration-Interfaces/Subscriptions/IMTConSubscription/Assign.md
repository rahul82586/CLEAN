[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConSubscription::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConSubscription::Assign(
       const IMTConSubscription*  iface  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.Assign(
       CIMTConSubscription        iface  // Source object
       )

### Parameters

**iface**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
