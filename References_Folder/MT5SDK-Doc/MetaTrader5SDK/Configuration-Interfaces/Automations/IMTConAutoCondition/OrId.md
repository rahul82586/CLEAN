[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / OrId

[Previous](Rule.md) | [Next](ValueType.md)

# IMTConAutoCondition::OrId

Get the identifier for the "OR" condition group.

C++
    
    
    UINT  IMTConAutoCondition::OrId()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.OrId()

Python
    
    
    MTConAutoCondition.OrId

### Return Value

Identifier for the "OR" condition group.

### Note

If several conditions of the same type have the same OrId, it means that they belong to the same "OR" condition block.

# IMTConAutoCondition::OrId

Set the identifier for the "OR" condition group.

C++
    
    
    MTAPIRES  IMTConAutoCondition::OrId(
       const UINT       or_id  // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.OrId(
       uint             or_id  // identifier
       )

Python
    
    
    MTConAutoCondition.OrId

### Parameters

**or_id**  
[in] Identifier for the "OR" condition group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The property is used to create "OR" conditions.
