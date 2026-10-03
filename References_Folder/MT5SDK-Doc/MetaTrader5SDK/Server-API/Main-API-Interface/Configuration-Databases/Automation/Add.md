[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Add

[Previous](Unsubscribe.md) | [Next](Delete.md)

# IMTServerAPI::AutomationAdd

Add or update an automation configuration.
    
    
    MTAPIRES  IMTServerAPI::AutomationAdd(
       IMTConMessenger*  config  // Automaton configuration object
       )

### Parameters

**config**  
[in] TheIMTConAutomationautomaton configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The record existence is checked during the method call. If the record already exists, it is updated. Otherwise a new record is added. The key field for comparison is the configuration name [IMTConAutomation::Name()](../../../../Configuration-Interfaces/Automations/IMTConAutomation/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConAutomationSink::OnAutomationUpdate](../../../../Configuration-Interfaces/Automations/IMTConAutomationSink/OnAutomationUpdate.md) notification method is not called.
