[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Get

[Previous](Next.md) | [Next](../VPS.md)

# IMTAdminAPI::AutomationGet

Get an automation configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::AutomationGet(
       LPCWSTR            name,     // Configuration name
       IMTConAutomation*  config    // Automation configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.AutomationGet(
       string             name,     // Configuration name
       CIMTConAutomation  config    // Automation configuration object
       )

Python
    
    
    AdminAPI.AutomationGet(
       name               // Configuration name
       )

### Parameters

**name**  
[in] The name of the configuration.

**config**  
[out] Automation configuration object. The 'config' object must be previously created using theIMTAdminAPI::AutomationCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConAutomation::Name](../../../../Configuration-Interfaces/Automations/IMTConAutomation/Name.md) value is used as the name.
