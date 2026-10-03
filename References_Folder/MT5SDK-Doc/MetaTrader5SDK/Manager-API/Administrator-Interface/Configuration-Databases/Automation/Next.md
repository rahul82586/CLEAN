[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Next

[Previous](Total.md) | [Next](Get.md)

# IMTAdminAPI::AutomationNext

Get an automation configuration by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::AutomationNext(
       const UINT         pos,      // Configuration position
       IMTConAutomation*  config    // Automation configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.AutomationNext(
       uint               pos,      // Configuration position
       CIMTConAutomation  config    // Automation configuration object
       )

Python
    
    
    AdminAPI.AutomationNext(
       pos                # Configuration position
       )

### Parameters

**pos**  
[in] Position of the configuration, starting at 0.

**config**  
[out] Automation configuration object. The 'config' object must be previously created using theIMTAdminAPI::AutomationCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of the automation task a specified index to the 'config' object.
