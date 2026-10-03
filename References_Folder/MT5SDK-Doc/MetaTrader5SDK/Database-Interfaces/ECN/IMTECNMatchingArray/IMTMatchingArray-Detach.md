[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatchingArray](../IMTMatchingArray.md) / IMTMatchingArray Detach

[Previous](IMTMatchingArray-Delete.md) | [Next](IMTMatchingArray-Update.md)

# IMTECNMatchingArray::Detach

Detach a matching order object from an array.

C++
    
    
    IMTECNMatching*  IMTECNMatchingArray::Detach(
       const UINT  pos      // order position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTECNMatching  CIMTECNMatchingArray.Detach(
       uint        pos      // order position
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

### Return Value

Returns a pointer to the detached order object.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
