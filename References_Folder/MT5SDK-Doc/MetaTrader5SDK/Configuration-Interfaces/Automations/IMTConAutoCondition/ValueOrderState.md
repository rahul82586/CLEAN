[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueOrderState

[Previous](ValueOrderType.md) | [Next](../IMTConAutoAction.md)

# IMTConAutoCondition::ValueOrderState

Get a condition value expressing order state.

C++
    
    
    UINT  IMTConAutoCondition::ValueOrderState()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.ValueOrderState()

Python
    
    
    MTConAutoCondition.ValueOrderState

### Return Value

[Order state](../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md).

### Note

The order state is set by the [IMTConAutoCondition::CONDITION_ORDER_STATE (#enconditions)](Enumerations.md#enconditions) condition.

# IMTConAutoCondition::ValueOrderState

Set a condition value expressing order state.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueOrderState(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueOrderState(
       uint        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueOrderState

### Parameters

**value**  
[in]Order state.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The order state is set by the [IMTConAutoCondition::CONDITION_ORDER_STATE (#enconditions)](Enumerations.md#enconditions) condition.
