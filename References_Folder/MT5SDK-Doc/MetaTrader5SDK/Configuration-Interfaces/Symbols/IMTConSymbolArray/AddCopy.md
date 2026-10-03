[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTConSymbolArray::AddCopy

Add a copy of a symbol object to the end of an array.

C++
    
    
    MTAPIRES  IMTConSymbolArray::AddCopy(
       const IMTConSymbol*  record    // Symbol to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.AddCopy(
       CIMTConSymbol        record    // Symbol to be added
       )

### Parameters

**record**  
[in]IMTConSymbolsymbol object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'record' object and places it to the end of the array.

# IMTConSymbolArray::AddCopy

Add copies of symbol objects to an array.

C++
    
    
    MTAPIRES  IMTConSymbolArray::AddCopy(
       const IMTConSymbolArray*  array      // Array of symbols to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.AddCopy(
       CIMTConSymbolArray        array      // Array of symbols to be added
       )

### Parameters

**array**  
[in] Symbols array objectIMTConSymbolArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of objects belonging to the 'array' object, and inserts them at the end of the current array.
