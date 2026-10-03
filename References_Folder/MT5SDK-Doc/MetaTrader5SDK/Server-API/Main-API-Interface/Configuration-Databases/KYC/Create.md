[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Create

[Previous](../KYC.md) | [Next](CountryCreate.md)

# IMTServerAPI::KYCCreate

Create a KYC provider configuration object.
    
    
    IMTConKYC*  IMTServerAPI::KYCCreate()

### Return Value

Returns a pointer to the created object implementing the [IMTConKYC](../../../../Configuration-Interfaces/KYC/IMTCon.md) interface. Null is returned in case of failure.

### Note

The created object should be destroyed by calling the [IMTConKYC::Release](../../../../Configuration-Interfaces/KYC/IMTConKYC/IMTCon-Release.md) method of this object.
