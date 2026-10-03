[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Network](../Network.md) / IMTConServerAccess

[Previous](IMTConBackupFolder/Flags.md) | [Next](IMTConServerAccess/Enumerations.md)

# IMTConServerAccess

The IMTConServerAccess interface contains methods for controlling the settings specific to the access servers.

Method | Purpose  
---|---  
[Release](IMTConServerAccess/Release.md) | Delete the current object.  
[Assign](IMTConServerAccess/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConServerAccess/Clear.md) | Clear an object.  
[Priority](IMTConServerAccess/Priority.md) | Get and set the base priority of the Access Server.  
[PriorityCurrent](IMTConServerAccess/PriorityCurrent.md) | Get the current priority of the Access Server.  
[AccessFlags](IMTConServerAccess/AccessFlags.md) | Get and set additional parameters of the Access Server.  
[AccessMask](IMTConServerAccess/AccessMask.md) | Get and set the allowed types of connection to the Access Server.  
[NewsMax](IMTConServerAccess/NewsMax.md) | Get and set the maximum number of news that can be stored on the Access Server.  
[AntifloodEnabled](IMTConServerAccess/AntifloodEnabled.md) | Get and set the state of antiflood control.  
[AntifloodConnects](IMTConServerAccess/AntifloodConnects.md) | Get and set the maximum number of connections from one IP address for a certain period of time, after which the address is temporarily blocked.  
[AntifloodErrors](IMTConServerAccess/AntifloodErrors.md) | Get and set the maximum number of incorrect connections, after which the IP address is temporarily blocked.  
[PointsAdd](IMTConServerAccess/PointsAdd.md) | Add an access point.  
[PointsUpdate](IMTConServerAccess/PointsUpdate.md) | Update of the access point at the specified position in the list.  
[PointsShift](IMTConServerAccess/PointsShift.md) | Move an access point in the list.  
[PointsDelete](IMTConServerAccess/PointsDelete.md) | Delete an access point by the index.  
[PointsClear](IMTConServerAccess/PointsClear.md) | Clear the list of access points.  
[PointsTotal](IMTConServerAccess/PointsTotal.md) | Get the number of access points of the Access Server.  
[PointsNext](IMTConServerAccess/PointsNext.md) | Get an access point by the index.  
[BindingsAdd](IMTConServerAccess/BindingsAdd.md) | Add a binding.  
[BindingsUpdate](IMTConServerAccess/BindingsUpdate.md) | Update the binding at the specified position in the list.  
[BindingsShift](IMTConServerAccess/BindingsShift.md) | Move a binding in the list.  
[BindingsDelete](IMTConServerAccess/BindingsDelete.md) | Delete a binding by the index.  
[BindingsClear](IMTConServerAccess/BindingsClear.md) | Clear the list of bindings.  
[BindingsTotal](IMTConServerAccess/BindingsTotal.md) | Get the number of bindings of the Access Server.  
[BindingsNext](IMTConServerAccess/BindingsNext.md) | Get a binding by the index.  
[ServersAdd](IMTConServerAccess/ServersAdd.md) | Add a trade server connection to which will be implemented through this Access Server.  
[ServersUpdate](IMTConServerAccess/ServersUpdate.md) | Update a trade server connection to which will be implemented through this Access Server.  
[ServersShift](IMTConServerAccess/ServersShift.md) | Move a trade server connection to which is implemented through this Access Server.  
[ServersDelete](IMTConServerAccess/ServersDelete.md) | Delete a trade server connection to which is implemented through this Access Server, from the list.  
[ServersClear](IMTConServerAccess/ServersClear.md) | Clear the list of trading servers connection to which is implemented through this Access Server.  
[ServersTotal](IMTConServerAccess/ServersTotal.md) | Get the number of trade servers connection to which will be implemented through this Access Server.  
[ServersNext](IMTConServerAccess/ServersNext.md) | Get a trade server connection to which is implemented through this Access Server, by the index.  
  
The IMTConServerAccess class contains the following methods:

Enumeration | Purpose  
---|---  
[EnAccessMask](IMTConServerAccess/Enumerations.md) | Allowed types of connection.  
[EnServerPriority (#enserverpriority)](IMTConServerAccess/Enumerations.md#enserverpriority) | Priority of the Access Server.
