[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / GroupCreate

[Previous](CountryCreate.md) | [Next](Subscribe.md)

# IMTAdminAPI::KYCGroupCreate

Create an object of the account group for which the KYC provider will be used.

C++
    
    
    IMTConKYCGroup*  IMTAdminAPI::KYCGroupCreate()

.NET
    
    
    CIMTConKYCGroup  CIMTAdminAPI.KYCGroupCreate()

### Return Value

Returns a pointer to the created object implementing the [IMTConKYCGroup](../../../../Configuration-Interfaces/KYC/IMTConGroup.md) interface. Null is returned in case of failure.

### Note

The created object should be destroyed by calling the [IMTConKYCGroup::Release](../../../../Configuration-Interfaces/KYC/IMTConKYCGroup/IMTConGroup-Release.md) method of this object.
