[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Symbol

[Previous](IMTHistoryFilling-ExternalID.md) | [Next](IMTHistoryFilling-Type.md)

# IMTECNHistoryFilling::Symbol

Get the name of the trading instrument for which the filling order was created.

C++
    
    
    LPCWSTR  IMTECNHistoryFilling::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNHistoryFilling.Symbol()

### Return Value

The name of the financial symbol for which the filling order is created.

### Note

A pointer to the resulting string is valid for the [IMTECNFilling](../IMTFilling.md) object lifetime.

# IMTECNHistoryFilling::Symbol

Set the name of the trading instrument for which the filling order was created.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Symbol(
       LPCWSTR       symbol    // symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Symbol(
       string        symbol    // symbol
       )

### Parameters

**symbol**  
[in] The name of the financial symbol for which the filling order is created.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The symbol name length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
