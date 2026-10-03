[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / Create

[Previous](../VPS.md) | [Next](CreateRule.md)

# IMTServerAPI::VPSCreate

Create the VPS sponsorship settings object.
    
    
    IMTConVPS*  IMTServerAPI::VPSCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConVPS](../../../../Configuration-Interfaces/VPS/IMTCon.md) interface. In case of failure, it returns NULL.

### Note

The created object should be destroyed by calling the [IMTConVPS::Release](../../../../Configuration-Interfaces/VPS/IMTConVPS/IMTCon-Release.md) method of this object.
