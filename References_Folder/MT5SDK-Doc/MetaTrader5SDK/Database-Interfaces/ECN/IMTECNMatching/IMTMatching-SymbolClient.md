[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching SymbolClient

[Previous](IMTMatching-Symbol.md) | [Next](IMTMatching-Type.md)

# IMTECNMatching::SymbolClient

Get the name of the trading symbol, for which the matching order is placed on the client side.

C++
    
    
    LPCWSTR  IMTECNMatching::SymbolClient()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNMatching.SymbolClient()

### Return Value

The name of the trading symbol, for which the matching order is placed on the client side.

### Note

A pointer to the resulting string is valid for the [IMTECNMatching](../IMTMatching.md) object lifetime.

# IMTECNMatching::SymbolClient

Set the name of the trading symbol, for which the matching order is placed on the client side.

C++
    
    
    MTAPIRES  IMTECNMatching::SymbolClient(
       LPCWSTR       symbol    // symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.SymbolClient(
       string        symbol    // symbol
       )

### Parameters

**symbol**  
[in] The name of the trading symbol, for which the matching order is placed on the client side.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The symbol name length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
