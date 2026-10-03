[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [History Server](../History-Server.md) / Interaction with Quote Providers

[Previous](Structure-of-Directories-and-Files.md) | [Next](Quotes-Filtration.md)

# Interaction with Quote Providers

In MetaTrader 5, [gateways](../../Platform-Setup/Gateways.md) and [data feeds](../../Platform-Setup/Data-Feeds.md) can be used as providers of quotes. Their interaction with the history server is identical. This interaction can be analyzed in terms of the physical connection and at the level of quotes streaming.

## Physical Connection

The physical connection must be established for each source of quotes enabled in the appropriate settings of the platform. The physical connection details can be configured on the "Timeouts" tab of [gateways (#timeouts)](../../Platform-Setup/Gateways/Configuration-of.md#timeouts) and [data feeds (#timeouts)](../../Platform-Setup/Data-Feeds/Configuration-of.md#timeouts). Let's consider the following configuration example:

  * Interval between reconnections = 5 seconds.
  * Number of reconnection attempts = 10.
  * Interval between series of reconnections = 60 seconds.



If a gateway/data feed loses connection with an external server, a reconnection attempt is made in 5 seconds. If it fails, another one is made in 5 seconds. The total number of attempts is 10. If unable to reconnect, a series of attempts is repeated after a pause of 60 seconds.

## Stream of Quotes

A stream of prices for several symbols goes through each physical connection to a quote provider.

At each point of time, the history server accepts the stream of prices for a certain symbol only from one quote provider, while other price streams of the same symbol are ignored. The source selected for the stream of prices for a symbol is considered a current (active) source for this symbol.

During operation the active source for an instrument may change. It is changed in accordance with [priority (#switching)](../../Platform-Setup/Data-Feeds.md#switching) settings. The priority of data feeds and gateways is determined by their position in the list.

> The priority of [gateways](../../Platform-Setup/Gateways.md), if they are used as a source of quotes, is always higher than that of data feeds.

The stream of prices switches to the source with a [higher priority (#switching)](../../Platform-Setup/Data-Feeds.md#switching) as soon as the first quotes for a symbol is received from that source.

It switches to the source with a lower priority by a timeout. In case no quotes are received from the active quote source during a certain time period (it is specified in the "Datafeeds timeout" parameter in [history server settings (#timeout)](../../Platform-Setup/Network-cluster/Configuring-Servers/History-Server.md#timeout)), then the history server switches to a source with the lower priority that provides quotes for the same symbol.

> The time to wait for a quote for a symbol is defined in the "Datafeeds timeout" parameter in [history server settings (#timeout)](../../Platform-Setup/Network-cluster/Configuring-Servers/History-Server.md#timeout).

After a new quotes source is selected, it is considered active. All cases of server switching to streams from other sources are reflected in the [journal](../../Platform-Setup/Network-cluster/Journal.md) in the form of the following entry:

2011.03.10 10:11:05 Ticks datafeed 4: CHFJPY activation  
---  
  
Here the entry means that for CHFJPY, a stream of quotes from the fourth data feed (a position in the list of data feeds at the moment the entry is made) is selected.
