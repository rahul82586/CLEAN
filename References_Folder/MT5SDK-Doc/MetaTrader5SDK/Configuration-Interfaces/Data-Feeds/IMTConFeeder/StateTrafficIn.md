[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / StateTrafficIn

[Previous](StateReceivedNews.md) | [Next](StateTrafficOut.md)

# IMTConFeeder::StateTrafficIn

Request traffic volume received by the data feed during the current session.

C++
    
    
    UINT  IMTConFeeder::StateTrafficIn()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFeeder.StateTrafficIn()

Python (Manager API)
    
    
    MTConFeeder.StateTrafficIn

### Return Value

Incoming traffic volume in bytes.
