[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / SymbolUpdate

[Previous](SymbolAdd.md) | [Next](SymboDelete.md)

# IMTConGroup::SymbolUpdate

Change a symbol setting for a group at the specified position.

C++
    
    
    MTAPIRES  IMTConGroup::SymbolUpdate(
       const UINT                pos,        // Position of the symbol
       const IMTConGroupSymbol*  symbol      // An object of symbol setting
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.SymbolUpdate(
       uint                      pos,        // Position of the symbol
       CIMTConGroupSymbol        symbol      // An object of symbol setting
       )

Python (Manager API)
    
    
    MTConGroup.SymbolUpdate(
       pos,                      # Position of the symbol
       symbol                    # An object of symbol setting
       )
    
    
    MTConGroup.SymbolUpdate(
       symbol_list               # A list of objects
       )

### Parameters

**pos**  
[in] The position of the symbol in the list ofgroup symbol settings, starting with 0.

**symbol**  
[in] An object of the symbol setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
