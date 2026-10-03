[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolGet

[Previous](SymbolNext.md) | [Next](SymbolGetGroup.md)

# MT5WebAPI.SymbolGet

Get the symbol configuration by its name.
    
    
    MTRetCode  MT5WebAPI.SymbolGet(
       string           name,       // Symbol name
       out MTConSymbol  symbol      // Symbol configuration
       )

### Parameters

**name**  
[in] Symbol name.

**symbol**  
[out] The MTConSymbol structure that describes the symbol configuration. The structure parameters are described in section"Data Structure".

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
