[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Exposure](../Exposure.md) / GetAll

[Previous](Get.md) | [Next](../Daily-Reports.md)

# IMTManagerAPI::ExposureGetAll

Get an array of exposure records.

C++
    
    
    MTAPIRES  IMTManagerAPI::ExposureGetAll(
       IMTExposureArray*  exposure      // An object of an array of exposure records
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ExposureGetAll(
       CIMTExposureArray  exposure      // An object of an array of exposure records
       )

Python
    
    
    ManagerAPI.ExposureGetAll()

### Parameters

**exposure**  
[out] An object of the array. The exposure object must first be created using theIMTManagerAPI::ExposureCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To receive information about exposure, it is necessary to subscribe to events of its changes using the [IMTManagerAPI::ExposureSubscribe](Subscribe.md) method.
