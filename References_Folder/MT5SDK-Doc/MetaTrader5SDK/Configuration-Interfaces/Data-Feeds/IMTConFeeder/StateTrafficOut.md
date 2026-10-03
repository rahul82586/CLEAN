[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / StateTrafficOut

[Previous](StateTrafficIn.md) | [Next](../IMTConFeederModule.md)

# IMTConFeeder::StateTrafficOut

Request traffic volume sent by the data feed during the current session.

C++
    
    
    UINT  IMTConFeeder::StateTrafficOut()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFeeder.StateTrafficOut()

Python (Manager API)
    
    
    MTConFeeder.StateTrafficOut

### Return Value

Outgoing traffic volume in bytes.
