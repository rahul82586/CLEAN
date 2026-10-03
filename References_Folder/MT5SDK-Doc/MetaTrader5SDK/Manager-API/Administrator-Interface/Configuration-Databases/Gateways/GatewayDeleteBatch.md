[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayDeleteBatch

[Previous](GatewayDelete.md) | [Next](GatewayShift.md)

# IMTAdminAPI::GatewayDeleteBatch

Delete multiple gateway configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayDeleteBatch(
       IMTConGateway**  configs,      // An array of configurations
       const UINT       config_total, // The number of configurations in the array
       MTAPIRES*        results       // An array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayDeleteBatch(
       CIMTConGateway[] configs,      // An array of configurations
       MTRetCode[]      results       // An array of results
       )

Python
    
    
    AdminAPI.GatewayDeleteBatch(
       configs          # An array of configurations
       )

### Parameters

**configs**  
[in] A pointer to an array of configurations which you want to delete.

**config_total**  
[in] The number of configurations in the 'configs' array.

**results**  
[out] An array with the results of deletion of each configuration on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned. The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code is an indication of successful sending of changes to a server; results of applying the changes are passed in the 'results' parameter.

### Further Note

A configuration can only be deleted from the applications that run on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the [MT_RET_ERR_PARAMS](../../../../Return-Codes/Common-errors.md) error code is added to the 'results' array of this object.
