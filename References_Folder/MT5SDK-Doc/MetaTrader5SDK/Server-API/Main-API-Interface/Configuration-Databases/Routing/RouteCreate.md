[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteCreate

[Previous](../Routing.md) | [Next](RouteConditionCreate.md)

# IMTServerAPI::RouteCreate

Create an object of a routing rule.
    
    
    IMTConRoute*  IMTServerAPI::RouteCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConRoute](../../../../Configuration-Interfaces/Routing/IMTConRoute.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConRoute::Release](../../../../Configuration-Interfaces/Routing/IMTConRoute/Release.md) method of this object.
