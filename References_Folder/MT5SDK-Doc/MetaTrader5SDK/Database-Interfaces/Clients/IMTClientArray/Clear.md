[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTClientArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTClientArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears all fields ​​and removes nested objects.
