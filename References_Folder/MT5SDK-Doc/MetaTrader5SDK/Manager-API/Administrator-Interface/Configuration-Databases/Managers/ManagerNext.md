[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerNext

[Previous](ManagerTotal.md) | [Next](ManagerGet.md)

# IMTAdminAPI::ManagerNext

Gets a manager configuration with the specified index.

C++
    
    
    MTAPIRES  IMTAdminAPI::ManagerNext(
       const UINT      pos,         // Position of the configuration
       IMTConManager*  manager      // An object of manager configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ManagerNext(
       uint            pos,         // Position of the configuration
       CIMTConManager  manager      // An object of manager configuration
       )

Python
    
    
    AdminAPI.ManagerNext(
       pos             # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**manager**  
[out] An object of manager configuration. The manager object must be first created using theIMTAdminAPI::ManagerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a manager with a specified index to the manager object.
