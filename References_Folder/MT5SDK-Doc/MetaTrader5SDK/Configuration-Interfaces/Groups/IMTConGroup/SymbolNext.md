[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](SymbolGet.md)

# IMTConGroup::SymbolNext

Gets a symbol setting at the specified index.

C++
    
    
    MTAPIRES  IMTConGroup::SymbolNext(
       const UINT          pos,        // Position of the symbol
       IMTConGroupSymbol*  symbol      // An object of the symbol setting
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.SymbolNext(
       uint                pos,        // Position of the symbol
       CIMTConGroupSymbol  symbol      // An object of the symbol setting
       )

Python (Manager API)
    
    
    MTConGroup.SymbolNext(
       pos                 # Position of the symbol
       )

### Parameters

**pos**  
[in] The position of the symbol in the list ofgroup symbol settings, starting with 0.

**symbol**  
[out] An object of symbol setting. The symbol object must be first created using theIMTAdminAPI::GroupSymbolCreateorIMTManagerAPI::GroupSymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of a symbol with a specified index to the symbol object.
