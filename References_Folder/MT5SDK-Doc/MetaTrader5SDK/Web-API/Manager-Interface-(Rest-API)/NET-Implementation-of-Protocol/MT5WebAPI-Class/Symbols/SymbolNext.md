[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](SymbolGet.md)

# MT5WebAPI.SymbolNext

Get the configuration of a symbol by its index in the list of symbols of the platform.
    
    
    MTRetCode  MT5WebAPI.SymbolNext(
       int              pos,        // Symbol position
       out MTConSymbol  symbol      // Symbol configuration
       )

### Parameters

**pos**  
[in] Position of the symbol, starting with 0.

**symbol**  
[out] The MTConSymbol structure that describes the symbol configuration. The structure parameters are described in section"Data Structure".

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
