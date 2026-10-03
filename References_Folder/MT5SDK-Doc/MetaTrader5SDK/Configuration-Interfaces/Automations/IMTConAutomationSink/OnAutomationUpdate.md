[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomationSink](../IMTConAutomationSink.md) / OnAutomationUpdate

[Previous](OnAutomationAdd.md) | [Next](OnAutomationDelete.md)

# IMTConAutomationSink::OnAutomationUpdate

Event hander for the update of an automation configuration.

C++
    
    
    virtual void  IMTConAutomationSink::OnAutomationUpdate(
       const IMTConAutomation*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConAutomationSink.OnAutomationUpdate(
       CIMTConAutomation         config  // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the updatedIMTConAutomationconfiguration object.

### Note

This method is called by the API to notify that an automation configuration has been changed.
