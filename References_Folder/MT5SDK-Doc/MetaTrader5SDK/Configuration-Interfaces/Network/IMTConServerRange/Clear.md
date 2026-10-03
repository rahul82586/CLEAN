[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerRange](../IMTConServerRange.md) / Clear

[Previous](Assign.md) | [Next](From.md)

# IMTConServerRange::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConServerRange::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerRange.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
