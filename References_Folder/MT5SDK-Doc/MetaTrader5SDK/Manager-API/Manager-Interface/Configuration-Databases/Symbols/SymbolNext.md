[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](SymbolGet.md)

# IMTManagerAPI::SymbolNext

Get the symbol configuration by the index.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolNext(
       const UINT     pos,        // Position of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolNext(
       uint           pos,        // Position of the configuration
       CIMTConSymbol  obj         // An object of the symbol configuration
       )

Python
    
    
    ManagerAPI.SymbolNext(
       int            pos         # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTManagerAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a symbol with a specified index to the symbol object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_SYMBOLS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
