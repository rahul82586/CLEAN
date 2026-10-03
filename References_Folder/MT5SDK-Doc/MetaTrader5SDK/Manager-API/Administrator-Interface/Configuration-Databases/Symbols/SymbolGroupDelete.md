[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGroupDelete

[Previous](SymbolGroupAdd.md) | [Next](SymbolGroupShift.md)

# IMTAdminAPI::SymbolGroupDelete

Remove a subgroup of symbols by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolGroupDelete(
       LPCWSTR  name      // the name of the subgroup of symbols
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolGroupDelete(
       string   name      // the name of the subgroup of symbols
       )

Python
    
    
    AdminAPI.SymbolGroupDelete(
       str      name      # the name of the symbol subgroup
       )

### Parameters

**name**  
[in] The name of the symbol subgroup.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The subgroup is deleted along with all the symbols it contains.
