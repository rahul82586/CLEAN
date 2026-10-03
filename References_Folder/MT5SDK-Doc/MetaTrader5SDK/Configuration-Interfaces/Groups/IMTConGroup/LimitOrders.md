[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / LimitOrders

[Previous](LimitHistory.md) | [Next](LimitSymbols.md)

# IMTConGroup::LimitOrders

Get the maximum number of orders that can be simultaneously placed by an account from this group.

C++
    
    
    UINT  IMTConGroup::LimitOrders()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroup.LimitOrders()

Python (Manager API)
    
    
    MTConGroup.LimitOrders

### Return Value

The maximum number of orders that can be simultaneously placed. The 0 value means that the number of orders is unlimited.

# IMTConGroup::LimitOrders

Set the maximum number of orders that can be simultaneously placed by an account from this group.

C++
    
    
    MTAPIRES  IMTConGroup::LimitOrders(
       const UINT  limit      // Limit of orders
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.LimitOrders(
       ouint       limit      // Limit of orders
       )

Python (Manager API)
    
    
    MTConGroup.LimitOrders

### Parameters

**limit**  
[in] The maximum number of orders that can be simultaneously placed. The 0 value means that the number of orders is unlimited.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
