[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Next

[Previous](Total.md) | [Next](../Symbols.md)

# IMTAdminAPI::FirewallNext

Get the firewall configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::FirewallNext(
       const UINT       pos,        // Position of the configuration
       IMTConFirewall*  config      // Configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FirewallNext(
       uint             pos,        // Position of the configuration
       CIMTConFirewall  config      // Configuration
       )

Python
    
    
    AdminAPI.FirewallNext(
       pos              # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] An object of the firewall configuration. The config object must first be created using theIMTAdminAPI::FirewallCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the firewall configuration entry with a specified index to the config object.
