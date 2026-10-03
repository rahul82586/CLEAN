[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [News Database](../News-Database.md) / NewsSend

[Previous](NewsUnsubscribe.md) | [Next](../Daily-Reports.md)

# IMTServerAPI::NewsSend

Send news.
    
    
    MTAPIRES  IMTServerAPI::NewsSend(
       IMTNews*  news      // News object
       )

### Parameters

**news**  
[in] News object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Before sending a news item, its correctness is checked (presence of the [subject](../../../Database-Interfaces/News-Database/IMTNews/Subject.md)).
