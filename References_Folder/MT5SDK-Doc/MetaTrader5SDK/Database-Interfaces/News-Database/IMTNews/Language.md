[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Language

[Previous](Time.md) | [Next](Flags.md)

# IMTNews::Language

Gets the news language.

C++
    
    
    UINT  IMTNews::Language()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTNews.Language()

### Return Value

News language.

### Note

The language is used to filter news when receiving in terminals and when sending to different [groups](../../../Configuration-Interfaces/Groups/IMTConGroup/NewsLangAdd.md).

# IMTNews::Language

Set the news language.

C++
    
    
    MTAPIRES  IMTNews::Language(
       const UINT  language      // News language
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTNews.Language(
       uint        language      // News language
       )

### Parameters

**language**  
[in] News language in the LANGID format used inMS Windows(value from Prim.lang.identifier).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The language is used to filter news when receiving in terminals and when sending to different [groups](../../../Configuration-Interfaces/Groups/IMTConGroup/NewsLangAdd.md).
