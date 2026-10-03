[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupCreate

[Previous](../Groups.md) | [Next](GroupCreateArray.md)

# IMTManagerAPI::GroupCreate

Create an object of the group configuration.

C++
    
    
    IMTConGroup*  IMTManagerAPI::GroupCreate()

.NET
    
    
    CIMTConGroup  CIMTManagerAPI.GroupCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGroup](../../../../Configuration-Interfaces/Groups/IMTConGroup.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConGroup::Release](../../../../Configuration-Interfaces/Groups/IMTConGroup/Release.md) method of this object.
