[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTExposureArray::Add

Adds an asset record object at the end of an array.

C++
    
    
    MTAPIRES  IMTExposureArray::Add(
       IMTExposure*  exposure      // The asset record to add
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.Add(
       CIMTExposure  exposure      // The asset record to add
       )

### Parameters

**exposure**  
[in] The object of the asset record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the 'exposure' object is passed to the array object. Thus, when deleting an array object (call of [IMTExposureArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTExposureArray::Add

Adds an object of arrays of exposure records to the end of an array.

C++
    
    
    MTAPIRES  IMTExposureArray::Add(
       IMTExposureArray*  array      // An object of exposure records array
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.Add(
       CIMTExposureArray  array      // An object of exposure records array
       )

### Parameters

**array**  
[in] An object of arrays of exposure records.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

Example:
    
    
    //--- Example
        IMTExposureArray *array   =api->ExposureCreateArray();
        IMTExposure      *exposure=api->ExposureCreate();
     //---
        array->Add(exposure);// After that the lifetime is controlled by the array
        array->Delete(0);    // Delete the first element, after which the pointer in exposure becomes invalid (Release has been called)
     //--- An example of incorrect use
        IMTExposureArray  *array   =api->ExposureCreateArray();
        IMTExposure       *exposure=api->ExposureCreate();
     //---
        array->Add(exposure); 
        array->Add(exposure); // In this case the array contains two pointers to the same object!
        //--- Array clearing will cause crash, because two attempts will be made to delete the same object
