[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Create

[Previous](../Common.md) | [Next](CreateAllocation.md)

# IMTServerAPI::CommonCreate

Create an object of the common platform configuration.
    
    
    IMTConCommon*  IMTServerAPI::CommonCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConCommon](../../../../Configuration-Interfaces/Common/IMTCon.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConCommon::Release](../../../../Configuration-Interfaces/Common/IMTConCommon/IMTCon-Release.md) method of this object.
