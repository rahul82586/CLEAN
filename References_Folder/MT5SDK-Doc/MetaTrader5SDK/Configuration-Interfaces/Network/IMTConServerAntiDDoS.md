[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Network](../Network.md) / IMTConServerAntiDDoS

[Previous](IMTConServerAccess/ServersNext.md) | [Next](IMTConServerAntiDDoS/Enumerations.md)

# IMTConServerAntiDDoS

The IMTConServerAntiDDoS interface contains methods for managing parameters of the Anti DDoS Proxy Server component, which enables the use of [external Anti-DDoS services](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_anti_ddos).

Method | Purpose  
---|---  
[Release](IMTConServerAntiDDoS/Release.md) | Delete the current object.  
[Assign](IMTConServerAntiDDoS/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConServerAntiDDoS/Clear.md) | Clear an object.  
[Priority](IMTConServerAntiDDoS/Priority.md) | Get and set the allowed types of connection to the Access Server.  
[AccessMask](IMTConServerAntiDDoS/AccessMask.md) | Get the allowed types of connection to the Anti-DDoS Server.  
[PointsAdd](IMTConServerAntiDDoS/PointsAdd.md) | Add a public access point of the Anti DDoS protection provider.  
[PointsUpdate](IMTConServerAntiDDoS/PointsUpdate.md) | Edit the public access point of the Anti DDoS protection provider.  
[PointsShift](IMTConServerAntiDDoS/PointsShift.md) | Move a public access point of the Anti DDoS protection provider in the list.  
[PointsDelete](IMTConServerAntiDDoS/PointsDelete.md) | Delete a public access point of the Anti DDoS protection provider with the specified index.  
[PointsClear](IMTConServerAntiDDoS/PointsClear.md) | Clear the list of access points of the Anti DDoS protection provider.  
[PointsTotal](IMTConServerAntiDDoS/PointsTotal.md) | Get the number of access points of the Anti DDoS protection provider.  
[PointsNext](IMTConServerAntiDDoS/PointsNext.md) | Get a public access point of the Anti DDoS protection provider with the specified index.  
[ServersAdd](IMTConServerAntiDDoS/ServersAdd.md) | Add a trade server, the connection to which will be implemented through this Anti DDoS server.  
[ServersUpdate](IMTConServerAntiDDoS/ServersUpdate.md) | Edit a trade server, the connection to which will be implemented through this Anti DDoS server.  
[ServersShift](IMTConServerAntiDDoS/ServersShift.md) | Move a trade server, the connection to which is implemented through this Anti DDoS server, in the list.  
[ServersDelete](IMTConServerAntiDDoS/ServersDelete.md) | Delete from the list a trade server, the connection to which is implemented through this Anti DDoS server.  
[ServersClear](IMTConServerAntiDDoS/ServersClear.md) | Clear the list of trade servers, the connection to which is implemented through this Anti DDoS server.  
[ServersTotal](IMTConServerAntiDDoS/ServersTotal.md) | Get the number of trade servers, the connection to which is implemented through this Anti DDoS server.  
[ServersNext](IMTConServerAntiDDoS/ServersNext.md) | Get a trade server, the connection to which is implemented through this Anti DDoS server, by the index.  
[SourcesAdd](IMTConServerAntiDDoS/SourcesAdd.md) | Add a range of IP addresses of Anti DDoS provider's proxy servers.  
[SourcesUpdate](IMTConServerAntiDDoS/SourcesUpdate.md) | Update the range of IP addresses of Anti DDoS provider's proxy servers.  
[SourcesDelete](IMTConServerAntiDDoS/SourcesDelete.md) | Delete the range of IP addresses of Anti DDoS provider's proxy servers.  
[SourcesShift](IMTConServerAntiDDoS/SourcesShift.md) | Change the position of the range of IP addresses of Anti DDoS provider's proxy servers in the list.  
[SourcesTotal](IMTConServerAntiDDoS/SourcesTotal.md) | Get the number of ranges of IP addresses of Anti DDoS provider's proxy servers.  
[SourcesNext](IMTConServerAntiDDoS/SourcesNext.md) | Get the range of IP addresses of Anti DDoS provider's proxy servers at the specified index.  
  
The IMTConServerAntiDDoS class contains the following methods:

Enumeration | Purpose  
---|---  
[EnAccessMask](IMTConServerAntiDDoS/Enumerations.md) | Get and set allowed types of connection.  
[EnServerPriority](IMTConServerAntiDDoS/Enumerations.md) | Get and set the basic priority of the Anti DDoS server.
