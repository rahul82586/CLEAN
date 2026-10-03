[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolExist

[Previous](SymbolGet.md) | [Next](SymbolGroupAdd.md)

# IMTAdminAPI::SymbolExist

Check the availability of a symbol for a specified [group](../../../../Configuration-Interfaces/Groups.md) of clients.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolExist(
       const IMTConSymbol*  symbol,     // An object of the symbol configuration
       const IMTConGroup*   group       // An object of the group configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolExist(
       CIMTConSymbol        symbol,     // An object of the symbol configuration
       CIMTConGroup         group       // An object of the group configuration
       )

Python
    
    
    AdminAPI.SymbolExist(
       symbol,              # An object of the symbol configuration
       group                # object of the group configuration
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration.

**group**  
[in] An object of the group configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method checks whether the parameters of a client group allow working with a specified symbol.
