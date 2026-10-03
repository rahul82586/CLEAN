[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTExposureArray::AddCopy

Adds a copy of an asset record object at the end of an array.

C++
    
    
    MTAPIRES  IMTExposureArray::AddCopy(
       const IMTExposure*  exposure      // Asset record object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.AddCopy(
       CIMTExposure        exposure      // Asset record object
       )

### Parameters

**exposure**  
[in] The object of the asset record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'exposure' object and places it at the end of the array.

# IMTExposureArray::AddCopy

Adds copies of the asset record objects to an array.

C++
    
    
    MTAPIRES  IMTExposureArray::AddCopy(
       const IMTExposureArray*  array      // An object of exposure records array
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.AddCopy(
       CIMTExposureArray        array      // An object of exposure records array
       )

### Parameters

**array**  
[in] An object of arrays of exposure records.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates copies of asset record objects belonging to the 'array' object, and inserts them at the end of the current array.
