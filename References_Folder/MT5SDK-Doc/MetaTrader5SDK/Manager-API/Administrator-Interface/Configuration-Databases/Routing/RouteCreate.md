[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteCreate

[Previous](../Routing.md) | [Next](RouteConditionCreate.md)

# IMTAdminAPI::RouteCreate

Create an object of a routing rule.

C++
    
    
    IMTConRoute*  IMTAdminAPI::RouteCreate()

.NET
    
    
    CIMTConRoute  CIMTAdminAPI.RouteCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConRoute](../../../../Configuration-Interfaces/Routing/IMTConRoute.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConRoute::Release](../../../../Configuration-Interfaces/Routing/IMTConRoute/Release.md) method of this object.
