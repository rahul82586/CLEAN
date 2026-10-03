[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / Clear

[Previous](Assign.md) | [Next](Priority.md)

# IMTConServerAccess::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConServerAccess::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
