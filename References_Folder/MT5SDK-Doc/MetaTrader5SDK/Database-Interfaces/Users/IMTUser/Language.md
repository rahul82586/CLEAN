[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Language

[Previous](Country.md) | [Next](City.md)

# IMTUser::Language

Get the user's language.

C++
    
    
    UINT  IMTUser::Language()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTUser.Language()

### Return Value

User's language.

# IMTUser::Language

Set the user's language.

C++
    
    
    MTAPIRES  IMTUser::Language(
       const UINT  language      // Language
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Language(
       uint        language      // Language
       )

### Parameters

**language**  
[in] The user's language in the LANGID format used inMS Windows(value from Prim.lang.identifier).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
