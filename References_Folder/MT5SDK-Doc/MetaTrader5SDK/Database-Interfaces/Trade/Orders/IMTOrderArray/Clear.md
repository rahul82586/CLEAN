[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTOrderArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTOrderArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
