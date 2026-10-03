[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolRequest

[Previous](SymbolGet.md) | [Next](SymbolRequestArray.md)

# IMTManagerAPI::SymbolRequest

Request a symbol configuration from a server by the name.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolRequest(
       LPCWSTR        name,       // Symbol name
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolRequest(
       string         name,       // Symbol name
       CIMTConSymbol  obj         // An object of the symbol configuration
       )

Python
    
    
    ManagerAPI.SymbolRequest(
       name           # Symbol name
       )

### Parameters

**name**  
[in] Symbol name.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTManagerAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConSymbol::Symbol()](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the name. This method returns a symbol configuration with default trade settings.

# IMTManagerAPI::SymbolRequest

Request from a server an individual configuration of a symbol for a group by the name of the symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolRequest(
       LPCWSTR        name,       // Symbol name
       LPCWSTR        group,      // Group name
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolRequest(
       string         name,       // Symbol name
       string         group,      // Group name
       CIMTConSymbol  symbol      // An object of the symbol configuration
       )

Python
    
    
    ManagerAPI.SymbolRequest(
       name,          # Symbol name
       group          # Group name
       )

### Parameters

**name**  
[in] Symbol name.

**group**  
[in] Group name.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTManagerAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConSymbol::Symbol()](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name, [IMTConGroup::Group()](../../../../Configuration-Interfaces/Groups/IMTConGroup/Group.md) \- as the group name.
