[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGet

[Previous](SymbolNext.md) | [Next](SymbolExist.md)

# IMTAdminAPI::SymbolGet

Gets the symbol configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolGet(
       LPCWSTR        name,       // Name of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolGet(
       string         name,       // Name of the configuration
       CIMTConSymbol  symbol      // An object of the symbol configuration
       )

Python
    
    
    AdminAPI.SymbolGet(
       str            name        # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTAdminAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConSymbol::Symbol()](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the name. This method returns a symbol configuration with default trade settings.
