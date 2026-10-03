[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolCreate

[Previous](../Symbols.md) | [Next](SymbolCreateArray.md)

# IMTManagerAPI::SymbolCreate

Create an object of the symbol configuration.

C++
    
    
    IMTConSymbol*  IMTManagerAPI::SymbolCreate()

.NET
    
    
    CIMTConSymbol  CIMTManagerAPI.SymbolCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConSymbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConSymbol::Release](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Release.md) method of this object.
