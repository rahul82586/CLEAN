[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteNext

[Previous](RouteTotal.md) | [Next](RouteGet.md)

# IMTServerAPI::RouteNext

Get a routing rule by the index.
    
    
    MTAPIRES  IMTServerAPI::RouteNext(
       const UINT    pos,       // Position of a rule
       IMTConRoute*  route      // An object of a routing rule
       )

### Parameters

**pos**  
[in] Position of a routing rule, starting with 0.

**route**  
[out] An object of a routing rule. The route object must be first created using theIMTServerAPI::RouteCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the parameters of a routing rule with a specified index to the route object.
