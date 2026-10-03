[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGroupNext

[Previous](SymbolGroupTotal.md) | [Next](SymbolGroupExist.md)

# IMTServerAPI::SymbolGroupNext

Get the name of a subgroup of symbols by index.
    
    
    MTAPIRES  IMTServerAPI::SymbolGroupNext(
       const UINT     pos,        // position of symbol subgroup
       MTAPISTR&      name        // name of the symbol subgroup
       )

### Parameters

**pos**  
[in] The position of the symbol subgroup starting from 0.

**name**  
[out] The name of the symbol subgroup, including the path.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
