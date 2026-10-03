[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching Symbol

[Previous](IMTHistoryMatching-TimeExpiration.md) | [Next](IMTHistoryMatching-SymbolClient.md)

# IMTECNHistoryMatching::Symbol

Get the name of the trading symbol, for which the matching order is placed on the ECN side.

C++
    
    
    LPCWSTR  IMTECNHistoryMatching::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNHistoryMatching.Symbol()

### Return Value

The name of the trading symbol, for which the matching order is placed on the ECN side.

### Note

A pointer to the resulting string is valid for the [IMTECNHistoryMatching](../IMTHistoryMatching.md) object lifetime.

# IMTECNHistoryMatching::Symbol

Set the name of the trading symbol, for which the matching order is placed on the ECN side.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Symbol(
       LPCWSTR       symbol    // symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.Symbol(
       string        symbol    // symbol
       )

### Parameters

**symbol**  
[in] The name of the trading symbol, for which the matching order is placed on the ECN side.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The symbol name length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
