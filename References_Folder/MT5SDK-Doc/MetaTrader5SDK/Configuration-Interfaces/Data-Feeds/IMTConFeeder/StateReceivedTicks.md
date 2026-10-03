[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / StateReceivedTicks

[Previous](StateConnected.md) | [Next](StateReceivedBooks.md)

# IMTConFeeder::StateReceivedTicks

Request number of price changes ([MTTick](../../../Structures/MTTick.md)), received by the data feed from an external data source during the current session.

C++
    
    
    UINT  IMTConFeeder::StateReceivedTicks()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFeeder.StateReceivedTicks()

Python (Manager API)
    
    
    MTConFeeder.StateReceivedTicks

### Return Value

Number of price changes.
