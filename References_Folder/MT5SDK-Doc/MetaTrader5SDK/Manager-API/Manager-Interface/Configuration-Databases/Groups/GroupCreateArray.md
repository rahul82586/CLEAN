[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupCreateArray

[Previous](GroupCreate.md) | [Next](GroupSymbolCreate.md)

# IMTManagerAPI::GroupCreateArray

Create a groups array object.

C++
    
    
    IMTConGroupArray*  IMTManagerAPI::GroupCreateArray()

.NET
    
    
    CIMTConGroupArray  CIMTManagerAPI.GroupCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTConGroupArray](../../../../Configuration-Interfaces/Groups/IMTConGroupArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConGroupArray::Release](../../../../Configuration-Interfaces/Groups/IMTConGroupArray/Release.md) method of this object.
