[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Next

[Previous](IMTProviderArray-Total.md) | [Next](IMTProviderArray-Sort.md)

# IMTECNProviderArray::Next

Get a provider object by its position.

C++
    
    
    IMTECNProvider*  IMTECNProviderArray::Next(
       const UINT  index    // provider position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTECNProvider  CIMTECNProviderArray.Next(
       uint        index    // provider position
       )

### Parameters

**index**  
[in] Position of a provider in the array, starting with 0.

### Return Value

If successful, the method returns a pointer to the provider object at the specified position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, if you delete an array object, the returned pointer will become invalid.
