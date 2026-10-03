[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSession](../IMTConSymbolSession.md) / Clear

[Previous](Assign.md) | [Next](Open.md)

# IMTConSymbolSession::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConSymbolSession::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolSession.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
