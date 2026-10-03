[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / SymbolGet

[Previous](SymbolNext.md) | [Next](../IMTConGroupSymbol.md)

# IMTConGroup::SymbolGet

Gets a symbol setting at the specified path (with the full specified name).

C++
    
    
    MTAPIRES  IMTConGroup::SymbolGet(
       LPCWSTR             name,       // Path
       IMTConGroupSymbol*  symbol      // An object of the symbol setting
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.SymbolGet(
       string              name,       // Path
       CIMTConGroupSymbol  symbol      // An object of the symbol setting
       )

Python (Manager API)
    
    
    MTConGroup.SymbolGet()

### Parameters

**name**  
[in] The path to a symbol or group of symbols, which is specified in thesymbol settings for the group.

**symbol**  
[out] An object of symbol setting. The symbol object must be first created usingIMTAdminAPI::GroupSymbolCreate,IMTManagerAPI::GroupSymbolCreate,IMTServerAPI::GroupSymbolCreateorIMTGatewayAPI::GroupSymbolCreate.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of a symbol with a specified name to the symbol object.
