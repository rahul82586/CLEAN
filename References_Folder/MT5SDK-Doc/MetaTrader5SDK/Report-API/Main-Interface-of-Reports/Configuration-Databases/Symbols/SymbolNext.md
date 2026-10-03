[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](SymbolGet.md)

# IMTReportAPI::SymbolNext

Get the symbol configuration by the index.
    
    
    MTAPIRES  IMTReportAPI::SymbolNext(
       const UINT     pos,        // Position of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTReportAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a symbol with a specified index to the symbol object.
