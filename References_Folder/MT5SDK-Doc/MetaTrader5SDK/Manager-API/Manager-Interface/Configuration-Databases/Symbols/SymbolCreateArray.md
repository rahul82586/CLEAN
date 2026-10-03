[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolCreateArray

[Previous](SymbolCreate.md) | [Next](SymbolSessionCreate.md)

# IMTManagerAPI::SymbolCreateArray

Create a symbols array object.

C++
    
    
    IMTConSymbolArray*  IMTManagerAPI::SymbolCreateArray()

.NET
    
    
    CIMTConSymbolArray  CIMTManagerAPI.SymbolCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTConSymbolArray](../../../../Configuration-Interfaces/Symbols/IMTConSymbolArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConSymbolArray::Release](../../../../Configuration-Interfaces/Symbols/IMTConSymbolArray/Release.md) method of this object.
