[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerSubscribe

[Previous](ManagerReportCreate.md) | [Next](ManagerUnsubscribe.md)

# IMTServerAPI::ManagerSubscribe

Subscribe to events and hooks associated with the configuration of managers.
    
    
    MTAPIRES  IMTServerAPI::ManagerSubscribe(
       IMTConManagerSink*  sink      // A pointer to the IMTConManagerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConManagerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConManagerSink](../../../../Configuration-Interfaces/Managers/IMTConManagerSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
