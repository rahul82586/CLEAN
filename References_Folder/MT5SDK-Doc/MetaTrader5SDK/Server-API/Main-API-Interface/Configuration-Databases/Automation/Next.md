[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Next

[Previous](Total.md) | [Next](Get.md)

# IMTServerAPI::AutomationNext

Get an automation configuration by index.
    
    
    MTAPIRES  IMTServerAPI::AutomationNext(
       const UINT         pos,      // Configuration position
       IMTConAutomation*  config    // Automation configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting at 0.

**config**  
[out] Automation configuration object. The 'config' object must be previously created using theIMTServerAPI::AutomationCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of the automation task a specified index to the 'config' object.
