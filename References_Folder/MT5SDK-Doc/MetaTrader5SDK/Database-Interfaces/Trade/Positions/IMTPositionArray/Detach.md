[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTPositionArray::Detach

Detach an object of a trade position from an array.

C++
    
    
    IMTPosition*  IMTPositionArray::Detach(
       const UINT  pos      // Position index
       )

.NET (Gateway/Manager API)
    
    
    CIMTPosition  CIMTPositionArray.Detach(
       uint        pos      // Position index
       )

### Parameters

**pos**  
[in] The index of a trade position in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of a position.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.
