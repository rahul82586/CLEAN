[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / StateConnected

[Previous](TranslateGet.md) | [Next](StateReceivedTicks.md)

# IMTConFeeder::StateConnected

Get the state of the data feed connection to an external data source.

C++
    
    
    bool  IMTConFeeder::StateConnected()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConFeeder.StateConnected()

Python (Manager API)
    
    
    MTConFeeder.StateConnected

### Return Value

If a data feed has successfully connected to a history data source and is ready to interact with it, the method returns TRUE, otherwise — FALSE.
