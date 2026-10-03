[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGroupExist

[Previous](SymbolGroupNext.md) | [Next](../Spreads.md)

# IMTAdminAPI::SymbolGroupExist

Check the presence of a subgroup of symbols on the trading server.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolGroupExist(
       LPCWSTR  name      // the name of the subgroup of symbols
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolGroupExist(
       string   name      // the name of the subgroup of symbols
       )

Python
    
    
    AdminAPI.SymbolGroupExist(
       str      name      # the name of the subgroup of symbols
       )

### Parameters

**name**  
[in] The name of the symbol subgroup.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
