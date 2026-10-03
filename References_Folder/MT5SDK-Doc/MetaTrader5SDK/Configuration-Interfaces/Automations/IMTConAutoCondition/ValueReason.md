[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueReason

[Previous](ValuePositionType.md) | [Next](ValueDealType.md)

# IMTConAutoCondition::ValueReason

Get a condition value expressing the reason for a trading operation.

C++
    
    
    UINT  IMTConAutoCondition::ValueReason()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.ValueReason()

Python
    
    
    MTConAutoCondition.ValueReason

### Return Value

[Reason for position opening](../../../Database-Interfaces/Trade/Positions/IMTPosition/Reason.md) or [deal execution](../../../Database-Interfaces/Trade/Deals/IMTDeal/Reason.md).

# IMTConAutoCondition::ValueReason

Set a condition value expressing the reason for a trading operation.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueReason(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueReason(
       uint        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueReason

### Parameters

**value**  
[in]Reason for position openingordeal execution.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
