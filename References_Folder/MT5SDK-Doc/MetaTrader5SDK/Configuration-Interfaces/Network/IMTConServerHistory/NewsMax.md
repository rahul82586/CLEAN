[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerHistory](../IMTConServerHistory.md) / NewsMax

[Previous](DatafeedsTimeout.md) | [Next](../IMTConServerBackup.md)

# IMTConServerHistory::NewsMax

Gets the maximum number of news that can be stored on the history server.

C++
    
    
    UINT  IMTConServerHistory::NewsMax()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerHistory.NewsMax()

Python (Manager API)
    
    
    MTConServerHistory.NewsMax

### Return Value

The maximum number of news that can be stored on the history server.

# IMTConServerHistory::NewsMax

Sets the maximum number of news that can be stored on the history server.

C++
    
    
    MTAPIRES  IMTConServerHistory::NewsMax(
       const UINT  news_max      // Maximum number of news
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerHistory.NewsMax(
       uint        news_max      // Maximum number of news
       )

Python (Manager API)
    
    
    MTConServerHistory.NewsMax

### Parameters

**news_max**  
[in] The maximum number of news.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
