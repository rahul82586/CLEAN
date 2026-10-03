[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNewsSink](../IMTNewsSink.md) / OnNews

[Previous](../IMTNewsSink.md) | [Next](HookNews.md)

# IMTNewsSink::OnNews

A handler of the event of news receiving.

C++
    
    
    virtual void  IMTNewsSink::OnNews(
       const IMTNews*  news      // A pointer to the news object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTNewsSink.OnNews(
       CIMTNews        news      // News object
       )

### Parameters

**news**  
[in] A pointer to the news object.

### Note

In Manager API, only the news header without the body is received in the IMTNewsSink::OnNews event. To request the news body, call the [IMTManagerAPI::NewsBodyRequest](../../../Manager-API/Manager-Interface/News-Database/NewsBodyRequest.md) method while passing to the method the news ID ([IMTNews::ID](../IMTNews/ID.md)) from the event.
