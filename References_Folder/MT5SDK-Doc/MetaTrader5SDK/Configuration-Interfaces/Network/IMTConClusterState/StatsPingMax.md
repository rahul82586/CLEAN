[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConClusterState](../IMTConClusterState.md) / StatsPingMax

[Previous](StatsPingMin.md) | [Next](StatsSpeed.md)

# IMTConClusterState::StatsPingMax

Get the largest value of the network delay (ping) to the selected server for the current day.

C++
    
    
    UINT  IMTConClusterState::StatsPingMax()  const

.NET (Gateway/Manager API)
    
    
    uint  IMTConClusterState.StatsPingMax()

### Return Value

The network delay value in microseconds.
