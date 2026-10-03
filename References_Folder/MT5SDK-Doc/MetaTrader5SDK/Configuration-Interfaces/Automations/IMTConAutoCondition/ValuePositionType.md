[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValuePositionType

[Previous](ValueServer.md) | [Next](ValueReason.md)

# IMTConAutoCondition::ValuePositionType

Get a condition value expressing position type.

C++
    
    
    UINT  IMTConAutoCondition::ValuePositionType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.ValuePositionType()

Python
    
    
    MTConAutoCondition.ValuePositionType

### Return Value

[Position type](../../../Database-Interfaces/Trade/Positions/IMTPosition/Action.md).

# IMTConAutoCondition::ValuePositionType

Set a condition value expressing position type.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValuePositionType(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValuePositionType(
       uint        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValuePositionType

### Parameters

**value**  
[in]Position type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
