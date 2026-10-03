[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolTotal

[Previous](SymbolDelete.md) | [Next](SymbolNext.md)

# MTWebAPI::SymbolTotal

Get the number of symbols created on the trade server.
    
    
    MTAPIRES  MTWebAPI::SymbolTotal(
       int  &$total      // Number of symbols
       )

### Parameters

**& $total**  
[out] The number of symbols on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
