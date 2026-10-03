[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Update

[Previous](IMTProviderArray-Detach.md) | [Next](IMTProviderArray-UpdateCopy.md)

# IMTECNProviderArray::Update

Update a provider at the specified position of an array.

C++
    
    
    MTAPIRES  IMTECNProviderArray::Update(
       const UINT       pos,      // position
       IMTECNProvider*  provider  // provider object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.Update(
       uint             pos,      // position
       CIMTECNProvider  provider  // provider object
       )

### Parameters

**pos**  
[in] Position of a provider in the array, starting with 0.

**provider**  
[in]Provider object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The IMTECNProviderArray::Update method deletes the previous element ([IMTECNProvider::Release](../IMTECNProvider/IMTProvider-Release.md) call) and replaces it with a new one. After that, the lifetime of the new element is controlled by an array object. Therefore, when you delete an array object (IMTECNProviderArray::Release call), the earlier inserted object is automatically deleted.

### Example
    
    
    //--- example
      IMTECNProviderArray *array=api->ECNProviderCreateArray();  
       IMTECNProvider      *provider1=api->ECNProviderCreate();
       IMTECNProvider      *provider2=api->ECNProviderCreate();
    //---
       array->Add(provider1);
       array->Update(0,provider2); // the first element (the provider1 object) is replaced with provider2
       //--- after that the provider1 element will be released via Release, and provider2 lifetime will be controlled by the array
