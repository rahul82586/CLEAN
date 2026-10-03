[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / CreateAgreement

[Previous](CreateAllocation.md) | [Next](Subscribe.md)

# IMTServerAPI::CommonCreate

Create an agreement object for an account allocation configuration.
    
    
    IMTConAccountAgreement*  IMTServerAPI::CommonCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConAccountAgreement](../../../../Configuration-Interfaces/Common/IMTConAccountAgreement.md) interface. On failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConAccountAgreement::Release](../../../../Configuration-Interfaces/Common/IMTConAccountAgreement/Release.md) method of this object.
