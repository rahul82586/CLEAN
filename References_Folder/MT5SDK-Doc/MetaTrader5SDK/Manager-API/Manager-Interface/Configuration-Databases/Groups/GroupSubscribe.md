[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupSubscribe

[Previous](GroupTierCreate.md) | [Next](GroupUnsubscribe.md)

# IMTManagerAPI::GroupSubscribe

Subscribe to events associated with the configuration of groups.

C++
    
    
    MTAPIRES  IMTManagerAPI::GroupSubscribe(
       IMTConGroupSink*  sink      // A pointer to the IMTConGroupSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.GroupSubscribe(
       CIMTConGroupSink  sink      // CIMTConGroupSink object
       )

Python
    
    
    ManagerAPI.GroupSubscribe(
       sink              # IMTConGroupSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConGroupSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConGroupSink](../../../../Configuration-Interfaces/Groups/IMTConGroupSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
