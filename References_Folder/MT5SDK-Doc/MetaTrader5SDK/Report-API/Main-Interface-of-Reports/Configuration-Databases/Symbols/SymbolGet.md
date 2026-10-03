[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGet

[Previous](SymbolNext.md) | [Next](SymbolGetLight.md)

<a id="imtreportapisymbolget"></a>
# IMTReportAPI::SymbolGet (#imtreportapisymbolget)

Gets the symbol configuration by the name.
    
    
    MTAPIRES  IMTReportAPI::SymbolGet(
       LPCWSTR        name,       // Name of the configuration
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

<a id="parameters"></a>
### Parameters (#parameters)

**name**  
[in] The name of the configuration.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTReportAPI::SymbolCreatemethod.

<a id="return-value"></a>
### Return Value (#return-value)

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

<a id="note"></a>
### Note (#note)

The [IMTConSymbol::Symbol()](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the name. This method returns a symbol configuration with default trade settings.

<a id="group"></a>
# SymbolGet (#group)

Get an individual configuration of a symbol for a group by the name of the symbol.
    
    
    MTAPIRES  IMTReportAPI::SymbolGet(
       LPCWSTR             name,       // Name of the configuration
       const IMTConGroup*  group,      /An object of the group configuration
       IMTConSymbol*       symbol      // An object of the symbol configuration
       )

<a id="parameters"></a>
### Parameters (#parameters)

**name**  
[in] The name of the configuration.

**group**  
[in] An object of the group configuration. The group object must be first created using theIMTReportAPI::GroupCreatemethod.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTReportAPI::SymbolCreatemethod.

<a id="return-value"></a>
### Return Value (#return-value)

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

<a id="note"></a>
### Note (#note)

The [IMTConSymbol::Symbol()](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the name.
