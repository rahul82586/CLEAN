[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Subscribe

[Previous](ParamCreate.md) | [Next](Unsubscribe.md)

# IMTServerAPI::AutomationSubscribe

Subscribe to events and hooks associated with automation configurations.
    
    
    MTAPIRES  IMTServerAPI::AutomationSubscribe(
       IMTConAutomationSink*  sink   // A pointer to the IMTConAutomationSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConAutomationSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. The same [IMTConAutomationSink](../../../../Configuration-Interfaces/Automations/IMTConAutomationSink.md) interface cannot subscribe to an event twice. The [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) response code is returned in this case.
