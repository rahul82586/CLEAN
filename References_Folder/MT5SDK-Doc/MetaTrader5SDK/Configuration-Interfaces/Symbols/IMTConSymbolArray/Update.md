[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTConSymbolArray::Update

Update a symbol at the specified position of an array.

C++
    
    
    MTAPIRES  IMTConSymbolArray::Update(
       const UINT     pos,       // Position
       IMTConSymbol*  record     // Symbol object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.Update(
       uint           pos,       // Position
       CIMTConSymbol  record     // Symbol object
       )

### Parameters

**pos**  
[in] Symbol position in the array, starting with 0.

**record**  
[in]IMTConSymbolsymbol object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTConSymbolArray::Update method deletes the previous element (by calling [IMTConSymbol::Release](../IMTConSymbol/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by the array object. Thus, when deleting an array object (by calling IMTConSymbolArray::Release), an earlier inserted object will be automatically deleted.
