[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTAccountArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTAccountArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
