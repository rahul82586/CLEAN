[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Main Interface](../Main-Interface.md) / Quote and News Feeds

[Previous](Client-Connection/ClientAllowIP.md) | [Next](Quote-and-News-Feeds/SendTickStats.md)

<a id="quote-and-news-streams"></a>
# Quote and News Streams (#quote-and-news-streams)

The functions described in this section allow sending quiting data and news to the platform. The following functions are provided:

Function | Purpose  
---|---  
[SendTickStats](Quote-and-News-Feeds/SendTickStats.md) | Sending statistical information about a financial instrument.  
[SendTicks](Quote-and-News-Feeds/SendTicks.md) | Sending current prices.  
[SendBookDiffs](Quote-and-News-Feeds/SendBookDiffs.md) | Sending the Depth of Market changes.  
[SendBooks](Quote-and-News-Feeds/SendBooks.md) | Sending the entire state of the Depth of Market.  
[SendNews](Quote-and-News-Feeds/SendNews.md) | Sending news.  
[SendEconomicEvents](Quote-and-News-Feeds/SendEconomicEvents.md) | Sending economic calendar events. The method is obsolete and is not supported.  
  
<a id="charts"></a>
## Chart Construction (#charts)

The trading platform (the history server) builds bars using ticks received from datafeeds and gateways. Depending on the [IMTConSymbol::ChartMode](../../Configuration-Interfaces/Symbols/IMTConSymbol/ChartMode.md) parameter, financial symbol bars are based on Bid or Last prices (the price of the last executed trade). As a rule, charts of exchange instruments with the enabled Market Depth feature are based on the Last price.

For the symbols, the charts of which are based on Bid prices, the history server does no accept Last prices and volumes from gateways and datafeeds. Such ticks are not saved and are not provided to other components of the platform. Therefore, when sending quotes using the [IMTGatewayAPI::SendTicks](Quote-and-News-Feeds/SendTicks.md) method, you should not fill the [MTTick::last](../../Structures/MTTick.md) and [MTTick::volume](../../Structures/MTTick.md) fields.

If a data feed or gateway sends symbol Market Depth changes to a platform ([IMTGatewayAPI::SendBookDiffs](Quote-and-News-Feeds/SendBookDiffs.md), [IMTGatewayAPI::SendBooks](Quote-and-News-Feeds/SendBooks.md)), the history server automatically monitors changes of the best Bid and Ask price in it. If the best Bid or Ask price has changed, the history server generates a tick with the values ​​of the best Bid and Ask prices. In this tick, the value of the last trade price and the volume will be zero. The gateway/datafeed must only send ticks with the filled Last price and volume value. The network traffic is saved, because Bid and Ask prices are not sent.

> For operations with the symbol's price history, use methods [IMTGatewayAPI::Chart*](History-Data.md) and [IMTGatewayAPI::TickHistory*](Tick-Data.md).
