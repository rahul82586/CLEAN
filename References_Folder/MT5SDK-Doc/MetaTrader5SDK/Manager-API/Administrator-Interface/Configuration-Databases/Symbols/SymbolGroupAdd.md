[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGroupAdd

[Previous](SymbolExist.md) | [Next](SymbolGroupDelete.md)

# IMTAdminAPI::SymbolGroupAdd

Add a subgroup of symbols.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolGroupAdd(
       LPCWSTR  name      // the name of the symbol subgroup
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolGroupAdd(
       string   name      // the name of the symbol subgroup
       )

Python
    
    
    AdminAPI.SymbolGroupAdd(
       str      name      # the name of the symbol subgroup
       )

### Parameters

**name**  
[in] The name of the subgroup of symbols, with the path.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A subgroup can only be added from applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
