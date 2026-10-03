[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / TimeoutSleep

[Previous](TimeoutReconnect.md) | [Next](TimeoutAttempts.md)

# IMTConFeeder::TimeoutSleep

Gets the timeout to wait between series of attempts to reconnect to the source server.

C++
    
    
    UINT  IMTConFeeder::TimeoutSleep()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFeeder.TimeoutSleep()

Python (Manager API)
    
    
    MTConFeeder.TimeoutSleep

### Return Value

Timeout between the series of reconnections to the source server.

# IMTConFeeder::TimeoutSleep

Sets the timeout to wait between series of attempts to reconnect to the source server.

C++
    
    
    MTAPIRES  IMTConFeeder::TimeoutSleep(
       const UINT  timeout      // Timeout between reconnection series
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.TimeoutSleep(
       uint        timeout      // Timeout between reconnection series
       )

Python (Manager API)
    
    
    MTConFeeder.TimeoutSleep

### Parameters

**timeout**  
[in] Timeout between reconnection series.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
