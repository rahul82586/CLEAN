[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Network](../Network.md) / IMTConClusterState

[Previous](IMTConServerAntiDDoS/SourcesNext.md) | [Next](IMTConClusterState/Release.md)

# IMTConClusterState

The IMTConClusterState interface contains methods for controlling network connection between the trading platform components.

Use these methods to receive data on the connection state, network delays and data exchange speed between the current server ([IMTConServer::Id](IMTConServer/Id.md)) and another selected server within the cluster. The selected cluster server is specified during the call of [IMTConServer::ClusterStateGet](IMTConServer/ClusterStateGet.md) or [IMTConServer::ClusterStateNext](IMTConServer/ClusterStateNext.md) as an identifier or position in the list of components, respectively.

Method | Purpose  
---|---  
[Release](IMTConClusterState/Release.md) | Delete the current object.  
[Assign](IMTConClusterState/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConClusterState/Clear.md) | Clear an object.  
[Id](IMTConClusterState/Id.md) | Get the ID of the server, connection to which you want to analyze.  
[Connected](IMTConClusterState/Connected.md) | Get connection status with the selected server.  
[ConnectedAddress](IMTConClusterState/ConnectedAddress.md) | Get the address of the server, connection to which you want to analyze.  
[ConnectedTime](IMTConClusterState/ConnectedTime.md) | Get the time of the last connection to the selected server.  
[StatsDay](IMTConClusterState/StatsDay.md) | Get the day for which the network information is provided.  
[StatsPing](IMTConClusterState/StatsPing.md) | Get the last measured value of the network delay (ping) to the selected server.  
[StatsPingMin](IMTConClusterState/StatsPingMin.md) | Get the lowest value of the network delay (ping) to the selected server for the current day.  
[StatsPingMax](IMTConClusterState/StatsPingMax.md) | Get the largest value of the network delay (ping) to the selected server for the current day.  
[StatsSpeed](IMTConClusterState/StatsSpeed.md) | Get the last measured data transfer rate to the selected server.  
[StatsSpeedMin](IMTConClusterState/StatsSpeedMin.md) | Get the lowest data transfer rate to the selected server for the current day.  
[StatsSpeedMax](IMTConClusterState/StatsSpeedMax.md) | Get the largest data transfer rate to the selected server for the current day.
