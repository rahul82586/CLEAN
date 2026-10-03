[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray UpdateCopy

[Previous](IMTProviderArray-Update.md) | [Next](IMTProviderArray-Shift.md)

# IMTECNProviderArray::UpdateCopy

Update a provider at the specified position of an array by copying the parameters of a passed provider object.

C++
    
    
    MTAPIRES  IMTECNProviderArray::UpdateCopy(
       const UINT             pos,      // position
       const IMTECNProvider*  provider  // provider object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.UpdateCopy(
       uint                   pos,      // position
       CIMTECNProvider        provider  // provider object
       )

### Parameters

**pos**  
[in] Position of a provider in the array, starting with 0.

**provider**  
[in]Provider object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method copies the parameters of the 'provider' object into a deal object at the specified position of an array.
