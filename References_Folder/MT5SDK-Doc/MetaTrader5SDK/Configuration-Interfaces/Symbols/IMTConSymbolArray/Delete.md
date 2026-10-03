[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTConSymbolArray::Delete

Delete a symbol object by position.

C++
    
    
    MTAPIRES  IMTConSymbolArray::Delete(
       const UINT  pos      // Symbol position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.Delete(
       uint        pos      // Symbol position
       )

### Parameters

**pos**  
[in] Symbol position in the array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by [IMTConSymbol::Release](../IMTConSymbol/Release.md) method call.
