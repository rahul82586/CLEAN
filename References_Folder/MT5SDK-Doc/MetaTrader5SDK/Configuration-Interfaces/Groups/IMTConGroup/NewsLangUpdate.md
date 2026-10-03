[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / NewsLangUpdate

[Previous](NewsLangAdd.md) | [Next](NewsLangDelete.md)

# IMTConGroup::NewsLangUpdate

Change the language of news that the group will receive.

C++
    
    
    MTAPIRES  IMTConGroup::NewsLangUpdate(
       const UINT  pos,          // Position of the language
       const UINT  language      // News language
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.NewsLangUpdate(
       uint        pos,          // Position of the language
       uint        language      // News language
       )

Python (Manager API)
    
    
    MTConGroup.NewsLangUpdate(
       pos,        # Position of the language
       language    # News language
       )
    
    
    MTConGroup.NewsLangSet(
       lang_list   # A list of languages
       )

### Parameters

**pos**  
[in] Position of the language in the list, starting with 0.

**language**  
[in] News language in the LANGID format used inMS Windows(value from Prim.lang.identifier).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
