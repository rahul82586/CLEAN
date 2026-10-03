[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Symbol

[Previous](IMTMatching-TimeExpiration.md) | [Next](IMTMatching-SymbolClient.md)

# IMTECNMatching::Symbol

Get the name of the trading symbol, for which the matching order is placed on the ECN side.

C++
    
    
    LPCWSTR  IMTECNMatching::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNMatching.Symbol()

### Return Value

The name of the trading symbol, for which the matching order is placed on the ECN side.

### Note

A pointer to the resulting string is valid for the [IMTECNMatching](../IMTMatching.md) object lifetime.

To use the string after object deletion (by a call of the [IMTECNMatching::Release](IMTMatching-Release.md) method of this object), a copy of it should be created.

# IMTECNMatching::Symbol

Set the name of the trading symbol, for which the matching order is placed on the ECN side.

C++
    
    
    MTAPIRES  IMTECNMatching::Symbol(
       LPCWSTR       symbol    // symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Symbol(
       string        symbol    // symbol
       )

### Parameters

**symbol**  
[in] The name of the trading symbol, for which the matching order is placed on the ECN side.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The symbol name length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
