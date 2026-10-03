[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Data Feeds](../Data-Feeds.md) / Restarting

[Previous](Journal-of.md) | [Next](Setup-as-Service.md)

# Restarting Data Feeds

Restart of [data feeds](../Data-Feeds.md) is required when technical problems with quotes or news receipt occur. This procedure can be performed using command "![Restart Datafeeds](images/restart_datafeeds_button.png) Restart Datafeeds" in the [Services](../../MetaTrader-5-Administrator/User-Interface/Main-Menu/Services.md) menu. All working data feeds will be restarted.

Data feeds are restarted automatically in the following cases:

  * If any of the data feed configurations has changed, it is restarted;
  * If the position of the data feed in the list has changed (and therefore its priority has changed), all data feeds are restarted.


