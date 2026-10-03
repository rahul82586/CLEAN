[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Subscribe

[Previous](Create.md) | [Next](Unsubscribe.md)

# IMTManagerAPI::TimeSubscribe

Subscribe to events associated with time configuration.

C++
    
    
    MTAPIRES  IMTManagerAPI::TimeSubscribe(
       IMTConTimeSink*  sink      // A pointer to the IMTConTimeSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TimeSubscribe(
       CIMTConTimeSink  obj       // CIMTConTimeSink object
       )

Python
    
    
    ManagerAPI.TimeSubscribe(
       sink             # IMTConTimeSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConTimeSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConTimeSink](../../../../Configuration-Interfaces/Time/IMTConSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
