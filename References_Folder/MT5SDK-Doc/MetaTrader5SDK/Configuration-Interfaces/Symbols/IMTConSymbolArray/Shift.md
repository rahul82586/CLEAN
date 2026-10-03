[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTConSymbolArray::Shift

Change the position of a symbol in an array.

C++
    
    
    MTAPIRES  IMTConSymbolArray::Shift(
       const UINT  pos,       // Symbol position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.Shift(
       uint        pos,       // Symbol position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Symbol position in the array, starting with 0.

**shift**  
[in] Shift of a symbol relative to its current position. A negative value means shifting towards the beginning of an array, a positive value - towards its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
