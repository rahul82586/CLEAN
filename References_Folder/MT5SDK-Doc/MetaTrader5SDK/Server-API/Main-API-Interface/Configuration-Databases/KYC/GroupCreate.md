[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / GroupCreate

[Previous](CountryCreate.md) | [Next](Subscribe.md)

# IMTServerAPI::KYCGroupCreate

Create an object of an account group for which the messenger will be used.
    
    
    IMTConKYCGroup*  IMTServerAPI::KYCGroupCreate()

### Return Value

Returns a pointer to the created object implementing the [IMTConKYCGroup](../../../../Configuration-Interfaces/KYC/IMTConGroup.md) interface. Null is returned in case of failure.

### Note

The created object should be destroyed by calling the [IMTConKYCGroup::Release](../../../../Configuration-Interfaces/KYC/IMTConKYCGroup/IMTConGroup-Release.md) method of this object.
