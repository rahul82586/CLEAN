[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTExposureArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTExposureArray::Assign(
       const IMTExposureArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.Assign(
       CIMTExposureArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
