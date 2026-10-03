[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTOnlineArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTOnlineArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
