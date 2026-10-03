[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgDelete

[Previous](SubscriptionCfgUpdateBatch.md) | [Next](SubscriptionCfgDeleteByID.md)

# IMTAdminAPI::SubscriptionCfgDelete

Delete a subscription configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgDelete(
       LPCWSTR  name      // Configuration name
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgDelete(
       string   name      // Configuration name
       )

### Parameters

**name**  
[in] The name of the configuration to delete. TheIMTConSubscription::Namevalue is used for the configuration name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can only be deleted from the applications that run on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

# IMTAdminAPI::SubscriptionCfgDelete

Delete a subscription configuration by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgDelete(
       const UINT  pos      // Configuration position
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgDelete(
       uint        pos      // Configuration position
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can only be deleted from the applications that run on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
