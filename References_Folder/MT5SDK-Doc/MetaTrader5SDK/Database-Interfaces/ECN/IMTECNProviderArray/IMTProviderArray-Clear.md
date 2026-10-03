[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Clear

[Previous](IMTProviderArray-Assign.md) | [Next](IMTProviderArray-Add.md)

# IMTECNProviderArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNProviderArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIIMTECNProviderArray.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
