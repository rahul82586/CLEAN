[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Symbol

[Previous](IMTHistoryDeal-TimeMsc.md) | [Next](IMTHistoryDeal-Action.md)

# IMTECNHistoryDeal::Symbol

Get the name of the trading symbol for which the deal was executed.

C++
    
    
    LPCWSTR  IMTECNHistoryDeal::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNHistoryDeal.Symbol()

### Return Value

The name of the trading symbol for which the deal was executed.

### Note

A pointer to the resulting string is valid for the [IMTECNHistoryDeal](../IMTHistoryDeal.md) object lifetime.

# IMTECNHistoryDeal::Symbol

Set the name of the trading symbol for which the deal was executed.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Symbol(
       LPCWSTR       symbol    // symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Symbol(
       string        symbol    // symbol
       )

### Parameters

**symbol**  
[in] The name of the trading symbol for which the deal was executed.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The symbol name length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
