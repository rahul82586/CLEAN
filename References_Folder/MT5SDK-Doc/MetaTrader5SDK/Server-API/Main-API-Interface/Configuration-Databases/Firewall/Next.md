[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Next

[Previous](Total.md) | [Next](../Symbols.md)

# IMTServerAPI::FirewallNext

Get the firewall configuration by the index.
    
    
    MTAPIRES  IMTServerAPI::FirewallNext(
       const UINT       pos,        // Position of the configuration
       IMTConFirewall*  config      // Comment
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] An object of the firewall configuration. The feeder object must be first created using theFIMTServerAPI::FirewallCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the firewall configuration entry with a specified index to the config object.
