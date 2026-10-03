[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolSessionCreate

[Previous](SymbolCreate.md) | [Next](SymbolTotal.md)

# IMTReportAPI::SymbolSessionCreate

Create an object of configuration of a trading or quoting session of the symbol.
    
    
    IMTConSymbolSession*  IMTReportAPI::SymbolSessionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConSymbolSession](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSession.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConSymbolSession::Release](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSession/Release.md) method of this object.
