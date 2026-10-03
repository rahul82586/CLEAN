[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Exposure](../Exposure.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Currency.md)

# IMTManagerAPI::ExposureUnsubscribe

Undubscribe from events associated with changes in the exposure database.

C++
    
    
    MTAPIRES  IMTManagerAPI::ExposureUnsubscribe(
       IMTExposureSink*  sink      // A pointer to the IMTExposureSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ExposureUnsubscribe(
       CIMTExposureSink  sink      // CIMTExposureSink object
       )

Python
    
    
    ManagerAPI.ExposureUnsubscribe(
       callback          # MTExposureSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTExposureSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This is a pair method to [IMTManagerAPI::ExposureSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
