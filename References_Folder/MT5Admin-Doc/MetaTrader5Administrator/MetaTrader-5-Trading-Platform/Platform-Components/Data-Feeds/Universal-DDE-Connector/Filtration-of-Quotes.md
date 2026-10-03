[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Data Feeds](../../Data-Feeds.md) / [Universal DDE Connector](../Universal-DDE-Connector.md) / Filtration of Quotes

[Previous](Setting-Up-Symbols.md) | [Next](UniFeeder-Protocol.md)

<a id="filtration-of-quotes"></a>
# Filtration of Quotes (#filtration-of-quotes)

Universal DDE Connector has the built-in system of automatic filtration of received quotes before they are passed to the [history server](../../History-Server.md). The filtration system consists of several components:

<a id="selecting-the-best-banks"></a>
## Selecting the Best Banks (#selecting-the-best-banks)

One of the most effective ways of cleaning quotes is the automatic selection of the best [banks (#bank)](Setting-Up-Symbols.md#bank) based on statistic data on them. If you tick off "Auto" for the list of banks, UniDDE will start collecting statistics of symbol quotes from banks. Based on this statistics, once a day (except for holidays) several best banks are selected and automatically added to the ["List of banks" (#bank-list)](Setting-Up-Symbols.md#bank-list). Next day filtering of quotes will be performed according to this list. If the selected list of banks is satisfying, you can disable Auto.

> The automatic selection of the list of banks according to the collected results is performed once a day. I.e. the list will be empty the first day.

<a id="white-noise"></a>
## Cleaning from "White" Noise (#white-noise)

For a milder cleaning of the quotes thread from the "white" noise, another new adaptive filtration mechanism is used — ["Automatic filter" (#automatic-filter)](Setting-Up-Symbols.md#automatic-filter). It analyzes the average deviation of received prices and sifts away questionable quotes that fit several template situations.

Very often the thread filtration requires analysis of the next quote for making a decision about the previous questionable price, which may slow down data delivery. But the automatic filter in UniDDE does not allow questionable prices stay longer than half a second. This condition can let some questionable quotes in, but there is one more filtration level described below.

<a id="auto-limit"></a>
## Rough Protection (#auto-limit)

For a rough protection from erroneous price substitution from other symbols the ["Auto Limit" (#auto-limit)](Setting-Up-Symbols.md#auto-limit) mode is used, which doesn't let in new prices if they differ from previous ones by more than the specified number of percents.
