[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Exposure](../Exposure.md) / Subscribe

[Previous](CreateArray.md) | [Next](Unsubscribe.md)

# IMTManagerAPI::ExposureSubscribe

Subscribe to events associated with changes in the exposure database.

C++
    
    
    MTAPIRES  IMTManagerAPI::ExposureSubscribe(
       IMTExposureSink*  sink      // A pointer to the IMTExposureSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI::ExposureSubscribe(
       CIMTExposureSink  sink      // CIMTExposureSink object
       )

Python
    
    
    ManagerAPI::ExposureSubscribe(
       callback          # MTExposureSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTExposureSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTExposureSink](../../../Database-Interfaces/Trade/Assets/IMTExposureSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
