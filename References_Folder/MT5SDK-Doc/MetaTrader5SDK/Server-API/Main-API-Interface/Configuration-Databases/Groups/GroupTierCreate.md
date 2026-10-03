[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupTierCreate

[Previous](GroupCommissionCreate.md) | [Next](GroupSubscribe.md)

# IMTServerAPI::GroupTierCreate

Create an object of commission range configuration for a group.
    
    
    IMTConCommTier*  IMTServerAPI::GroupTierCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConCommTier](../../../../Configuration-Interfaces/Groups/IMTConCommTier.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConCommTier::Release](../../../../Configuration-Interfaces/Groups/IMTConCommTier/Release.md) method of this object.
