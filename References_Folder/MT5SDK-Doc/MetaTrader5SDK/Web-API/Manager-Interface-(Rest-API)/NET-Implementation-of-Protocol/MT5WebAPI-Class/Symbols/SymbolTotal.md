[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolTotal

[Previous](SymbolDelete.md) | [Next](SymbolNext.md)

# MT5WebAPI.SymbolTotal

Get the number of symbols created on the trade server.
    
    
    MTRetCode  MT5WebAPI.SymbolTotal(
       out int  total      // The number of symbols
       )

### Parameters

**total**  
[out] The number of symbols on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
