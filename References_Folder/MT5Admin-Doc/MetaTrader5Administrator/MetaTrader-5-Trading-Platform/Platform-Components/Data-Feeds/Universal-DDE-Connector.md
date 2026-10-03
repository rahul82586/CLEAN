[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Data Feeds](../Data-Feeds.md) / Universal DDE Connector

[Previous](Remote-Datafeed.md) | [Next](Universal-DDE-Connector/Installation-and-Setup.md)

# Universal DDE Connector

Universal DDE Connector is a universal gateway that works through protocol DDE (Dynamic Data Exchange). It is used as an intermediary server that accepts quotes from different data sources and passes them to data feed [MetaTrader 5 UniFeeder](MetaTrader-5-UniFeeder.md). Thus, using these two components, you can receive quotes from any data source that supports the DDE protocol.

UniDDE can process up to 1024 financial symbols and distribute quotes to the unlimited number of data feeds [MetaTrader 5 UniFeeder](MetaTrader-5-UniFeeder.md) tuned to it.

This section describes the following aspects of work with UniDDE:

  * Installation and set up of data transmission to the MetaTrader 5 server;
  * Set up of symbols for receiving quotes;
  * Filtering of quotes.


