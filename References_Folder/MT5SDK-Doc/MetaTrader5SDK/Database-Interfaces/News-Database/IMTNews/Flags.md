[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Flags

[Previous](Language.md) | [Next](Body.md)

# IMTNews::Flags

Get news flags.

C++
    
    
    UINT  IMTNews::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnNewsFlags  CIMTNews.Flags()

### Return Value

The value of the [IMTNews::EnNewsFlags (#ennewsflags)](Enumerations.md#ennewsflags) enumeration.

# IMTNews::Flags

Set news flags.

C++
    
    
    MTAPIRES  IMTNews::Flags(
       const UINT   flags     // News flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTNews.Flags(
       EnNewsFlags  flags     // News flags
       )

### Parameters

**flags**  
[in] News flags. TheIMTNews::EnNewsFlagsenumeration is used for setting the flag.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
