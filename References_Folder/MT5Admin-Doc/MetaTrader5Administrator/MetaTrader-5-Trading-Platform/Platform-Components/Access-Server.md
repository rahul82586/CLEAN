[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../Platform-Components.md) / Access Server

[Previous](Trade-Server/Return-Errors.md) | [Next](Access-Server/Structure-of-Directories-and-Files.md)

# Access Server

Access servers are proxy servers and the platform firewalls at the same time. They perform the following functions:

  * Processing of incoming client connections.
  * Packing authorization requests and sending them to the trade server.
  * Checking activity of client connections protecting the trade server from attacks and overload ([antiflood control](Access-Server/Antiflood-Control.md)).
  * Saving history data, depth of market and news, and translate them to clients, thus reducing the load to the history server.
  * Cashing and providing [Live Update](../Platform-Setup/Live-Update.md) to terminals.
  * [Monitoring (#witness)](../Platform-Setup/Network-cluster/Configuring-Servers/Access-Server.md#witness) the operation of the history and trade servers.



The unlimited number of access servers can exist for each trade server. Terminals are switched between them automatically, depending on the [priority](Access-Server/Priority.md) settings.

  * For server configuration details, see the ["Network cluster"](../Platform-Setup/Network-cluster/Configuring-Servers.md) section.


  * Use the [Access Server hosting from MetaQuotes](../Platform-Setup/Network-cluster/Hosted-Access-Servers.md) to quickly and safely deploy an access server in the desired region. 

  
---
