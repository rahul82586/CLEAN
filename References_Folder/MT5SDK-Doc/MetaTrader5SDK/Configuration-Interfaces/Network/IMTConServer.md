[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Network](../Network.md) / IMTConServer

[Previous](../Network.md) | [Next](IMTConServer/Enumerations.md)

# IMTConServer

The IMTConServer interface contains methods for managing the settings that are common to all types of servers.

Method | Purpose  
---|---  
[Release](IMTConServer/Release.md) | Delete the current object.  
[Assign](IMTConServer/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConServer/Clear.md) | Clear an object.  
[Type](IMTConServer/Type.md) | Get and set the server type.  
[Name](IMTConServer/Name.md) | Get and set the server name.  
[Address](IMTConServer/Address.md) | Get and set the server IPv4 address.  
[AddressTotal](IMTConServer/AddressTotal.md) | Get the number of IPv4 addresses available on a computer.  
[AddressNext](IMTConServer/AdaptersNext.md) | Get an available IPv4 address by the index.  
[AddressIPv6](IMTConServer/AddressIPv6.md) | Get and set the IPv6 address of the server.  
[AddressIPv6Total](IMTConServer/AddressIPv6Total.md) | Get the number of IPv6 addresses available on a computer.  
[AddressIPv6Next](IMTConServer/AddressIPv6Next.md) | Get an available IPv6 address by the index.  
[Id](IMTConServer/Id.md) | Get and set the server ID.  
[Password](IMTConServer/Password.md) | Set the server password.  
[PasswordCheck](IMTConServer/PasswordCheck.md) | Check the server password.  
[ServiceTime](IMTConServer/ServiceTime.md) | Get and set the service time (time of optimization), when various operations aimed at increasing the performance and reliability of the platform are conducted.  
[AdaptersCurrent](IMTConServer/AdaptersCurrent.md) | Get and set the parameter network controller.  
[AdaptersTotal](IMTConServer/AdaptersTotal.md) | Get the number of available network controllers.  
[AdaptersNext](IMTConServer/AdaptersNext.md) | Get the network controller by the index.  
[Version](IMTConServer/Version.md) | Get the server version.  
[Build](IMTConServer/Build.md) | Get the server build.  
[BuildDate](IMTConServer/BuildDate.md) | Get the date of the server build.  
[LastBootTime](IMTConServer/LastBootTime.md) | Get the time of the last server boot.  
[Connected](IMTConServer/Connected.md) | Get the status of a server connection to the main trade server.  
[OS](IMTConServer/OS.md) | Get the operating system of the computer running the server.  
[CPU](IMTConServer/CPU.md) | Get the processor type of the computer that is running the server.  
[CPUTotal](IMTConServer/CPUTotal.md) | Get the number of CPU cores.  
[CPUUsageMax](IMTConServer/CPUUsageMax.md) | Get the maximum level of CPU usage.  
[CPUUsageCritical](IMTConServer/CPUUsageCritical.md) | Get the critical level of CPU usage.  
[MemoryTotal](IMTConServer/MemoryTotal.md) | Get the total amount of available RAM.  
[MemoryFree](IMTConServer/MemoryFree.md) | Get the amount of free RAM.  
[MemoryFreeMin](IMTConServer/MemoryFreeMin.md) | Get the minimum available amount of free RAM and virtual memory.  
[MemoryFreeCritical](IMTConServer/MemoryFreeCritical.md) | Get the critical level of free RAM.  
[HDDTotal](IMTConServer/HDDTotal.md) | Get the total volume of the hard disk.  
[HDDFree](IMTConServer/HDDFree.md) | Get the amount of free memory on the hard disk.  
[HDDFreeCritical](IMTConServer/HDDFreeCritical.md) | Get the critical amount of free memory on the hard disk.  
[HDDFragments](IMTConServer/HDDFragments.md) | Get the current level of fragmentation of server files.  
[HDDFragmentsCritical](IMTConServer/HDDFragmentsCritical.md) | Get the critical level of fragmentation of server files.  
[HDDSpeedRead](IMTConServer/HDDSpeedRead.md) | Get the current speed of data reading from the hard disk.  
[HDDSpeedReadCritical](IMTConServer/HDDSpeedReadCritical.md) | Get the critical speed of data reading from the hard disk.  
[HDDSpeedWrite](IMTConServer/HDDSpeedWrite.md) | Get the current speed of information writing on the hard disk.  
[HDDSpeedWriteCritical](IMTConServer/HDDSpeedWriteCritical.md) | Get the critical speed of information writing on the hard disk.  
[ConnectsMax](IMTConServer/ConnectsMax.md) | Get the maximum number of simultaneous connections to a server that has been achieved during the day.  
[ConnectsCritical](IMTConServer/ConnectsCritical.md) | Get the critical number of simultaneous connections to the server.  
[NetworkMax](IMTConServer/Max.md) | Get the maximum level of network usage reached during the day.  
[NetworkCritical](IMTConServer/Critical.md) | Get the critical level of network usage.  
[TradeServer](IMTConServer/TradeServer.md) | The interface of the Trade Server.  
[HistoryServer](IMTConServer/HistoryServer.md) | The interface of the History Server.  
[AccessServer](IMTConServer/AccessServer.md) | The interface of the Access Server.  
[BackupServer](IMTConServer/BackupServer.md) | The interface of the Backup Server.  
[AntiDDoSServer](IMTConServer/AntiDDoSServer.md) | The Anti DDoS server interface.  
[PointsAdd](IMTConServer/PointsAdd.md) | Add an access point.  
[PointsUpdate](IMTConServer/PointsUpdate.md) | Update of the access point at the specified position in the list.  
[PointsShift](IMTConServer/PointsShift.md) | Move an access point in the list.  
[PointsDelete](IMTConServer/PointsDelete.md) | Delete an access point by the index.  
[PointsClear](IMTConServer/PointsClear.md) | Clear the list of access points.  
[PointsTotal](IMTConServer/PointsTotal.md) | Get the number of access points of the Access Server.  
[PointsNext](IMTConServer/PointsNext.md) | Get an access point by the index.  
[BindingsAdd](IMTConServer/BindingsAdd.md) | Add a binding.  
[BindingsUpdate](IMTConServer/BindingsUpdate.md) | Update the binding at the specified position in the list.  
[BindingsShift](IMTConServer/BindingsShift.md) | Move a binding in the list.  
[BindingsDelete](IMTConServer/BindingsDelete.md) | Delete a binding by the index.  
[BindingsClear](IMTConServer/BindingsClear.md) | Clear the list of bindings.  
[BindingsTotal](IMTConServer/BindingsTotal.md) | Get the number of bindings of the Access Server.  
[BindingsNext](IMTConServer/BindingsNext.md) | Get a binding by the index.  
[FailoverMode](IMTConServer/FailoverMode.md) | Get and set the automated failover mode.  
[FailoverTime](IMTConServer/FailoverTimeout.md) | Get the downtime of the primary server, after which the platform switches to a backup server.  
[ClusterStateTotal](IMTConServer/ClusterStateTotal.md) | Get the number of cluster components, the status of connection with which can be analyzed for the current server.  
[ClusterStateNext](IMTConServer/ClusterStateNext.md) | Get the network connection status with a cluster component having the specified index.  
[ClusterStateGet](IMTConServer/ClusterStateGet.md) | Get the network connection status with a cluster component having the specified identifier.  
  
The IMTConServer class contains one enumeration:

Enumeration | Purpose  
---|---  
[EnServerTypes](IMTConServer/Enumerations.md) | Server type.  
[EnFailoverModes (#enfailovermodes)](IMTConServer/Enumerations.md#enfailovermodes) | Automated failover modes
