[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / CreateGroup

[Previous](CreateCondition.md) | [Next](Subscribe.md)

# IMTAdminAPI::VPSCreateGroup

Create an entry object in the list of groups for which the Sponsored VPS is allowed.

C++
    
    
    IMTConVPS*  IMTAdminAPI::VPSCreateGroup()

.NET
    
    
    CIMTConVPS  CIMTAdminAPI.VPSCreateGroup()

### Return Value

It returns a pointer to the created object that implements the [IMTConVPSGroup](../../../../Configuration-Interfaces/VPS/IMTConGroup.md) interface. In case of failure, it returns NULL.

### Note

The created object should be destroyed by calling the [IMTConVPSGroup::Release](../../../../Configuration-Interfaces/VPS/IMTConVPSGroup/IMTConGroup-Release.md) method of this object.
