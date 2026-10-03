[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConClusterState](../IMTConClusterState.md) / StatsDay

[Previous](ConnectedTime.md) | [Next](StatsPing.md)

# IMTConClusterState::StatsDay

Get the day for which the network information is provided.

C++
    
    
    INT64  IMTConClusterState::StatsDay()  const

.NET (Gateway/Manager API)
    
    
    long  IMTConClusterState.StatsDay()

### Return Value

The beginning of the day (00:00) for which the network information is provided. The date is specified in seconds since 01.01.1970.
