[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteGet

[Previous](RouteNext.md) | [Next](../Reports.md)

# IMTAdminAPI::RouteGet

Get a routing rule by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::RouteGet(
       LPCWSTR       name,      // Rule name
       IMTConRoute*  route      // An object of a routing rule
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.RouteGet(
       string        name,      // Rule name
       CIMTConRoute  route      // An object of a routing rule
       )

Python
    
    
    AdminAPI.RouteGet(
       name          # Rule name
       )

### Parameters

**name**  
[in] The name of a routing rule.

**route**  
[out] An object of a routing rule. The route object must be first created using theIMTAdminAPI::RouteCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConRoute::Name()](../../../../Configuration-Interfaces/Routing/IMTConRoute/Name.md) value is used as the name.
