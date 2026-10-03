[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / CreateAllocation

[Previous](Create.md) | [Next](CreateAgreement.md)

# IMTServerAPI::CommonCreateAllocation

Create an account allocation configuration object.
    
    
    IMTConAccountAllocation*  IMTServerAPI::CommonCreateAllocation()

### Return Value

Returns a pointer to the created object that implements the [IMTConAccountAllocation](../../../../Configuration-Interfaces/Common/IMTConAccountAllocation.md) interface. On failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConAccountAllocation::Release](../../../../Configuration-Interfaces/Common/IMTConAccountAllocation/Release.md) method of this object.
