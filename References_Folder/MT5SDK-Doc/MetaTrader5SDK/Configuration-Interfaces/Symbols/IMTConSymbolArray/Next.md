[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTConSymbolArray::Next

Get a symbol object by position.

C++
    
    
    IMTConSymbol*  IMTConSymbolArray::Next(
       const UINT  index      // Symbol position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTConSymbol  CIMTConSymbolArray.Next(
       uint        index      // Symbol position
       )

### Parameters

**index**  
[in] Symbol position in the array, starting with 0.

### Return Value

If successful, the method returns a pointer to the [IMTConSymbol](../IMTConSymbol.md) symbol object at the corresponding array position. Otherwise, NULL is returned.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when an array object is deleted, the returned pointer becomes invalid.
