[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGet

[Previous](SymbolNext.md) | [Next](../Groups.md)

<a id="group"></a>
# IMTGatewayAPI::SymbolGet (#group)

Gets the symbol configuration by the name.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SymbolGet(
       LPCWSTR        name,       // Name of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SymbolGet(
       string         name,       // Name of the configuration
       CIMTConSymbol  symbol      // An object of the symbol configuration
       )

<a id="parameters"></a>
### Parameters (#parameters)

**name**  
[in] The name of the configuration.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTGatewatAPI::SymbolCreatemethod.

<a id="return-value"></a>
### Return Value (#return-value)

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

<a id="note"></a>
### Note (#note)

The method returns a symbol configuration with default trade settings.

  * If a symbol with the name matching the symbol name in the external system is found in the platform, SymbolGet will return the configuration of the original symbol.
  * If there is no such symbol in the platform, the first translation setting corresponding to the original symbol will be used. For example, if for the original EURUSD symbol two settings are available, EURUSD.1 and EURUSD.2, SymbolGet(EURUSD,symbol) will return the configuration of EURUSD.1.
  * During the call of SymbolGet(name,group,symbol), the availability of a symbol for the group is additionally checked. If a symbol with the original name exists in the platform and it is available to the specified group, the method will return its configuration. Otherwise, a symbol from the first translation setting corresponding to the original symbol will be used. If it is available to the specified group, the method will return its settings. If it is not available, the next setting will be used, etc.



<a id="group"></a>
# IMTGatewayAPI::SymbolGet (#group)

Get symbol settings taking into account that they are overridden for the specified group.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SymbolGet(
       LPCWSTR             name,        // Name of the configuration
       LPCWSTR             name_group,  // Group name
       IMTConSymbol*       symbol       // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SymbolGet(
       string              name,        // Name of the configuration
       string              name_group,  // Group name
       CIMTConSymbol       symbol       // An object of the symbol configuration
       )

<a id="parameters"></a>
### Parameters (#parameters)

**name**  
[in] The name of the configuration.

**name_group**  
[in] Group name.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTGatewatAPI::SymbolCreatemethod.

<a id="return-value"></a>
### Return Value (#return-value)

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

<a id="note"></a>
### Note (#note)

The method returns a symbol configuration with trade settings for the specified group. The [IMTConGroup::Group](../../../../Configuration-Interfaces/Groups/IMTConGroup/Group.md) value is used as the group name.

  * If a symbol with the name matching the symbol name in the external system is found in the platform, SymbolGet will return the configuration of the original symbol.
  * If there is no such symbol in the platform, the first translation setting corresponding to the original symbol will be used. For example, if for the original EURUSD symbol two settings are available, EURUSD.1 and EURUSD.2, SymbolGet(EURUSD,symbol) will return the configuration of EURUSD.1.
  * During the call of SymbolGet(name,group,symbol), the availability of a symbol for the group is additionally checked. If a symbol with the original name exists in the platform and it is available to the specified group, the method will return its configuration. Otherwise, a symbol from the first translation setting corresponding to the original symbol will be used. If it is available to the specified group, the method will return its settings. If it is not available, the next setting will be used, etc.


