[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / CreateCondition

[Previous](CreateRule.md) | [Next](CreateGroup.md)

# IMTServerAPI::VPSCreateCondition

Create a condition object for the VPS allocation rule.
    
    
    IMTConVPSCondition*  IMTServerAPI::VPSCreateCondition()

### Return Value

The method returns a pointer to the created object that implements the [IMTConVPSCondition](../../../../Configuration-Interfaces/VPS/IMTConCondition.md) interface. NULL is returned on failure.

### Note

The created object must be destroyed by calling the [IMTConVPSCondition::Release](../../../../Configuration-Interfaces/VPS/IMTConVPSCondition/IMTConCondition-Release.md) method of this object.
