[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Get

[Previous](Next.md) | [Next](Trigger.md)

# IMTServerAPI::AutomationGet

Get an automation configuration by name.
    
    
    MTAPIRES  IMTServerAPI::AutomationGet(
       LPCWSTR            name,     // Configuration name
       IMTConAutomation*  config    // Automation configuration object
       )

### Parameters

**name**  
[in] The name of the configuration.

**config**  
[out] Automation configuration object. The 'config' object must be previously created using theIMTServerAPI::AutomationCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConAutomation::Name](../../../../Configuration-Interfaces/Automations/IMTConAutomation/Name.md) value is used as the name.
