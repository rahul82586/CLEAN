[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / LimitSymbols

[Previous](LimitOrders.md) | [Next](LimitPositions.md)

# IMTConGroup::LimitSymbols

Get the maximum number of symbols, for which an account can simultaneously receive quotes.

C++
    
    
    UINT  IMTConGroup::LimitSymbols()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroup.LimitSymbols()

Python (Manager API)
    
    
    MTConGroup.LimitSymbols

### Return Value

The maximum number of symbols, for which an account can simultaneously receive quotes.

# IMTConGroup::LimitSymbols

Set the maximum number of symbols, for which an account can simultaneously receive quotes.

C++
    
    
    MTAPIRES  IMTConGroup::LimitSymbols(
       const UINT  limit      // Limit of symbols
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.LimitSymbols(
       uint        limit      // Limit of symbols
       )

Python (Manager API)
    
    
    MTConGroup.LimitSymbols

### Parameters

**limit**  
[in] The maximum number of symbols, for which an account can simultaneously receive quotes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
