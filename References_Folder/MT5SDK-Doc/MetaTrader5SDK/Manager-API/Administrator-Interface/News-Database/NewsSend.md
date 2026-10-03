[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [News Database](../News-Database.md) / NewsSend

[Previous](NewsUnsubscribe.md) | [Next](../History-Data.md)

# IMTAdminAPI::NewsSend

Send news.

C++
    
    
    MTAPIRES  IMTAdminAPI::NewsSend(
       IMTNews*  news      // News object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NewsSend(
       CIMTNews  news      // News object
       )

### Parameters

**news**  
[in] News object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Before sending a news item, its correctness is checked (presence of the [subject](../../../Database-Interfaces/News-Database/IMTNews/Subject.md)).
