[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupSymbolCreate

[Previous](GroupCreateArray.md) | [Next](GroupCommissionCreate.md)

# IMTManagerAPI::GroupSymbolCreate

Create an object of [symbol](../../../../Configuration-Interfaces/Symbols.md) configuration for a group.

C++
    
    
    IMTConGroupSymbol*  IMTManagerAPI::GroupSymbolCreate()

.NET
    
    
    CIMTConGroupSymbol  CIMTManagerAPI.GroupSymbolCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGroupSymbol](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConGroupSymbol::Release](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/Release.md) method of this object.
