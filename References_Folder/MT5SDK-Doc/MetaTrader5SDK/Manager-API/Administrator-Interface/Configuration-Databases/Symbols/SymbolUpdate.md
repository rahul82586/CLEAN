[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolUpdate

[Previous](SymbolUnsubscribe.md) | [Next](SymbolUpdateBatch.md)

# IMTAdminAPI::SymbolUpdate

Add or update a symbol configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolUpdate(
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolUpdate(
       CIMTConSymbol  symbol      // An object of the symbol configuration
       )

Python
    
    
    AdminAPI.SymbolUpdate(
       symbol         # An object of the symbol configuration
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
