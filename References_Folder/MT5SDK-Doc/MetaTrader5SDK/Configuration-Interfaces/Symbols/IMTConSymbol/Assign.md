[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConSymbol::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConSymbol::Assign(
       const IMTConSymbol*  symbol      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Assign(
       CIMTConSymbol        symbol      // Source object
       )

### Parameters

**symbol**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
