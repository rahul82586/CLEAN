[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomationSink](../IMTConAutomationSink.md) / OnAutomationDelete

[Previous](OnAutomationUpdate.md) | [Next](OnAutomationSync.md)

# IMTConAutomationSink:OnAutomationDelete

Event hander for the deletion of an automation configuration.

C++
    
    
    virtual void  IMTConAutomationSink::OnAutomationDelete(
       const IMTConAutomation*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConAutomationSink.OnAutomationDelete(
       CIMTConAutomation         config  // Configuration object
       )

### Parameters

**config**  
A pointer to the deletedIMTConAutomationconfiguration object.

### Note

This method is called by the API to notify that an automation configuration has been deleted.
