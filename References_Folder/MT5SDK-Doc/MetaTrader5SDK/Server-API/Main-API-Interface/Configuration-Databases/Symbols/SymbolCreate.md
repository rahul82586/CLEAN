[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolCreate

[Previous](../Symbols.md) | [Next](SymbolSessionCreate.md)

# IMTServerAPI::SymbolCreate

Create an object of the symbol configuration.
    
    
    IMTConSymbol*  IMTServerAPI::SymbolCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConSymbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConSymbol::Release](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Release.md) method of this object.
