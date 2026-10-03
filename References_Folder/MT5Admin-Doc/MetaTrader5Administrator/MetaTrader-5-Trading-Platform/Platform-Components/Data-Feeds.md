[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../Platform-Components.md) / Data Feeds

[Previous](Backup-Server/SQL-Export/mt5-gateways-symbols.md) | [Next](Data-Feeds/Dow-Jones-Prime-Tass-News-Feeder.md)

# Data Feeds

Data feeds enable receipt of quotes and news in the online trading platform. They transmit information to [the history server](History-Server.md), from which the are translated to [access points](../Platform-Setup/Network-cluster/Configuring-Servers/Access-Server.md) (data centers) and terminals. The trading platform includes several data feeds that enable receiving of quotes and news from the most popular feed providers:

  * [Dow Jones Prime Tass News Feeder](Data-Feeds/Dow-Jones-Prime-Tass-News-Feeder.md)
  * [DJ News Feeder](Data-Feeds/DJ-News-Feeder.md)
  * [IQFeeder](Data-Feeds/IQFeeder.md)
  * [MetaTrader 4 Feeder](Data-Feeds/MetaTrader-4-Feeder.md)
  * [MetaTrader 5 Feeder](Data-Feeds/MetaTrader-5-Feeder.md)
  * [Trading Central News Feeder](Data-Feeds/Trading-Central-News-Feeder.md)
  * [MetaTrader 5 UniFeeder](Data-Feeds/MetaTrader-5-UniFeeder.md)
  * [Thomson Reuters Feeder](Data-Feeds/Thomson-Reuters-Feeder.md)
  * [RSS News Feeder](Data-Feeds/RSS-News-Feeder.md)
  * [IBTimes News Feeder](Data-Feeds/IBTimes-News-Feeder.md)
  * [ForexPros Feeder](Data-Feeds/ForexPros-Feeder.md)
  * [KnowledgeView News Feeder](Data-Feeds/KnowledgeView-News-Feeder.md)
  * [FXstreet Feeder](Data-Feeds/FXstreet-Feeder.md)
  * [Financial Source News Feeder](Data-Feeds/Financial-Source-News-Feeder.md)
  * [Claws & Horns Feeder](Data-Feeds/Claws-&-Horns-Feeder.md)
  * [UniNewsFeeder ](Data-Feeds/UniNewsFeeder.md)
  * [Alliance News Feeder](Data-Feeds/Alliance-News-Feeder.md)
  * [Newsquawk](Data-Feeds/Newsquawk.md)
  * [Remote Datafeed](Data-Feeds/Remote-Datafeed.md)
  * [Universal DDE Connector](Data-Feeds/Universal-DDE-Connector.md)



Data feeds are executable filed (with extension *.exe) that are run as separate processes. These executable files must be located in the datafeed folder of [the history server (#datafeed)](History-Server/Structure-of-Directories-and-Files.md#datafeed).

> If the data feed file is copied to the above mentioned folder while the platform is operating, the history server needs to be restarted (select it in the ["Network"](../Platform-Setup/Network-cluster.md) section and execute the "![Restart](images/restart_server_button.png) Restart" command in the ["Services"](../MetaTrader-5-Administrator/User-Interface/Main-Menu/Services.md) menu or in the [context menu (#context)](../Platform-Setup/Network-cluster.md#context)). After that refresh configurations in the administrator terminal by pressing "![Refresh configuration](images/refresh_configuration_button.png) Refresh configuration".

In order to use a data feed, connection to the feed provider server needs to be established. Data delivery from a third party vendor is implemented based on a special agreement.
