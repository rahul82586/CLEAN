[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Update

[Previous](Unsubscribe.md) | [Next](UpdateBatch.md)

# IMTAdminAPI::AutomationUpdate

Add or update an automation configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::AutomationUpdate(
       IMTConAutomation*  config  // Automation configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.AutomationUpdate(
       CIMTConAutomation  config  // Automation configuration object
       )

Python
    
    
    AdminAPI.AutomationUpdate(
       config             # Automation configuration object
       )

### Parameters

**config**  
[in] TheIMTConAutomationautomaton configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The record existence is checked during the method call. If the record already exists, it is updated. Otherwise a new record is added. The key field for comparison is the configuration name [IMTConAutomation::Name()](../../../../Configuration-Interfaces/Automations/IMTConAutomation/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConAutomationSink::OnAutomationUpdate](../../../../Configuration-Interfaces/Automations/IMTConAutomationSink/OnAutomationUpdate.md) notification method is not called.
