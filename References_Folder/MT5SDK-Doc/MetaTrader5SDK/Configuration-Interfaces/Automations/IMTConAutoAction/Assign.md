[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConAutoAction::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConAutoAction::Assign(
       const IMTConAutoAction*  action  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoAction.Assign(
       CIMTConAutoAction        action  // Source object
       )

### Parameters

**action**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
