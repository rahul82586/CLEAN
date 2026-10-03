[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../Platform-Components.md) / History Server

[Previous](Access-Server/Priority.md) | [Next](History-Server/Structure-of-Directories-and-Files.md)

# History Server

The history server processes price and news data. This server performs the following functions:

  * Receiving and filtering price and news data from gateways and datafeeds.
  * Packing price and news data.
  * Storing and providing price history in the form of 1-minute bars and ticks to other components of the platform.
  * Storing and providing the news thread.
  * Receiving, checking and distributing [Live Updates](../Platform-Setup/Live-Update.md) among the MetaTrader 5 platform components.



> For server configuration details, see the ["Network cluster"](../Platform-Setup/Network-cluster/Configuring-Servers.md) section.
