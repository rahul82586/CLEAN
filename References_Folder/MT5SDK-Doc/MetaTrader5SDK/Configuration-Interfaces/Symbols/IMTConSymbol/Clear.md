[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Clear

[Previous](Assign.md) | [Next](Symbol.md)

# IMTConSymbol::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConSymbol::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
