[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolDelete

[Previous](SymbolUpdateBatch.md) | [Next](SymbolDeleteBatch.md)

# IMTAdminAPI::SymbolDelete

Delete a symbol configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolDelete(
       const UINT  pos      // Position of the configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolDelete(
       uint        pos      // Position of the configuration
       )

Python
    
    
    AdminAPI.SymbolDelete(
       int         pos      # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

# IMTAdminAPI::SymbolDelete

Delete a symbol configuration by the index or name.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolDelete(
       LPCWSTR  name      // Symbol name
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolDelete(
       string   name      // Symbol name
       )

Python
    
    
    AdminAPI.SymbolDelete(
       str      name      # Symbol name
       )

### Parameters

**name**  
[in] Symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
