[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray AddCopy

[Previous](IMTProviderArray-Add.md) | [Next](IMTProviderArray-Delete.md)

# IMTECNProviderArray::AddCopy

Add a copy of a provider object to the end of an array.

C++
    
    
    MTAPIRES  IMTECNProviderArray::AddCopy(
       const IMTECNProvider*       provider  // provider to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.AddCopy(
       CIMTECNProvider             provider  // provider to be added
       )

### Parameters

**provider**  
[in]Provider object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of the 'provider' object and places it at the end of the array.

# IMTECNProviderArray::AddCopy

Add copies of deal objects into an array.

C++
    
    
    MTAPIRES  IMTECNProviderArray::AddCopy(
       const IMTECNProviderArray*   array   // array of providers to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.AddCopy(
       CIMTECNProviderArray         array   // array of providers to be added
       )

### Parameters

**array**  
[in] Array of provider arrays.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of order objects belonging to the 'array' object, and inserts them at the end of the current array.
