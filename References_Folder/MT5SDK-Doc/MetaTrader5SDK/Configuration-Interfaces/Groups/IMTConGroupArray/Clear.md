[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTConGroupArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConGroupArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all field values ​and removes embedded objects.
