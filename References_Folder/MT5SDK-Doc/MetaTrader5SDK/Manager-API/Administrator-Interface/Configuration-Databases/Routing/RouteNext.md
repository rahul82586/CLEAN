[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteNext

[Previous](RouteTotal.md) | [Next](RouteGet.md)

# IMTAdminAPI::RouteNext

Get a routing rule by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::RouteNext(
       const UINT    pos,       // Position of a rule
       IMTConRoute*  route      // An object of a routing rule
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.RouteNext(
       uint          pos,       // Position of a rule
       CIMTConRoute  route      // An object of a routing rule
       )

Python
    
    
    AdminAPI.RouteNext(
       pos           # Position of a rule
       )

### Parameters

**pos**  
[in] Position of a routing rule, starting with 0.

**route**  
[out] An object of a routing rule. The route object must be first created using theIMTAdminAPI::RouteCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the parameters of a routing rule with a specified index to the route object.
