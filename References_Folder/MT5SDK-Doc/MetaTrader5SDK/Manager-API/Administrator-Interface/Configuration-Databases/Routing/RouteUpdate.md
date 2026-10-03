[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteUpdate

[Previous](RouteUnsubscribe.md) | [Next](RouteUpdateBatch.md)

# IMTAdminAPI::RouteUpdate

Add or update a routing rule.

C++
    
    
    MTAPIRES  IMTAdminAPI::RouteUpdate(
       IMTConRoute*  route      // An object of a routing rule
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.RouteUpdate(
       CIMTConRoute  route      // An object of a routing rule
       )

Python
    
    
    AdminAPI.RouteUpdate(
       route         # An object of a routing rule
       )

### Parameters

**route**  
[in] An object of a routing rule.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
