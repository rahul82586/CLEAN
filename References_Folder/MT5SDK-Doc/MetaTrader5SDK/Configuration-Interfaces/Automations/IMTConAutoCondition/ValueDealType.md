[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueDealType

[Previous](ValueReason.md) | [Next](ValueDealEntry.md)

# IMTConAutoCondition::ValueDealType

Get a condition value expressing the deal type.

C++
    
    
    UINT  IMTConAutoCondition::ValueDealType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.ValueDealType()

Python
    
    
    MTConAutoCondition.ValueDealType

### Return Value

[Deal type](../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md).

# IMTConAutoCondition::ValueDealType

Set a condition value expressing the deal type.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueDealType(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueDealType(
       uint        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueDealType

### Parameters

**value**  
[in]Deal type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
