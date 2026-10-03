[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolGet

[Previous](SymbolNext.md) | [Next](SymbolGetGroup.md)

# MTWebAPI::SymbolGet

Get the symbol configuration by its name.
    
    
    MTAPIRES  MTWebAPI::SymbolGet(
       string       $name,        // Symbol name
       MTConSymbol  &$symbol      // Symbol configuration
       )

### Parameters

**$name**  
[in] Symbol name.

**& $symbol**  
[out] The MTConSymbol structure that describes the symbol configuration. The structure parameters are described in section"Data Structure".

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The string specifying the group name must be passed in the UTF-8 format.
