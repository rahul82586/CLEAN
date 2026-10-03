[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Add.md)

# IMTServerAPI::AutomationUnsubscribe

Unsubscribe from events and hooks associated with the automation configuration.
    
    
    MTAPIRES  IMTServerAPI::AutomationUnsubscribe(
       IMTConAutomationSink*  sink   // A pointer to the IMTConAutomationSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConAutomationSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is paired with [IMTServerAPI::AutomationSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface which has not been previously subscribed to, the [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
