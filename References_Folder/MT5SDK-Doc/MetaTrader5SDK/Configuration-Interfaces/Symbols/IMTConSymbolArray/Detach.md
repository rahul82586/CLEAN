[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTConSymbolArray::Detach

Detach a symbol object from an array.

C++
    
    
    IMTConSymbol*  IMTConSymbolArray::Detach(
       const UINT  pos      // Symbol position
       )

.NET (Gateway/Manager API)
    
    
    CIMTConSymbol  CIMTConSymbolArray.Detach(
       uint        pos      // Symbol position
       )

### Parameters

**pos**  
[in] Symbol position in the array, starting with 0.

### Return Value

Returns a pointer to the detached [IMTConSymbol](../IMTConSymbol.md) symbol object.

### Note

This method removes the object pointer at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
