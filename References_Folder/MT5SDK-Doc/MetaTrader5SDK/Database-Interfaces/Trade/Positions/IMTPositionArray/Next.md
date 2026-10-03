[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTPositionArray::Next

Get an object of a trade position by the index.

C++
    
    
    IMTPosition*  IMTPositionArray::Next(
       const UINT  index      // The index of a trade position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTPosition  CIMTPositionArray.Next(
       uint        index      // The index of a trade position
       )

### Parameters

**index**  
[in] The index of a trade position in an wrray, starting with 0.

### Return Value

If successful, it returns a pointer to the path to the object of a position with the specified index in the array. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
