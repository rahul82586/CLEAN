[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTConSymbolArray::UpdateCopy

Update a symbol at the specified position of an array by copying the parameters of a passed symbol object.

C++
    
    
    MTAPIRES  IMTConSymbolArray::UpdateCopy(
       const UINT           pos,      // Position
       const IMTConSymbol*  record    // Symbol object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.UpdateCopy(
       uint                 pos,      // Position
       CIMTConSymbol        record    // Symbol object
       )

### Parameters

**pos**  
[in] Symbol position in the array, starting with 0.

**record**  
[in] Symbol object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method copies the 'record' object to the parameter object at the specified array position.
