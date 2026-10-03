[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerNext

[Previous](NetServerTotal.md) | [Next](NetServerGet.md)

# IMTAdminAPI::NetServerNext

Get a server configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::NetServerNext(
       const UINT     pos,        // Position of the configuration
       IMTConServer*  config      // Configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NetServerNext(
       uint           pos,        // Position of the configuration
       CIMTConServer  config      // Configuration object
       )

Python
    
    
    AdminAPI.NetServerNext(
       pos            # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] The server configuration object. The config object must first be created using theIMTAdminAPI::NetServerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a server with a specified index to the config object.
