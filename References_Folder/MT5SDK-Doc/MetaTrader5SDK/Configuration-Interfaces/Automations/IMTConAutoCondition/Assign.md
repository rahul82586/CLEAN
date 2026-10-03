[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConAutoCondition::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConAutoCondition::Assign(
       const IMTConAutoCondition*  condition  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.Assign(
       CIMTConAutoCondition        condition  // Source object
       )

### Parameters

**condition**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
