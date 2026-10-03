[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / SymboDelete

[Previous](SymbolUpdate.md) | [Next](SymbolClear.md)

# IMTConGroup::SymbolDelete

Deletes a symbol setting for a group.

C++
    
    
    MTAPIRES  IMTConGroup::SymbolDelete(
       const UINT  pos      // Position of the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.SymbolDelete(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConGroup.SymbolDelete(
       pos         # Position of the symbol
       )

### Parameters

**pos**  
[in] The position of the symbol in the list ofgroup symbol settings, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
