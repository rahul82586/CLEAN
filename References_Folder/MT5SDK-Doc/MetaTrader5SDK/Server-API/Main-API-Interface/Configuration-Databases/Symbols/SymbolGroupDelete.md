[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGroupDelete

[Previous](SymbolGroupAdd.md) | [Next](SymbolGroupShift.md)

# IMTServerAPI::SymbolGroupDelete

Delete a subgroup of symbols by name.
    
    
    MTAPIRES  IMTServerAPI::SymbolGroupDelete(
       LPCWSTR  name      // the name of the symbol subgroup
       )

### Parameters

**name**  
[in] The name of the subgroup of symbols, with the path.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A subgroup is deleted along with all the symbols it contains.
