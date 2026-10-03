[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Assign

[Previous](IMTProviderArray-Release.md) | [Next](IMTProviderArray-Clear.md)

# IMTECNProviderArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNProviderArray::Assign(
       const IMTECNProviderArray*  provider // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.Assign(
       CIMTECNProviderArray        provider // source object
       )

### Parameters

**provider**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
