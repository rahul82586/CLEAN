[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / SymbolShift

[Previous](SymbolClear.md) | [Next](SymbolTotal.md)

# IMTConGroup::SymbolShift

Move a symbol setting in the list.

C++
    
    
    MTAPIRES  IMTConGroup::SymbolShift(
       const UINT  pos,       // Position of the symbol
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.SymbolShift(
       uint        pos,       // Position of the symbol
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConGroup.SymbolShift(
       pos,        # Position of the symbol
       shift       # Shift
       )

### Parameters

**pos**  
[in] The position of the symbol in the list ofgroup symbol settings, starting with 0.

**shift**  
[in] Shift of a symbol relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
