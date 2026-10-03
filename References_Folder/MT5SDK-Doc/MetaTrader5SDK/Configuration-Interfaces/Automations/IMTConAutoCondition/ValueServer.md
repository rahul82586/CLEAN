[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueServer

[Previous](ValueLanguage.md) | [Next](ValuePositionType.md)

# IMTConAutoCondition::ValueServer

Get the value of a condition expressing [server identifier](../../Network/IMTConServer/Id.md).

C++
    
    
    UINT64  IMTConAutoCondition::ValueServer()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConAutoCondition.ValueServer()

Python
    
    
    MTConAutoCondition.ValueServer

### Return Value

The condition value of the UINT type.

# IMTConAutoCondition::ValueServer

Set the value of a condition expressing [server identifier](../../Network/IMTConServer/Id.md).

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueServer(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueServer(
       ulong         value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueServer

### Parameters

**value**  
[in] A value of the UINT type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
