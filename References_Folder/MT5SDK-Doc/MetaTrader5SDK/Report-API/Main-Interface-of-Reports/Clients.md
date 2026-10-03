[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Main Interface of Reports](../Main-Interface-of-Reports.md) / Clients

[Previous](Configuration-Databases/Funds-and-ETF/FundGet.md) | [Next](Clients/ClientCreate.md)

# Clients

MetaTrader 5 Report API provides functionality for receiving data from the client database stored on the trade server. Use the API to expand the standard functionality of the reporting system and to create tables and diagrams based on any data series from the client database.

A detailed description of operations with clients is provided in the [MetaTrader 5 Administrator documentation](https://support.metaquotes.net/en/docs/mt5/platform/administration/clients).

  * The client database is maintained separately for each trading server in the cluster. The plugin can only manage those clients which belong to [the server, on which the plugin is running](../../Server-API/Configuration-of-Plugins.md).
  * Data requesting methods are executed in accordance with the availability of clients for the specific [manager account, from which the data is requested](../Request-for-Reports.md).

  
---  
  
The following client operation functions are available:

Features | Purpose  
---|---  
[ClientCreate](Clients/ClientCreate.md) | Create a client object.  
[ClientCreateArray](Clients/ClientCreateArray.md) | Create an object of the client array.  
[ClientGet](Clients/ClientGet.md) | Get a client by identifier.  
[ClientGetHistory](Clients/ClientGetHistory.md) | Get the history of client changes.  
[ClientIdsAll](Clients/ClientIdsAll.md) | Get the list of identifiers of all clients in the server database.  
[ClientIdsByGroup](Clients/ClientIdsByGroup.md) | Get the list of identifiers of all clients in the server database filtered by the list of groups.  
[ClientUserLogins](Clients/ClientUserLogins.md) | Get the list of client's trading accounts.
