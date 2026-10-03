[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Symbol

[Previous](Requests-Flags.md) | [Next](Requests-SymbolNew.md)

# IMTExecution::Symbol

Gets the symbol name, for which trade execution is performed.

C++
    
    
    LPCWSTR  IMTExecution::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.Symbol()

### Return Value

If successful, it returns a pointer to a string with the name of the symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of [IMTExecution](../Requests-IMTExecution.md) object.

# IMTExecution::Symbol

Sets the name of the symbol, for which trade execution is performed.

C++
    
    
    MTAPIRES  IMTExecution::Symbol(
       LPCWSTR  symbol      // Symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Symbol(
       string   symbol      // Symbol
       )

### Parameters

**symbol**  
[in] Name of the symbol, for which trade execution is performed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name.
