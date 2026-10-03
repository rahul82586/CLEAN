[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolTotal

[Previous](SymbolUpdateBatch.md) | [Next](SymbolNext.md)

# IMTManagerAPI::SymbolTotal

The total number of symbol configurations available in the platform.

C++
    
    
    UINT  IMTManagerAPI::SymbolTotal()

.NET
    
    
    uint  CIMTManagerAPI.SymbolTotal()

Python
    
    
    ManagerAPI.SymbolTotal()

### Return Value

The number of symbol configurations in the trading platform.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_SYMBOLS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
