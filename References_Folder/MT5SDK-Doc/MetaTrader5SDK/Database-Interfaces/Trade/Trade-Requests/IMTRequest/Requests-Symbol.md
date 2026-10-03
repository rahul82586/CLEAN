[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Symbol

[Previous](Requests-Group.md) | [Next](Requests-SymbolOriginal.md)

# IMTRequest::Symbol

Get the symbol, a request for which is received.

C++
    
    
    LPCWSTR  IMTRequest::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.Symbol()

### Return Value

If successful, it returns a pointer to a string with a request symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTRequest](../Requests-IMTRequest.md) object.

# IMTRequest::Symbol

Set the symbol of a trade request.

C++
    
    
    MTAPIRES  IMTRequest::Symbol(
       LPCWSTR  symbol      // Symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Symbol(
       string   symbol      // Symbol
       )

### Parameters

**symbol**  
[in] The symbol of a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name.
