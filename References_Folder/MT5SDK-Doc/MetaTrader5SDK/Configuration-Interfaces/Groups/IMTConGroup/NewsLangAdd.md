[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / NewsLangAdd

[Previous](NewsCategory.md) | [Next](NewsLangUpdate.md)

# IMTConGroup::NewsLangAdd

Add a language of news that the group will receive.

C++
    
    
    MTAPIRES  IMTConGroup::NewsLangAdd(
       const UINT  language      // News language
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.NewsLangAdd(
       uint        language      // News language
       )

Python (Manager API)
    
    
    MTConGroup.NewsLangAdd(
       language    # News language
       )

### Parameters

**language**  
[in] News language in the LANGID format used inMS Windows(value from Prim.lang.identifier).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
