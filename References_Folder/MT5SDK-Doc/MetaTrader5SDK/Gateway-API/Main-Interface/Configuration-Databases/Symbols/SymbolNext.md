[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](SymbolGet.md)

# IMTGatewayAPI::SymbolNext

Get the symbol configuration by the index.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SymbolNext(
       const UINT     pos,        // Position of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SymbolNext(
       uint           pos,        // Position of the configuration
       CIMTConSymbol  symbol      // An object of the symbol configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTGatewayAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies the configuration data of a symbol with a specified index to the symbol object.

  * Symbols with the filled [IMTConSymbol::Source](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Source.md) field. Quotes for such symbols are always provided by the source symbol.
  * Symbols with the disabled [IMTConSymbol::EnTickFlags::TICK_REALTIME (#entickflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entickflags) flag. The platform does not receive quotes from gateways and datafeeds for such symbols.


