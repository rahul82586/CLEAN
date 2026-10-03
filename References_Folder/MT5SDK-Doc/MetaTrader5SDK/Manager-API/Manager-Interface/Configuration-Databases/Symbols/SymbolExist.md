[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolExist

[Previous](SymbolRequestArray.md) | [Next](../Floating-Margin.md)

# IMTManagerAPI::SymbolExist

Check the availability of a symbol for a specified [group](../../../../Configuration-Interfaces/Groups.md) of clients.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolExist(
       const IMTConSymbol*  symbol,     // An object of the symbol configuration
       const IMTConGroup*   group       // An object of the group configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolExist(
       CIMTConSymbol        symbol,     // An object of the symbol configuration
       CIMTConGroup         group       // An object of the group configuration
       )

Python
    
    
    ManagerAPI.SymbolExist(
       symbol,              # An object of the symbol configuration
       group                # An object of the group configuration
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
