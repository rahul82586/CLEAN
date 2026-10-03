[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionSymbol](../IMTConSubscriptionSymbol.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConSubscriptionSymbol::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConSubscriptionSymbol::Assign(
       const IMTConSubscriptionSymbol*  symbol  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.Assign(
       CIMTConSubscriptionSymbol        symbol  // Source object
       )

### Parameters

**symbol**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
