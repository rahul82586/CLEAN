[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTConSymbolArray::Add

Add a symbol object to the end of an array.

C++
    
    
    MTAPIRES  IMTConSymbolArray::Add(
       IMTConSymbol*  record    // Symbol object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.Add(
       CIMTConSymbol  record    // Symbol object
       )

### Parameters

**record**  
[in]IMTConSymbolsymbol object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, control over the lifetime of the 'record' object is transferred to the array object. Thus, when deleting an array object (by calling [IMTConSymbolArray::Release](Release.md)), an earlier inserted object will be automatically deleted.

In turn, the deletion of a newly inserted object will cause the pointer stored within the array object to become invalid, and therefore its call (also when deleting the array object) will cause the application to crash.

Please be sure to never add a link to one and the same object within an array, as this will lead to a crash during memory release.

# IMTConSymbolArray::Add

Add an object of the groups array to the end of an array.

C++
    
    
    MTAPIRES  IMTConSymbolArray::Add(
       IMTConSymbolArray*  array      // Array of symbols to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolArray.Add(
       CIMTConSymbolArray  array      // Array of symbols to be added
       )

### Parameters

**array**  
[in] Symbols array objectIMTConSymbolArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers from the 'array' object to the end of the current array and clears the 'array' object.
