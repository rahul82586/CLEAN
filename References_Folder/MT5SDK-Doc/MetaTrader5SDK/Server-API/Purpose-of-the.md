[🏠 Document Start](../README.md) / [Server API](README.md) / Purpose of the

[Previous](README.md) | [Next](Interaction-with-Servers.md)

# Purpose of the Server API

The purpose of plugins written using MetaTrader 5 Server API, can be divided into four main components:

  * Calling the internal server data  
Reading various configurations, databases, information about the current state of clients, etc. This feature allows making all sorts of reports about the current state of the platform.
  * Management of internal data on a server  
Changing the settings, databases, creation of information in the databases (emails, news, etc.).
  * Receive notifications of events  
Whenever you change the database or configurations, the plugin can receive the appropriate notifications and respond to them.
  * Changing the behavior of the server  
With the help of plugins you can make various changes in the behavior of the server. For example, you can change the algorithm for calculating the agent commissions, quote filtering algorithm, etc.



Thus, plugins created using MetaTrader 5 Server API, allow you to configure servers for your own needs, enhance their functionality and integrate the platform with other systems (e.g., CRM-system).
