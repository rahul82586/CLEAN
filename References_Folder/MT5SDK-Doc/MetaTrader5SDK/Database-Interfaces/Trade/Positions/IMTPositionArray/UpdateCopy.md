[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTPositionArray::UpdateCopy

Change a trade position at the specified position of an array by copying the parameters of a passed object of a trade position.

C++
    
    
    MTAPIRES  IMTPositionArray::UpdateCopy(
       const UINT        pos,       // Position
       const IMTOrder*   order      // An object of a trade order
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.UpdateCopy(
       uint              pos,       // Position
       CIMTOrder         order      // An object of a trade order
       )

### Parameters

**pos**  
[in] The index of a trade position in an array, starting with 0.

**order**  
[in] An object of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the position object into an object of a trade position at the specified position of an array.
