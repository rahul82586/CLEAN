[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTPositionArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTPositionArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
