[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching SymbolClient

[Previous](IMTHistoryMatching-Symbol.md) | [Next](IMTHistoryMatching-Type.md)

# IMTECNHistoryMatching::SymbolClient

Get the name of the trading symbol, for which the matching order is placed on the client side.

C++
    
    
    LPCWSTR  IMTECNHistoryMatching::SymbolClient()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNHistoryMatching.SymbolClient()

### Return Value

The name of the trading symbol, for which the matching order is placed on the client side.

### Note

A pointer to the resulting string is valid for the [IMTECNHistoryMatching](../IMTHistoryMatching.md) object lifetime.

# IMTECNHistoryMatching::SymbolClient

Set the name of the trading symbol, for which the matching order is placed on the client side.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::SymbolClient(
       LPCWSTR       symbol    // symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.SymbolClient(
       string        symbol    // symbol
       )

### Parameters

**symbol**  
[in] The name of the trading symbol, for which the matching order is placed on the client side.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The symbol name length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
