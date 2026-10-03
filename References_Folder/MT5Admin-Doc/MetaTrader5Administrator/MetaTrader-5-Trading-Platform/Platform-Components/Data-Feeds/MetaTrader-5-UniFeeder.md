[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Data Feeds](../Data-Feeds.md) / MetaTrader 5 UniFeeder

[Previous](Trading-Central-News-Feeder.md) | [Next](Thomson-Reuters-Feeder.md)

# MetaTrader 5 UniFeeder

MetaTrader 5 UniFeeder is the data feed that enables receipt of quotes from the special utility — Universal DDE Connector. This solution is built into the platform, which ensures minimal delays in quote delivery.

## How It Works

Universal DDE Connector allows collecting quotes from different data feeds that support the DDE (Dynamic Data Exchange) protocol. The feeder translates quotes received from it to the MetaTrader 5 history server. More details about the Universal DDE Connector are given in a [separate section](Universal-DDE-Connector.md).

## Setup

The data feed must be added via the [corresponding section](../../Platform-Setup/Data-Feeds.md) of the administrator terminal.

![MetaTrader 5 UniFeeder](images/data_feeds_server_uni.png)

The following parameters should be specified on the ["Common" (#common)](../../Platform-Setup/Data-Feeds/Configuration-of.md#common) tab of the data feed:

  * Module — UniFeeder;
  * Feed server — address of the server where the Universal DDE Connector is installed and [port (#port)](Universal-DDE-Connector/Installation-and-Setup.md#port) for connecting to it, separated by a colon;
  * Feed login — [account (#account)](Universal-DDE-Connector/Installation-and-Setup.md#account), pre-created in the Universal DDE Connector;
  * Password — password of the account.



### Synthetic Quotes

MetaTrader 5 UniFeeder allows receiving quotes on symbols, whose data are not translated through Universal DDE Connector. This is achieved by way of mathematical conversion of other symbols' quotes translated through Universal DDE Connector. Such a calculation method can be applied to non-convertible currencies, whose exchange rate relative to convertible currencies is set by the central bank.

The calculation formulas for the quotes should be specified on the ["Parameters" (#parameters)](../../Platform-Setup/Data-Feeds/Configuration-of.md#parameters) tab of the data feed:

![Parameters](images/data_feeds_parameters_uni.png)

Two fields are available here:

### Parameter

In the "Parameter" field, you should specify the symbol name and its price (Bid or Ask), that will be calculated according to the formula specified in the next field. The symbol name and the price type should be separated by a point, for example: GOLDVND.ask.

  * Symbol whose quotes are calculated must be present in the ["Symbols"](../../Platform-Setup/Symbols.md) section. Make sure that the two names match.
  * Calculation of both Bid and Ask prices is required for all symbols.

  
---  
  
### Value

In this field the calculation formula should be specified. You may use:

  * Symbols — any symbol, whose quotes are received from Universal DDE Connector can be used for calculations. But only one symbol for one formula can be used. Do not forget to specify the price type to use (Bid or Ask). For example, EURUSD.bid.



> A symbol that is used for calculation must exist in the trading platform. In addition, it must be added to the [list of symbols (#symbols)](../../Platform-Setup/Data-Feeds/Configuration-of.md#symbols), the quotes for which are translated by the data feed.

  * Simple mathematical calculations — multiplication (*), division (/), addition (+) and subtraction (-).
  * Brackets — you can use brackets "()" to define the calculation order.



  * You cannot use negative numbers in formulas. Thus "-3 + 5" is incorrect. The correct expression will be "5 - 3".
  * The separator of the integer and fractional part in formulas is also a point, irrespective of the operating system settings.
  * Only one symbol, whose quotes are received from Universal DDE Connector can be used in every formula.
  * Synthetic quotes calculated from other symbols cannot be used in formulas.

  
---  
  
## Additional Settings

On the "Parameters" tab, you can specify additional settings:

  * News Category — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](../../Platform-Setup/Groups.md).
  * Quotes Delay — delay of transmitted quotes in seconds. The maximum duration of quotes delay is 20 minutes (1200 seconds). The flow of delayed quotes is neither thinned out, nor changed. A quote is passed to MetaTrader 5 History Server only after the expiration of delay period since the quote has arrived to Gateway API. If the temporary delay parameter is not defined, the quote delay is not used. Changes in depth of market and price statistics are delayed together with the quotes flow.
  * Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
  * Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
  * Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.


