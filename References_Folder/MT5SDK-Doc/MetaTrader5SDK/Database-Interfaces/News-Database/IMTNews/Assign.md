[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTNews::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTNews::Assign(
       const IMTNews*  news      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTNews.Assign(
       CIMTNews        news      // Source object
       )

### Parameters

**news**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
