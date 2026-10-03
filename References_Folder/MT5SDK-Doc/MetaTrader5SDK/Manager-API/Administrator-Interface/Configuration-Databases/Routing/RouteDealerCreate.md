[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteDealerCreate

[Previous](RouteConditionCreate.md) | [Next](RouteSubscribe.md)

# IMTAdminAPI::RouteDealerCreate

Create an object of a dealer configuration to whom requests under this rule will be sent.

C++
    
    
    IMTConRouteDealer*  IMTAdminAPI::RouteDealerCreate()

.NET
    
    
    CIMTConRouteDealer  CIMTAdminAPI.RouteDealerCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConRouteDealer](../../../../Configuration-Interfaces/Routing/IMTConRouteDealer.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConRouteDealer::Release](../../../../Configuration-Interfaces/Routing/IMTConRouteDealer/Release.md) method of this object.
