[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Detach

[Previous](IMTProviderArray-Delete.md) | [Next](IMTProviderArray-Update.md)

# IMTECNProviderArray::Detach

Detach a provider object from an array.

C++
    
    
    IMTECNProvider*  IMTECNProviderArray::Detach(
       const UINT  pos      // provider position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTECNProvider  CIMTECNProviderArray.Detach(
       uint        pos      // provider position
       )

### Parameters

**pos**  
[in] Position of a provider in the array, starting with 0.

### Return Value

Returns a pointer to the detached provider object.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
