[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgDelete

[Previous](SubscriptionCfgAdd.md) | [Next](SubscriptionCfgDeleteByID.md)

# IMTServerAPI::SubscriptionCfgDelete

Delete a subscription configuration by name.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionCfgDelete(
       LPCWSTR  name      // Configuration name
       )

### Parameters

**name**  
[in] The name of the configuration to delete. TheIMTConSubscription::Namevalue is used for the configuration name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

# IMTServerAPI::SubscriptionCfgDelete

Delete a subscription configuration by index.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionCfgDelete(
       const UINT  pos      // Configuration position
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
