[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Shift

[Previous](Delete.md) | [Next](Total.md)

# IMTServerAPI::FirewallShift

Change the position of a firewall configuration in the list.
    
    
    MTAPIRES  IMTServerAPI::FirewallShift(
       const UINT  pos,       // Position of the configuration
       const int   shift      // Shift
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**shift**  
[in] Shift of the configuration relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The position of a configuration can be changed only from the plugins that run on the main
