[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / CreateGroup

[Previous](CreateCondition.md) | [Next](Subscribe.md)

# IMTServerAPI::VPSCreateGroup

Create an entry object in the list of groups for which the Sponsored VPS is allowed.
    
    
    IMTConVPS*  IMTServerAPI::VPSCreateGroup()

### Return Value

It returns a pointer to the created object that implements the [IMTConVPSGroup](../../../../Configuration-Interfaces/VPS/IMTConGroup.md) interface. In case of failure, it returns NULL.

### Note

The created object should be destroyed by calling the [IMTConVPSGroup::Release](../../../../Configuration-Interfaces/VPS/IMTConVPSGroup/IMTConGroup-Release.md) method of this object.
