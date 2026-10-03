[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](SymbolGet.md)

# IMTAdminAPI::SymbolNext

Get the symbol configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolNext(
       const UINT     pos,        // Position of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolNext(
       uint           pos,        // Position of the configuration
       CIMTConSymbol  symbol      // An object of the symbol configuration
       )

Python
    
    
    AdminAPI.SymbolNext(
       pos,           # Position of the configuration
       symbol         # An object of the symbol configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTAdminAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a symbol with a specified index to the symbol object.
