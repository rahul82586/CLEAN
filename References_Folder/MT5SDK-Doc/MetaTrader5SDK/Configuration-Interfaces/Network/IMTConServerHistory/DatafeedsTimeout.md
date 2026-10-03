[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerHistory](../IMTConServerHistory.md) / DatafeedsTimeout

[Previous](Clear.md) | [Next](NewsMax.md)

# IMTConServerHistory::DatafeedsTimeout

Get a timeout of [data feeds](../../Data-Feeds.md) before switching to other feed.

C++
    
    
    UINT  IMTConServerHistory::DatafeedsTimeout()  const

.NET (Gateway/Manager API)
    
    
    uint  IMTConServerHistory::DatafeedsTimeout()

Python (Manager API)
    
    
    MTConServerHistory.DatafeedsTimeout

### Return Value

Timeout if data feed.

# IMTConServerHistory::DatafeedsTimeout

Set a timeout of [data feeds](../../Data-Feeds.md) before switching to other feed.

C++
    
    
    MTAPIRES  IMTConServerHistory::DatafeedsTimeout(
       const UINT  timeout      // Timeout
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerHistory.DatafeedsTimeout(
       uint        timeout      // Timeout
       )

Python (Manager API)
    
    
    MTConServerHistory.DatafeedsTimeout

### Parameters

**timeout**  
[in] Data feed timeout in seconds.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
