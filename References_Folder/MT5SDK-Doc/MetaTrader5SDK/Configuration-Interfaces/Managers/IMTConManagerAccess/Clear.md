[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerAccess](../IMTConManagerAccess.md) / Clear

[Previous](Assign.md) | [Next](From.md)

# IMTConManagerAccess::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConManagerAccess::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManagerAccess.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
