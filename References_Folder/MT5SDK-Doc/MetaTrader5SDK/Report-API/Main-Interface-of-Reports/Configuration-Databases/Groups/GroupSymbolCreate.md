[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupSymbolCreate

[Previous](GroupCreate.md) | [Next](GroupCommissionCreate.md)

# IMTReportAPI::GroupSymbolCreate

Create an object of [symbol](../../../../Configuration-Interfaces/Symbols.md) configuration for a group.
    
    
    IMTConGroupSymbol*  IMTReportAPI::GroupSymbolCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGroupSymbol](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConGroupSymbol::Release](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/Release.md) method of this object.
