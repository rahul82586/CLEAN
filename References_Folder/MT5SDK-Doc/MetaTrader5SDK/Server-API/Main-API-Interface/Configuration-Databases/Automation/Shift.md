[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Shift

[Previous](Delete.md) | [Next](Total.md)

# IMTServerAPI::AutomationShift

Change the position of an automation configuration in the list.
    
    
    MTAPIRES  IMTServerAPI::AutomationShift(
       const UINT  pos,       // Configuration position
       const int   shift      // Shift
       )

### Parameters

**pos**  
[in] Position of the configuration, starting at 0.

**shift**  
[in] The shift of the configuration relative to its current position. A negative value means shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The position of a configuration can be changed only from the plugins that run on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
