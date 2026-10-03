[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Exposure](../Exposure.md) / Next

[Previous](Total.md) | [Next](Get.md)

# IMTManagerAPI::ExposureNext

Get a record from an exposure table by an index.

C++
    
    
    MTAPIRES  IMTManagerAPI::ExposureNext(
       const UINT    pos,          // Position
       IMTExposure*  exposure      // Exposure object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ExposureNext(
       uint          pos,          // Position
       CIMTExposure  exposure      // Exposure object
       )

Python
    
    
    ManagerAPI.ExposureNext(
       int           pos           # Position
       )

### Parameters

**pos**  
[in] Position of the record, starting with 0.

**exposure**  
[out] An object of the exposure record. The exposure object must first be created using theIMTManagerAPI::ExposureCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To receive information about exposure, it is necessary to subscribe to events of its changes using the [IMTManagerAPI::ExposureSubscribe](Subscribe.md) method.
