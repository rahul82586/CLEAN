[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Shift

[Previous](IMTProviderArray-UpdateCopy.md) | [Next](IMTProviderArray-Total.md)

# IMTECNProviderArray::Shift

Change the position of a provider in an array.

C++
    
    
    MTAPIRES  IMTECNProviderArray::Shift(
       const UINT  pos,       // provider position
       const int   shift      // shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.Shift(
       uint        pos,       // provider position
       int         shift      // shift
       )

### Parameters

**pos**  
[in] Position of a provider in the array, starting with 0.

**shift**  
[in] Shift provider relative to its current position. A negative value means shift towards the array beginning, while a positive value means shift towards its end.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
