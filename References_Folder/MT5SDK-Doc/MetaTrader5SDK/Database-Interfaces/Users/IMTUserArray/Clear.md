[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTUserArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTUserArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
