[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTConSymbolArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConSymbolArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all field values ​and removes embedded objects.
