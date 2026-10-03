[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGroupExist

[Previous](SymbolGroupNext.md) | [Next](../Spreads.md)

# IMTServerAPI::SymbolGroupExist

Check the presence of a subgroup of symbols on the trading server.
    
    
    MTAPIRES  IMTServerAPI::SymbolGroupExist(
       LPCWSTR  name      // the name of the symbol subgroup
       )

### Parameters

**name**  
[in] The name of the subgroup of symbols, with the path.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
