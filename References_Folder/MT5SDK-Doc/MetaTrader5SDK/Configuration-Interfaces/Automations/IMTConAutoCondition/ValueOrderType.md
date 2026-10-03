[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueOrderType

[Previous](ValueDealEntry.md) | [Next](ValueOrderState.md)

# IMTConAutoCondition::ValueOrderType

Get a condition value expressing order type.

C++
    
    
    UINT  IMTConAutoCondition::ValueOrderType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.ValueOrderType()

Python
    
    
    MTConAutoCondition.ValueOrderType

### Return Value

[Type of the order](../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md).

### Note

The order type is set by the [IMTConAutoCondition::CONDITION_ORDER_TYPE (#enconditions)](Enumerations.md#enconditions) condition.

# IMTConAutoCondition::ValueDealType

Set a condition value expressing order type.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueOrderType(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueOrderType(
       uint        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueOrderType

### Parameters

**value**  
[in]Order type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The order type is set by the [IMTConAutoCondition::CONDITION_ORDER_TYPE (#enconditions)](Enumerations.md#enconditions) condition.
