[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupSymbolCreate

[Previous](GroupCreate.md) | [Next](GroupCommissionCreate.md)

# IMTAdminAPI::GroupSymbolCreate

Create an object of [symbol](../Symbols.md) configuration for a group.

C++
    
    
    IMTConGroupSymbol*  IMTAdminAPI::GroupSymbolCreate()

.NET
    
    
    CIMTConGroupSymbol  CIMTAdminAPI.GroupSymbolCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGroupSymbol](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConGroupSymbol::Release](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/Release.md) method of this object.
