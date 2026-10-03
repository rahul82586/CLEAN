[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolExist

[Previous](SymbolGetLight.md) | [Next](../Managers.md)

# IMTReportAPI::SymbolExist

Check the availability of a symbol for a specified [group](../../../../Configuration-Interfaces/Groups.md) of clients.
    
    
    MTAPIRES  IMTReportAPI::SymbolExist(
       const IMTConSymbol*  symbol,     // An object of the symbol configuration
       const IMTConGroup*   group       // An object of the group configuration
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration.

**group**  
[in] An object of the group configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method checks whether the parameters of a client group allow working with a specified symbol.
