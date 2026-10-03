[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueDealEntry

[Previous](ValueDealType.md) | [Next](ValueOrderType.md)

# IMTConAutoCondition::ValueDealEntry

Get a condition value expressing deal direction.

C++
    
    
    UINT  IMTConAutoCondition::ValueDealEntry()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.ValueDealEntry()

Python
    
    
    MTConAutoCondition.ValueDealEntry

### Return Value

[Deal direction](../../../Database-Interfaces/Trade/Deals/IMTDeal/Entry.md).

# IMTConAutoCondition::ValueDealType

Set a condition value expressing deal direction.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueDealEntry(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueDealEntry(
       uint        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueDealEntry

### Parameters

**value**  
[in]Deal direction.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
