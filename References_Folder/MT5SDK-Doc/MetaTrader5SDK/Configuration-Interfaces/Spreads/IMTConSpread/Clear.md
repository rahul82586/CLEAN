[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / Clear

[Previous](Assign.md) | [Next](ID.md)

# IMTConSpread::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConSpread::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
