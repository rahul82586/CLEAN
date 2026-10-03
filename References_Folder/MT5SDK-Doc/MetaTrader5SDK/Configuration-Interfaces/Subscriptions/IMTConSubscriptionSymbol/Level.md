[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionSymbol](../IMTConSubscriptionSymbol.md) / Level

[Previous](Symbol.md) | [Next](TickHistory.md)

# IMTConSubscriptionSymbol::Level

Get the type of price data available by subscription.

C++
    
    
    UINT64  IMTConSubscriptionSymbol::Level()  const

.NET (Gateway/Manager API)
    
    
    EnFlags  CIMTConSubscriptionSymbol.Level()

### Return Value

Type of price data as a value of the [IMTConSubscriptionSymbol::EnLevel (#enlevel)](Enumerations.md#enlevel) enumeration.

# IMTConSubscriptionSymbol::Level

Set the type of price data available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscriptionSymbol::Level(
       const UINT64  level   // Type of price data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscriptionSymbol.Level(
       EnFlags       level   // Type of price data
       )

### Parameters

**level**  
[in] Type of price data as a value of theIMTConSubscriptionSymbol::EnLevelenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
