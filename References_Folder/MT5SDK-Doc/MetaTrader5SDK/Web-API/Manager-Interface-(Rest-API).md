[🏠 Document Start](../README.md) / [Web API](README.md) / Manager Interface (Rest API)

[Previous](Examples.md) | [Next](Manager-Interface-(Rest-API)/Configuration-Databases.md)

# Main Interface (Rest API)

The following commands of manager connection to a trade server are implemented the MetaTrader 5 Web API:

  * [Configuration Databases](Manager-Interface-(Rest-API)/Configuration-Databases.md)
  * [Trading](Manager-Interface-(Rest-API)/Trading.md)
  * [Users](Manager-Interface-(Rest-API)/Users.md)
  * [Clients](Manager-Interface-(Rest-API)/Clients.md)
  * [Mail](Manager-Interface-(Rest-API)/Mail.md)
  * [News](Manager-Interface-(Rest-API)/News.md)
  * [Prices](Manager-Interface-(Rest-API)/Prices.md)
  * [Daily Reports](Manager-Interface-(Rest-API)/Daily-Reports.md)
  * [Settings Files](Manager-Interface-(Rest-API)/Settings-Files.md)
  * [Subscriptions](Manager-Interface-(Rest-API)/Subscriptions.md)
  * [Common Requests](Manager-Interface-(Rest-API)/Common-Requests.md)



The accessibility of information using the manager commands is fully defined by access permissions set for the manager account that is used for [connecting](Manager-Interface-(Rest-API)/Text-Protocol-(Raw-API)/Authentication.md#client-start) to the server.  
---  
  
The main method of working with the Manager interface is sending commands via GET and POST requests (Rest API). However, it also supports the purely [text-based protocol](Manager-Interface-(Rest-API)/Text-Protocol-(Raw-API).md) (Raw API). Manager commands can be sent to the server as text messages over TCP connection. The MetaTrader 5 SDK package also includes the [PHP](Manager-Interface-(Rest-API)/PHP-Implementation-of-Protocol.md) and [.NET](Manager-Interface-(Rest-API)/NET-Implementation-of-Protocol.md) implementation examples of this protocol.
