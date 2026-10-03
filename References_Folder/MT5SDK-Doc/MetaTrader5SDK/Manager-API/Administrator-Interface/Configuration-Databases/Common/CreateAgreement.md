[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / CreateAgreement

[Previous](CreateAllocation.md) | [Next](Subscribe.md)

# IMTAdminAPI::CommonCreate

Create an agreement object for an account allocation configuration.

C++
    
    
    IMTConAccountAgreement*  IMTAdminAPI::CommonCreate()

.NET
    
    
    CIMTConAccountAgreement  CIMTAdminAPI.CommonCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConAccountAgreement](../../../../Configuration-Interfaces/Common/IMTConAccountAgreement.md) interface. On failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConAccountAgreement::Release](../../../../Configuration-Interfaces/Common/IMTConAccountAgreement/Release.md) method of this object.
