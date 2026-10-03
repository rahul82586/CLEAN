[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolSessionCreate

[Previous](SymbolCreate.md) | [Next](SymbolSubscribe.md)

# IMTAdminAPI::SymbolSessionCreate

Create an object of configuration of a trading or quoting session of the symbol.

C++
    
    
    IMTConSymbolSession*  IMTAdminAPI::SymbolSessionCreate()

.NET
    
    
    CIMTConSymbolSession  CIMTAdminAPI.SymbolSessionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConSymbolSession](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSession.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConSymbolSession::Release](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSession/Release.md) method of this object.
