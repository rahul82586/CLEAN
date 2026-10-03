[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteDelete

[Previous](RouteAdd.md) | [Next](RouteShift.md)

# IMTServerAPI::RouteDelete

Delete a routing rule by the name.
    
    
    MTAPIRES  IMTServerAPI::RouteDelete(
       LPCWSTR  name      // Rule name
       )

### Parameters

**name**  
[in] The name of a routing rule (IMTConRoute::Name).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Routing rules can be deleted only from the plugins that run on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

# IMTServerAPI::RouteDelete

Delete a routing rule by the index.
    
    
    MTAPIRES  IMTServerAPI::RouteDelete(
       const UINT  pos      // Position of a rule
       )

### Parameters

**pos**  
[in] Position of a routing rule, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Routing rules can be deleted only from the plugins that run on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
