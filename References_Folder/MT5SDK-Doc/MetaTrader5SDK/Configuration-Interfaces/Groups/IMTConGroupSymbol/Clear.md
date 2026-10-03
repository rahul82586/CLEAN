[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / Clear

[Previous](Assign.md) | [Next](Default.md)

# IMTConGroupSymbol::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.Clear()

Python (Manager API)
    
    
    MTConGroupSymbol.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
