[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Create

[Previous](../KYC.md) | [Next](CountryCreate.md)

# IMTAdminAPI::KYCCreate

Create a KYC provider configuration object.

C++
    
    
    IMTConKYC*  IMTAdminAPI::KYCCreate()

.NET
    
    
    CIMTConKYC  CIMTAdminAPI.KYCCreate()

### Return Value

Returns a pointer to the created object implementing the [IMTConKYC](../../../../Configuration-Interfaces/KYC/IMTCon.md) interface. Null is returned in case of failure.

### Note

The created object should be destroyed by calling the [IMTConKYC::Release](../../../../Configuration-Interfaces/KYC/IMTConKYC/IMTCon-Release.md) method of this object.
