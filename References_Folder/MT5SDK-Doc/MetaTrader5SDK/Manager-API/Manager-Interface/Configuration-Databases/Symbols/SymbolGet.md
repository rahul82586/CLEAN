[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGet

[Previous](SymbolNext.md) | [Next](SymbolRequest.md)

<a id="group"></a>
# IMTManagerAPI::SymbolGet (#group)

Gets the symbol configuration by the name.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolGet(
       LPCWSTR        name,       // Name of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolGet(
       string         name,       // Name of the configuration
       CIMTConSymbol  obj         // An object of the symbol configuration
       )

Python
    
    
    ManagerAPI.SymbolGet(
       str            name        # Name of the configuration
       )

<a id="parameters"></a>
### Parameters (#parameters)

**name**  
[in] The name of the configuration.TheIMTConSymbol::Symbolvalue is used as the name..

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTManagerAPI::SymbolCreatemethod.

<a id="return-value"></a>
### Return Value (#return-value)

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

<a id="note"></a>
### Note (#note)

This method returns a symbol configuration with default trade settings. The method is valid only if the [IMTManagerAPI::PUMP_MODE_SYMBOLS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.

<a id="group"></a>
# IMTManagerAPI::SymbolGet (#group)

Get symbol settings taking into account that they are overridden for the specified group.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolGet(
       LPCWSTR             name,       // Name of the configuration
       LPCWSTR             group,      // Group name
       IMTConSymbol*       symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolGet(
       string              name,       // Name of the configuration
       string              group,      // Group name
       CIMTConSymbol       obj         // An object of the symbol configuration
       )

Python
    
    
    ManagerAPI.SymbolGet(
       str                 name,       # Name of the configuration
       str                 group       # Group name
       )

<a id="parameters"></a>
### Parameters (#parameters)

**name**  
[in] The name of the configuration.TheIMTConSymbol::Symbolvalue is used as the name..

**group**  
[in] Name of a group. TheIMTConGroup::Groupvalue is used as the group name..

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTManagerAPI::SymbolCreatemethod.

<a id="return-value"></a>
### Return Value (#return-value)

<a id="note"></a>
### Note (#note)
