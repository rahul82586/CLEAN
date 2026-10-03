[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatchingArray](../IMTMatchingArray.md) / IMTMatchingArray Next

[Previous](IMTMatchingArray-Total.md) | [Next](IMTMatchingArray-Sort.md)

# IMTECNMatchingArray::Next

Get a matching order object by its position.

C++
    
    
    IMTECNMatching*  IMTECNMatchingArray::Next(
       const UINT  pos      // order position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTECNMatching  CIMTECNMatchingArray.Next(
       uint        pos      // order position
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

### Return Value

If successful, the method returns a pointer to the order object at the specified array position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, if you delete an array object, the returned pointer will become invalid.
