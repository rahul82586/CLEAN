[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionSymbol](../IMTConSubscriptionSymbol.md) / Symbol

[Previous](Clear.md) | [Next](Level.md)

# IMTConSubscriptionSymbol::Symbol

Get the name of a symbol data for which is provided by the subscription.

C++
    
    
    LPCWSTR  IMTConSubscriptionSymbol::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscriptionSymbol.Symbol()

### Return Value

If successful, the method returns a pointer to a string with the symbol name, including its path. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSubscriptionSymbol](../IMTConSubscriptionSymbol.md) object.

# IMTConSubscriptionSymbol::Symbol

Set the name of a symbol data for which is provided by the subscription.

C++
    
    
    MTAPIRES  IMTConSubscriptionSymbol::Symbol(
       LPCWSTR  symbol      // Symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscriptionSymbol.Symbol(
       string   symbol      // Symbol
       )

### Parameters

**symbol**  
[in] Path to a symbol or a group of symbols. For example, Forex\EURUSD or CFD\*.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The symbol name length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
