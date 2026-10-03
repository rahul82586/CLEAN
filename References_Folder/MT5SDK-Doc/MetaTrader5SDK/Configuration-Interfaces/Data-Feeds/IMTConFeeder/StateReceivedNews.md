[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / StateReceivedNews

[Previous](StateReceivedBooks.md) | [Next](StateTrafficIn.md)

# IMTConFeeder::StateReceivedBooks

Request number news ([MTNews](../../../Structures/MTNews.md)) received by the data feed from an external data source during the current session.

C++
    
    
    UINT  IMTConFeeder::StateReceivedNews()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFeeder.StateReceivedNews()

Python (Manager API)
    
    
    MTConFeeder.StateReceivedNews

### Return Value

Number of news.
