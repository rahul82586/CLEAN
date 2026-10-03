[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / NewsLangClear

[Previous](NewsLangDelete.md) | [Next](NewsLangTotal.md)

# IMTConGroup::NewsLangClear

Clear the list of news languages.

C++
    
    
    MTAPIRES  IMTConGroup::NewsLangClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.NewsLangClear()

Python (Manager API)
    
    
    MTConGroup.NewsLangClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears the entire list of news languages specified for the group. An empty list means that the group will receive news in all languages.
