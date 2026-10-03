[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Symbol

[Previous](LoginSet.md) | [Next](Action.md)

# IMTPosition::Symbol

Get the symbol of a trade position.

C++
    
    
    LPCWSTR  IMTPosition::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTPosition.Symbol()

### Return Value

If successful, it returns a pointer to a string with a position symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTPosition](../IMTPosition.md) object.

# IMTPosition::Symbol

Sets the symbol of a trade position.

C++
    
    
    MTAPIRES  IMTPosition::Symbol(
       LPCWSTR  symbol      // Symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Symbol(
       string   symbol      // Symbol
       )

### Parameters

**symbol**  
[in] The symbol of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name.
