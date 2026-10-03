[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolSessionCreate

[Previous](SymbolCreateArray.md) | [Next](SymbolSubscribe.md)

# IMTManagerAPI::SymbolSessionCreate

Create an object of configuration of a trading or quoting session of the symbol.

C++
    
    
    IMTConSymbolSession*  IMTManagerAPI::SymbolSessionCreate()

.NET
    
    
    CIMTConSymbolSession  CIMTManagerAPI.SymbolSessionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConSymbolSession](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSession.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTManagerAPI::Release](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSession/Release.md) method of this object.
