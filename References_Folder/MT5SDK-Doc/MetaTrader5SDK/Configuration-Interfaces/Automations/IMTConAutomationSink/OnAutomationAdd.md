[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomationSink](../IMTConAutomationSink.md) / OnAutomationAdd

[Previous](../IMTConAutomationSink.md) | [Next](OnAutomationUpdate.md)

# IMTConAutomationSink::OnAutomationAdd

Event hander for the addition of a new automation configuration.

C++
    
    
    virtual void  IMTConAutomationSink::OnAutomationAdd(
       const IMTConAutomation*  config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConAutomationSink.OnAutomationAdd(
       CIMTConAutomation        config  // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the addedIMTConAutomationconfiguration.

### Note

This method is called by the API to notify that a new automation configuration has been added.
