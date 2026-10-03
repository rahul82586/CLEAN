[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolGetGroup

[Previous](SymbolGet.md) | [Next](../Clients.md)

# MT5WebAPI.SymbolGetGroup

Get the configuration of a symbol for a group by the name of the symbol.
    
    
    MTRetCode  MT5WebAPI.SymbolGetGroup(
       string           name,       // Symbol name
       string           group,      // Group name
       out MTConSymbol  symbol      // Symbol configuration
       )

### Parameters

**name**  
[in] Symbol name.

**group**  
[in] The name of the group for which we get the symbol configuration.

**symbol**  
[out] The MTConSymbol structure that describes the symbol configuration. The structure parameters are described in section"Data Structure".

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
