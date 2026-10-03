[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNewsSink](../IMTNewsSink.md) / HookNews

[Previous](OnNews.md) | [Next](../../Byte-Stream.md)

# IMTNewsSink::HookNews

A hook of the event of news receiving.

C++
    
    
    virtual MTAPIRES  IMTNewsSink::HookNews(
       const int  feeder,     // Source of news
       IMTNews*   news        // An object of news
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTNewsSink.HookNews(
       int        feeder,     // Source of news
       CIMTNews   news        // An object of news
       )

### Parameters

**feeder**  
[in] The name of a data feed from which a news item is received. If the value is -1, the news was created by the dealer.

**news**  
[in][out] An object of news.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called consistently in accordance with the order of plugins in the list until the first plugin that has returned a response code other than [MT_RET_OK](../../../Return-Codes/Successful-completion.md).
