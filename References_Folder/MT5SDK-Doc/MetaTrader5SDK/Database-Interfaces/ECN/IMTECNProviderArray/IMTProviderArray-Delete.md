[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Delete

[Previous](IMTProviderArray-AddCopy.md) | [Next](IMTProviderArray-Detach.md)

# IMTECNProviderArray::Delete

Delete a provider object by its position.

C++
    
    
    MTAPIRES  IMTECNProviderArray::Delete(
       const UINT  pos      // provider position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.Delete(
       uint        pos      // provider position
       )

### Parameters

**pos**  
[in] Position of a provider in the array, starting with 0.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The deleted object will be automatically released by the [IMTECNProvider::Release](../IMTECNProvider/IMTProvider-Release.md) method call.
