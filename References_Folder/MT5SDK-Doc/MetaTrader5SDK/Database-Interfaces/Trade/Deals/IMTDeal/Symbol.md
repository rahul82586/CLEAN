[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Symbol

[Previous](Time.md) | [Next](Price.md)

# IMTDeal::Symbol

Get the symbol, for which a deal was executed.

C++
    
    
    LPCWSTR  IMTDeal::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDeal.Symbol()

### Return Value

If successful, it returns a pointer to a string with the symbol name and path to it in accordance with the hierarchy of symbols in the platform. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDeal](../IMTDeal.md) object.

# IMTDeal::Symbol

Set the symbol, for which a deal is executed.

C++
    
    
    MTAPIRES  IMTDeal::Symbol(
       LPCWSTR  symbol      // Symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Symbol(
       string   symbol      // Symbol
       )

### Parameters

**symbol**  
[in] The symbol, for which a deal is executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name.
