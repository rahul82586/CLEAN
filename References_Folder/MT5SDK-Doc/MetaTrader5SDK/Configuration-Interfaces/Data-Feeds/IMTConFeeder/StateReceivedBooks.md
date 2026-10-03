[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / StateReceivedBooks

[Previous](StateReceivedTicks.md) | [Next](StateReceivedNews.md)

# IMTConFeeder::StateReceivedBooks

Request number of the Depth of Market changes ([MTBook](../../../Structures/MTBookMTBookDiff.md)), received by the data feed from an external data source during the current session.

C++
    
    
    UINT  IMTConFeeder::StateReceivedBooks()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFeeder.StateReceivedBooks()

Python (Manager API)
    
    
    MTConFeeder.StateReceivedBooks

### Return Value

Number of Depth of Market changes.
