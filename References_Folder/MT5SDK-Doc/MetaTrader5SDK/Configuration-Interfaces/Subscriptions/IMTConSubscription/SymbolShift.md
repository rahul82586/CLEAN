[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / SymbolShift

[Previous](SymbolClear.md) | [Next](SymbolTotal.md)

# IMTConSubscription::SymbolShift

Shift a trading instrument in the list in subscription settings.

C++
    
    
    MTAPIRES  IMTConSubscription::SymbolShift(
       const UINT  pos,       // Symbol position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.SymbolShift(
       uint        pos,       // Symbol position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

**shift**  
[in] Shift of a symbol relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
