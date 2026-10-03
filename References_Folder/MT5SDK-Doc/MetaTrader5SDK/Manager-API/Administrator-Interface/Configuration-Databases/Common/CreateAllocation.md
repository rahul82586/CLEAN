[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / CreateAllocation

[Previous](Create.md) | [Next](CreateAgreement.md)

# IMTAdminAPI::CommonCreateAllocation

Create an account allocation configuration object.

C++
    
    
    IMTConAccountAllocation*  IMTAdminAPI::CommonCreateAllocation()

.NET
    
    
    CIMTConAccountAllocation  CIMTAdminAPI.CommonCreateAllocation()

### Return Value

Returns a pointer to the created object that implements the [IMTConAccountAllocation](../../../../Configuration-Interfaces/Common/IMTConAccountAllocation.md) interface. On failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConAccountAllocation::Release](../../../../Configuration-Interfaces/Common/IMTConAccountAllocation/Release.md) method of this object.
