[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayDelete

[Previous](GatewayUpdateBatch.md) | [Next](GatewayDeleteBatch.md)

# IMTAdminAPI::GatewayDelete

Delete a gateway configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayDelete(
       LPCWSTR  name      // Name of the configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayDelete(
       string   name      // Name of the configuration
       )

Python
    
    
    AdminAPI.GatewayDelete(
       name               # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

# IMTAdminAPI::GatewayDelete

Delete a gateway configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayDelete(
       const UINT  pos      // Position of the configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayDelete(
       uint        pos      // Position of the configuration
       )

Python
    
    
    AdminAPI.GatewayDelete(
       pos         # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
