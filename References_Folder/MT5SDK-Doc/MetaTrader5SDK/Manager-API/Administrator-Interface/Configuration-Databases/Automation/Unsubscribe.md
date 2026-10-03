[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Update.md)

# IMTAdminAPI::AutomationUnsubscribe

Unsubscribe from events and hooks associated with the automation configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::AutomationUnsubscribe(
       IMTConAutomationSink*  sink   // A pointer to the IMTConAutomationSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.AutomationUnsubscribe(
       CIMTConAutomationSink  sink   // CIMTConAutomationSink object
       )

Python
    
    
    AdminAPI.AutomationUnsubscribe(
       sink                   # IMTConAutomationSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConAutomationSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is paired with [IMTAdminAPI::AutomationSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface which has not been previously subscribed to, the [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
