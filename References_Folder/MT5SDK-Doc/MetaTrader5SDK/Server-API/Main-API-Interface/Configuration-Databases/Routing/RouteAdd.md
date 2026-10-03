[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteAdd

[Previous](RouteUnsubscribe.md) | [Next](RouteDelete.md)

# IMTServerAPI::RouteAdd

Add or update a routing rule.
    
    
    MTAPIRES  IMTServerAPI::RouteAdd(
       IMTConRoute*  route      // An object of a routing rule
       )

### Parameters

**route**  
[in] An object of a routing rule.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the rule name [IMTConRoute::Name()](../../../../Configuration-Interfaces/Routing/IMTConRoute/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConRouteSink::OnRouteUpdate](../../../../Configuration-Interfaces/Routing/IMTConRouteSink/OnRouteUpdate.md) notification method is not called.
