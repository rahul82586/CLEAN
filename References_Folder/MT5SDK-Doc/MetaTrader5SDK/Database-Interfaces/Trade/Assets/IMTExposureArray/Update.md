[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTExposureArray::Update

Modifies the asset record at the specified position of an array.

C++
    
    
    MTAPIRES  IMTExposureArray::Update(
       const UINT    pos,          // The position of the record
       IMTExposure*  exposure      // Asset record object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.Update(
       uint          pos,          // The position of the record
       CIMTExposure  exposure      // Asset record object
       )

### Parameters

**pos**  
[in] The position of an asset record in an array, starting with 0.

**exposure**  
[in] The object of the asset record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTExposureArray::Update method deletes the previous element (call of [IMTExposure::Release](../IMTExposure/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of [IMTExposureArray::Release](Release.md)), an earlier inserted object is automatically removed.

Example:
    
    
    //--- Example
        IMTExposureArray *array    =api->ExposureCreateArray();
        IMTExposure      *exposure1=api->ExposureCreate();
        IMTExposure      *exposure2=api->ExposureCreate();
     //---
        array->Add(exposure1);
        array->Update(0,exposure2); // The first element (the exposure1 object) is replaced with exposure2
        //--- After that the exposure1 element will be released through Release, and the lifetime of exposure2 will be controlled by the array
