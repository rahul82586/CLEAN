[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteConditionCreate

[Previous](RouteCreate.md) | [Next](RouteDealerCreate.md)

# IMTAdminAPI::RouteConditionCreate

Create an object of an additional condition to apply a rule.
    
    
    IMTConCondition*  IMTAdminAPI::RouteConditionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConCondition](../../../../Configuration-Interfaces/Routing/IMTConCondition.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConCondition::Release](../../../../Configuration-Interfaces/Routing/IMTConCondition/Release.md) method of this object.
