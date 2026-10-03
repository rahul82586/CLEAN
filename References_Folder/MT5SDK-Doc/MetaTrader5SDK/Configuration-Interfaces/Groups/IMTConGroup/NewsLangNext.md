[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / NewsLangNext

[Previous](NewsLangTotal.md) | [Next](MailMode.md)

# IMTConGroup::NewsLangNext

Get the language of news at the position in the list of selected language.

C++
    
    
    UINT  IMTConGroup::NewsLangNext(
       const UINT  pos      // Position of the language
       )  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroup.NewsLangNext(
       uint        pos      // Position of the language
       )

Python (Manager API)
    
    
    MTConGroup.NewsLangNext(
       pos         # Position of the language
       )
    
    
    MTConGroup.NewsLangGet()

### Parameters

**pos**  
[in] Position of the language in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
