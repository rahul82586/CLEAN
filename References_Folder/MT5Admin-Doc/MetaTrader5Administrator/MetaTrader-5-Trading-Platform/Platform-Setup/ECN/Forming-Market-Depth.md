[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [ECN](../ECN.md) / Forming Market Depth

[Previous](../ECN.md) | [Next](Market-Depth-Journal.md)

<a id="how-the-market-depth-is-formed"></a>
# How the Market Depth is Formed (#how-the-market-depth-is-formed)

The ECN receives price data from different sources and aggregates them into a single Market Depth. Such data sources include [gateways](../Gateways.md), [datafeeds](../Data-Feeds.md) and the trade servers of the cluster. In other words, the ECN collects data not only from external systems, but also from its own clients.

Traditional symbols are used for collecting data. Create a [separate subgroup of symbols](../Symbols.md) and add these symbols to the ECN section. No special configuration is required for symbols used in the ECN. Set parameters similar to normal trading instruments.

![Creating instruments in the ECN](images/ecn_create_symbol.png)

<a id="common-settings"></a>
## Common Settings (#common-settings)

In common settings, you should specify an earlier created ECN symbol and the following additional parameters:

  * Minimum spread — the minimum spread to be supported in the symbol's Market Depth even when requests at better prices are received. See more details [below (#minimal-spread)](Forming-Market-Depth.md#minimal-spread).
  * Allow to change best prices by client orders — the Market Depth of an ECN instrument can be formed of liquidity providers (gateways) and of orders placed by clients within the trading cluster. The best prices in the Market Depth must always be represented by liquid orders, i.e. by orders which can really be executed. If you have configured the ECN so that client orders are not considered to be valid and do not participate in matching, disable the possibility to change best prices for such orders.
  * Send last deal prices to quotes stream — if this option is disabled, then the prices of ECN symbol deals performed by traders within the cluster will not be sent to the ECN symbol quote stream.



<a id="history"></a>
### History keeping settings (#history)

Specify how long the ECN should store the Market Depth formation and orders matching history.

The Market Depth history is stored as separate Journals, in which each price change is recorded. These changes can be viewed in the separate [Market Depth Journal](Market-Depth-Journal.md) section. Since there can be a lot of changes (millions of entries per day), Journals can take up a large amount of disk space. Therefore, it is not recommended to set the parameter to "unlimited".

Access to the matching history is currency under development.

<a id="minimal-spread"></a>
### Minimum spread (#minimal-spread)

When receiving the Market Depth from different sources and aggregating orders within the cluster, a situation may occur in which both parties are ready to execute the deal at worse conditions than it is possible. For example, a trader on one server is ready to buy an asset at a price of 100, and another trader on a different server is ready to sell the same asset at 90. When matching such requests, the ECN organizing broker will receive profit in the amount of the spread. In this case, source prices must not be sent to the Market Depth. For that purpose the ECN provides the so called "visible price" and the "Minimum spread" parameter. If the actual symbol spread is less than the minimum allowed value, the ECN will modify request prices displayed in the Market Depth. Actual request prices will not be changed, so trades will be performed using actual prices.

Price conversion to meet the minimum spread condition is performed according to the following algorithm:

  * The current Market Depth spread is calculated as the difference between the best Bid and Ask.
  * If the current spread is less than the specified minimum value, a difference between them (delta) is calculated. This is the amount by which the current spread should be increased.
  * New Bid and Ask prices are calculated. Bid New = Bid - floor(spread_delta/2) points. Ask New = Ask + ceil(spread_delta/2) points. Here floor and ceil are standard functions for obtaining the nearest higher and lower integer value.
  * The visible price is set to Bid New for all Buy orders with the price greater than Bid New.
  * The visible price is set to Ask New for all Sell orders with the price lower than Ask New.



Example:

  1. The Market Depth of the EURUSD ECN symbol is formed according to the following rules: Sell items are used from the LMAX source (the EURUSDLMAX symbol), Buy items are provided by Currenex (the EURUSDCNX symbol).
  2. The minimum spread is set to 10 points.
  3. The actual Bid price of EURUSDCNX is 1.17723, while the Ask price of EURUSDLMAX is 1.17725.
  4. When aggregating these prices to the Market Depth, the final spread will be equal to 2 points, i.e. less than the minimum allowable value.
  5. The spread must be increased by 8 points (10 - 2).
  6. Bid New = 1.17723 - floor(8/2) points = 1.17719.
  7. Ask New = 1.17725 + ceil(8/2) points = 1.17729.
  8. The total volume of Buy orders having the price greater than Bid New is transferred to the Bid New level.
  9. The total volume of Sell orders having the price less than Ask New is transferred to the Ask New level.



![Example of conversion of Market Depth orders to meet minimum spread requirements](images/ecn_minimal_spread.png)

<a id="sources"></a>
## Configuration of gateways and datafeeds (#sources)

You need to configure gateways and datafeeds to enable passing of quotes and Market Depth changes to ECN symbols. Each ECN symbol must be appropriately linked to the appropriate symbol on the external system side via gateway/datafeed translation settings:

![Linking ECN symbols with liquidity providers' instruments](images/ecn_gateway_translation.png)

With such settings, all quotes and Market Depth changes for the specified symbol will be passed from the gateway to the ECN. Detailed filtering can be configured in ECN symbol parameters.

If the symbol name in an external system matches the ECN symbol in MetaTrader 5, translation settings are not required.

Also, the gateway must have access to the ECN symbol group. Specify a group of symbols using the mask:

![Enabling access to ECN symbols for the gateway](images/ecn_gateway_symbols.png)

<a id="price-rules"></a>
## Configuring data aggregation from gateways and datafeeds (#price-rules)

Receiving of Market Depth changes from external sources can be configured in detail for each ECN symbol. This can be done in symbol settings, in the "Price rules" tab.

  * If the rules are not set, all data from gateways/datafeeds with appropriate [translation (#sources)](Forming-Market-Depth.md#sources) settings will be added to the Market Depth. By default, all levels from gateways are considered to be liquid, those from datafeeds are considered to be illiquid. Liquid levels can be used for matching orders and forming best prices in the Market Depth.


  * Gateway prices are not considered liquid unless this gateway is connected as a dealer or it has [passed the symbol settings to the external system](https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_gateway_symbols). The last condition is required for the proper processing of prices and trading operations when symbol settings on the platform side and on the external system side differ (different number of decimal places, contract size, etc.).


  * If a gateway or a data feed does not support the order book feature and only translates the best bid/ask prices, its prices will be displayed in the aggregated Market Depth with the volume of 1 lot. If such a price is considered [liquid (#liquid)](Forming-Market-Depth.md#liquid), the ECN will consider the volume of this liquidity to be unlimited. Orders will be forwarded to these sources in any requested volume. The log will contain a clear indication that the request was matched with a tick element of the aggregated Market Depth. Example: "matched 10 at 1.09496, #3245040 buy 10 EURUSD.ECN at market vs sell limit (tick) 1 at 1.09496 on 'LMAX Gateway', by rule 'LMAX'".

  
---  
  
![Rules of accepting prices from external datafeeds](images/ecn_price_rules.png)

Click "Add" and set the rule name. In the "Perform action" field, select the method to process the price:

  * Reject price — the level will be totally rejected. It will not be displayed in the Market Depth and will not be saved in the ECN symbol history.
  * Use the price as liquidity, without displaying it — the level will be shown in the Market Depth, but will not be accepted by the platform. The level will be saved in the database, so it can be used for matching orders.
  * Display price only, without using it as liquidity — the level can appear in the Market Depth but it cannot be used for matching of orders. Such levels are considered to be illiquid and they cannot change the best prices in the order book. The application of this rule to a level does not guarantee that the level will be visible to traders in the Market Depth. This means that the level will not be hidden. For more details please visit the "[Market Depth availability to clients](Forming-Market-Depth.md)" section.



> Price rules cannot turn illiquid prices into liquid or make invisible prices be visible For example, datafeed prices cannot be marked as liquid, as well as prices hidden due to [minimum spread (#minimal-spread)](Forming-Market-Depth.md#minimal-spread) settings cannot be displayed.

Set the conditions that the price must meet in order to be processed according to this rule.

  * Date and time — processing prices received on the specific day and time.
  * Time — processing prices received at a specific time.
  * Day of week — processing prices received on a particular day of the week.
  * Type — processing prices depending on the direction of the offer: Buy or Sell.
  * Volume — processing prices depending on offer volume. For example, you may choose to hide large-volume price levels from the Market Depth.
  * Price — processing specific levels.
  * Gateway or datafeed — processing prices received from the selected gateway or datafeed.
  * Client login — processing request from the specific client trading within the cluster.



All specified rules are checked for each price passed to an ECN symbol.

<a id="aggregation-rules"></a>
## Configuring data aggregation from clients within the cluster (#aggregation-rules)

For each ECN symbol you can set detailed rules, according to which the orders placed by clients within the cluster but not processed by the ECN module directly, will be added to the aggregated Market Depth. Open the "Aggregation rule" tab in ECN symbol settings.

  * The settings do not affect the orders, which were forwarded to the ECN module according to the corresponding [routing rules (#routing)](Order-Matching.md#routing). Such orders are unconditionally displayed in the ECN symbol's Market Depth.


  * These settings only affect the display of client orders in the Market Depth. The orders are considered to be illiquid, so they are not used for matching orders and cannot change the best prices in the Market Depth.
  * If the rules are not set, orders from clients within the cluster will not be added to the Market Depth.

  
---  
  
![Rules for aggregating requests placed by clients within the cluster](images/ecn_aggregation_rules.png)

Click "Add" and set the rule name.

<a id="configuring-transformations"></a>
### Configuring transformations (#configuring-transformations)

You can define markups for client levels, which enable conversion of client orders when displayed in the Market Depth. Specify the desired number of points in the "Bid" and "Ask" fields. A positive value is used to increase the price, a negative one reduces it. For example, if the value of "-3" is specified in the "Bid" field and the client places a Buy Limit order at the price of 1.12286, then the request will appear as 1.12283 in the Market Depth.

Please note that price markups in the aggregation rule have a higher priority than similar settings in [translation rules](Price-Translations.md). For example, EURUSD.ECN data are forwarded to EURUSD.USR with the markups of -2/+2. Clients trade EURUSD.USR at converted prices. The following aggregation rule is set: client requests for the EURUSD.USR symbol are aggregated in the EURUSD.ECN symbol. If zero markups are specified in this rule, during aggregation the ECN will automatically convert client EURUSD.USR requests to source EURUSD.ECN prices. If non-zero markups are specified, the ECN will use them. An example with specific prices: 

  * Source prices in EURUSD.ECN: 1.15651 / 1.15659
  * When passed to EURUSD.USR, the prices are converted according to the markup rule -2/+2: 1.15649 / 1.15661
  * The client sees EURUSD.USR prices and places a Buy Limit orders 20 points below the market, at 1.15629.
  * If zero markups are set in aggregation rules, back conversion will be applied to the client's order: EURUSD.USR -> EURUSD.ECN. Two points will be added to the price: 1.15629 + 0.00002 = 1.15631.
  * If markups are specified in the aggregation rule, for example -5/+5, the client's order will be passed to EURUSD.ECN at a 5 point less price: 1.15629 - 0.00005 = 1.15624.



<a id="conditions"></a>
### Conditions (#conditions)

In the "Where symbol is" field, specify the symbol, which orders will be added to the Market Depth. Order types should be specified in the "Where order is": Buy, Sell. Only limit orders are displayed in the Market Depth. So, the Buy option enables the display of Buy Limit orders, while Sell enables Sell Limit orders.

Set the conditions which the orders must meet in order to be processed according to this rule.

  * Date and time — processing orders received on the specific day and time.
  * Time — processing orders received at a specific time.
  * Day of week — processing orders received on a particular day of the week.
  * Volume — processing orders depending on their volume. For example, you may choose to not display large-volume orders from the Market Depth.
  * Client group — processing orders placed by clients from the specific client group. For example, you may set the rule to only accept orders placed by clients from real groups.
  * Client login — processing orders from the specific client.



In the example shown in the image above, all EURUSD.ECN Market and Limit orders placed by clients from real groups will be added to the EURUSD.ECN Market Depth. Thus, clients trading the ECN symbol will be able to see their own orders in the Market Depth.

<a id="dom-clients"></a>
## Availability of Market Depth (order book) for clients (#dom-clients)

Two order book types (states) are possible in the ECN:

  * Full book is the internal state of the Market Depth in ECN. Prices are passed to it in accordance with the aggregation settings from gateways and the trading cluster.
  * Aggregated book is the Market Depth which is actually shown to clients. Compared to the internal order book, in this state some of the prices can be hidden due to [minimum spread (#minimal-spread)](Forming-Market-Depth.md#minimal-spread) settings, [order book depth (#dom)](../Symbols/Symbol-Settings/Common.md#dom) limitation and [price rules (#price-rules)](Forming-Market-Depth.md#price-rules), as well as depending on [price liquidity (#liquid)](Forming-Market-Depth.md#liquid).



Both order book states can be viewed in the [journal](Market-Depth-Journal.md). Use the context menu to switch between them.

<a id="liquid"></a>
### What is price liquidity and how it is determined (#liquid)

The order book can contain two types of orders: liquid and illiquid. According to this property, these orders can be visible to traders (shown in the aggregated order book) or hidden from them.

  * Liquid orders: these orders can be used to fill client orders (used in matching).
  * Illiquid orders: these orders cannot be used in matching.



Order liquidity is determined by its source and ECN settings:

  * Orders from gateways: an order is liquid if the following conditions are met:


  * The gateway must pass to ECN [symbol settings in the external system](https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_gateway_symbols) (all standard [liquidity gateways](../../Platform-Components/Gateways.md) support this function).
  * The gateway must be connected to the ECN as a [dealer (#routing)](Order-Matching.md#routing) using routing rules.
  * The gateway must be specified as a liquidity provider in [matching rules (#providers)](Order-Matching.md#providers).
  * Orders from datafeeds: these orders are never considered as liquid.
  * Orders from clients within the cluster: these orders are always liquid.



<a id="how-price-liquidity-affects-its-availability-to-traders"></a>
### How price liquidity affects its availability to traders (#how-price-liquidity-affects-its-availability-to-traders)

Only liquid orders can form best prices in the order book for traders (Best Bid/Best Ask). If the price is illiquid and it is currently the best one among all prices, then it will not be shown in the Market Depth for traders. In other words, illiquid prices are shown in traders' order book only if they are not the best.

Liquid prices by default are shown to traders in the order book. In contrast to illiquid prices, such prices are displayed without a check of whether they are currently the best prices. Liquid prices can be forcibly hidden from the traders' order book using [price rules (#price-rules)](Forming-Market-Depth.md#price-rules) (Perform action = Use price as liquidity, without showing).

> If the Market Depth does not contain any liquid price (for example, you have not specified any gateway in [matching rules (#providers)](Order-Matching.md#providers)), the traders will see an empty order book.

<a id="digits"></a>
## Aggregation rules for symbols having different price accuracy on the platform and external system side (#digits)

If the accuracy of security prices on the external system side differs from that in the trading platform, ECN converts these prices when sending to the aggregated Market Depth.

If the accuracy on the platform side is higher, decimal places are added to the prices provided by the external system. Consider the following example. The price accuracy on the platform side is 5 decimal places, while the external system provides prices with 4 decimal places. The price of 1.1329 received from the external system will be displayed as 1.13290 in the aggregated Market Depth feature.

If the accuracy on the platform side is lower, the prices provided by the external system will be rounded according to the following rules:

  * Buy orders are rounded down to the symbol accuracy on the platform side.
  * Sell orders are rounded up to the symbol accuracy on the platform side.



Example: EURUSD.ECN symbol with 4 decimal places exists in the platform. It features aggregated EURUSD prices from the LMAX gateway which provides the prices with 5 decimal places. The Market Depth feature provided to clients will be formed as follows:

![After converting to desired accuracy, levels with the same prices are summed](images/ecn_aggregation_digits.png)

Prices will be converted to the accuracy of 4 decimal points, then levels with the same prices will be combined.

Original data feed prices can be viewed in the [Market Depth journal](Market-Depth-Journal.md). The original price and the price displayed to clients (in brackets) are shown in the Price column:

![Original and converted prices in the Market Depth Journal](images/ecn_aggregation_digits_journal.png)
