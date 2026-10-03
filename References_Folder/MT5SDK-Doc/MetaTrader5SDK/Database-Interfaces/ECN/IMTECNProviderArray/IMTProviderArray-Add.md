[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Add

[Previous](IMTProviderArray-Clear.md) | [Next](IMTProviderArray-AddCopy.md)

# IMTECNProviderArray::Add

Add a provider object to the end of an array.

C++
    
    
    MTAPIRES  IMTECNProviderArray::Add(
       IMTECNProvider*  provider  // provider to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.Add(
       CIMTECNProvider  provider  // provider to be added
       )

### Parameters

**provider**  
[in]Provider object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the 'provider' object lifetime is passed to the array object. Therefore, when you delete an array object ([IMTECNProviderArray::Release](IMTProviderArray-Release.md) call), the earlier inserted object is automatically deleted.

# IMTECNProviderArray::Add

Add an object of provider arrays to the end of an array.

C++
    
    
    MTAPIRES  IMTECNProviderArray::Add(
       IMTECNProviderArray*   array   // array of providers to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProviderArray.Add(
       CIMTECNProviderArray   array   // array of providers to be added
       )

### Parameters

**array**  
[in] Array of provider arrays.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method places the pointers stored in the 'array' object, at the end of the current array, and clears the 'array' object.

### Example
    
    
    //--- example
       IMTECNProvidergArray *array=api->ECNProviderCreateArray();   
       IMTECNProvider       *provider=api->ECNProviderCreate();
    //---
       array->Add(provider);  // after that the lifetime is controlled by the array
       array->Delete(0);   // delete the first element, after that a pointer in 'provider' becomes invalid ('Release' was called)
     
    //--- incorrect use example
       IMTECNProviderArray *array=api->ECNProviderCreateArray();   
       IMTECNProvider      *provider=api->ECNProviderCreate();
    //---
       array->Add(provider);
       array->Add(provider); // in this case the array will contain two pointers to one and the same object!
       //--- an attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
