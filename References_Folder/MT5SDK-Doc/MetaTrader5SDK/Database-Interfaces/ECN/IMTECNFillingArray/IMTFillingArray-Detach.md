[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray Detach

[Previous](IMTFillingArray-Delete.md) | [Next](IMTFillingArray-Update.md)

# IMTECNFillingArray::Detach

Detach a filling order object from an array.

C++
    
    
    IMTECNFilling*  IMTECNFillingArray::Detach(
       const UINT  pos      // order position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTECNFilling  CIMTECNFillingArray.Detach(
       uint        pos      // order position
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

### Return Value

Returns a pointer to the detached order object.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
