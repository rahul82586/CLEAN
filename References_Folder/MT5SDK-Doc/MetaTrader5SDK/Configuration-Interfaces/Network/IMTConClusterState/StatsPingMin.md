[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConClusterState](../IMTConClusterState.md) / StatsPingMin

[Previous](StatsPing.md) | [Next](StatsPingMax.md)

# IMTConClusterState::StatsPingMin

Get the lowest value of the network delay (ping) to the selected server for the current day.

C++
    
    
    UINT  IMTConClusterState::StatsPingMin()  const

.NET (Gateway/Manager API)
    
    
    uint  IMTConClusterState.StatsPingMin()

### Return Value

The network delay value in microseconds.
