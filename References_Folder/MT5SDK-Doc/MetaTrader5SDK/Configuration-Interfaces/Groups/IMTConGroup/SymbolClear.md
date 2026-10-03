[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / SymbolClear

[Previous](SymboDelete.md) | [Next](SymbolShift.md)

# IMTConGroup::SymbolClear

Clear the list of symbols of a group

C++
    
    
    MTAPIRES  IMTConGroup::SymbolClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.SymbolClear()

Python (Manager API)
    
    
    MTConGroup.SymbolClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears the entire list of group symbols.
