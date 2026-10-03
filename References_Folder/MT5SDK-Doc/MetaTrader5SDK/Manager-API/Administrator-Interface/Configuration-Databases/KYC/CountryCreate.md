[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / CountryCreate

[Previous](Create.md) | [Next](GroupCreate.md)

# IMTAdminAPI::KYCCountryCreate

Create an object of a country for which the messenger will be used.

C++
    
    
    IMTConKYCCountry*  IMTAdminAPI::KYCCountryCreate()

.NET
    
    
    CIMTConKYCCountry  CIMTAdminAPI.KYCCountryCreate()

### Return Value

Returns a pointer to the created object implementing the [IMTConKYCCountry](../../../../Configuration-Interfaces/KYC/IMTConCountry.md) interface. Null is returned in case of failure.

### Note

The created object should be destroyed by calling the [IMTConKYCCountry::Release](../../../../Configuration-Interfaces/KYC/IMTConKYCCountry/IMTConCountry-Release.md) method of this object.
