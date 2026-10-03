[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests SymbolNew

[Previous](Requests-Symbol.md) | [Next](Requests-Digits.md)

# IMTExecution::SymbolNew

Getting the name of a new symbol where position is relocated.

C++
    
    
    LPCWSTR  IMTExecution::SymbolNew()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.SymbolNew()

### Return Value

If successful, it returns a pointer to a string with the name of the symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of [IMTExecution](../Requests-IMTExecution.md) object.

# IMTExecution::SymbolNew

Setting the name of a new symbol where position is relocated.

C++
    
    
    MTAPIRES  IMTExecution::SymbolNew(
       LPCWSTR  symbol      // Symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.SymbolNew(
       string   symbol      // Symbol
       )

### Parameters

**symbol**  
[in] Name of the symbol, for which trade execution is performed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name.
