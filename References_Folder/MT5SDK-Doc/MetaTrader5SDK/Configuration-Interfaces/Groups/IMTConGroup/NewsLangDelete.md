[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / NewsLangDelete

[Previous](NewsLangUpdate.md) | [Next](NewsLangClear.md)

# IMTConGroup::NewsLangDelete

Deletes a news language by the index.

C++
    
    
    MTAPIRES  IMTConGroup::NewsLangDelete(
       const UINT  pos      // Position of the language
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.NewsLangDelete(
       uint        pos      // Position of the language
       )

Python (Manager API)
    
    
    MTConGroup.NewsLangDelete(
       pos         # Position of the language
       )

### Parameters

**pos**  
[in] Position of the language in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
