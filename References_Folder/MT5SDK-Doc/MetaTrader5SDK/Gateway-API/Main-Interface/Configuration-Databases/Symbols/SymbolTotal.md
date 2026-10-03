[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolTotal

[Previous](SymbolDelete.md) | [Next](SymbolNext.md)

# IMTGatewayAPI::SymbolTotal

Get the number of the symbols configurations avaialble for a gateway or a data feed.

C++
    
    
    UINT  IMTGatewayAPI::SymbolTotal()

.NET
    
    
    uint  CIMTGatewayAPI.SymbolTotal()

### Return Value

The number of configurations, 

### Note

Available symbols are specified in the "Symbols" tab of a gateway in MetaTrader 5 Administrator. The list does not include the symbols, for which sending of quotes from the gateway is useless:

  * Symbols with the filled [IMTConSymbol::Source](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Source.md) field. Quotes for such symbols are always provided by the source symbol.
  * Symbols with the disabled [IMTConSymbol::EnTickFlags::TICK_REALTIME (#entickflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entickflags) flag. The platform does not receive quotes from gateways and datafeeds for such symbols.


