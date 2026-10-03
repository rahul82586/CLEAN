[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](SymbolGet.md)

# IMTServerAPI::SymbolNext

Get the symbol configuration by the index.
    
    
    MTAPIRES  IMTServerAPI::SymbolNext(
       const UINT     pos,        // Position of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTServerAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a symbol with a specified index to the symbol object.
