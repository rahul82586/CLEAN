[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / CreateRule

[Previous](Create.md) | [Next](CreateCondition.md)

# IMTServerAPI::VPSCreateRule

Create a VPS allocation rule object.
    
    
    IMTConVPSRule*  IMTServerAPI::VPSCreateRule()

### Return Value

The method returns a pointer to the created object that implements the [IMTConVPSRule](../../../../Configuration-Interfaces/VPS/IMTConRule.md) interface. NULL is returned on failure.

### Note

The created object must be destroyed by calling the [IMTConVPSRule::Release](../../../../Configuration-Interfaces/VPS/IMTConVPSRule/IMTConRule-Release.md) method of this object.
