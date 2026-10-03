[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Deals Profit

[Previous](Deals-History.md) | [Next](Deals-Initiators.md)

# Deals Profit

A detailed deal report for the selected period. It consists of several diagrams: by deal volume with distribution by profitable and losing trades, by profit, loss, total number and other metrics.

![The "Deals Profit" report](images/deals_profit.png)

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.
  * Lead Campaign — the name of an advertising campaign by which the client, who has executed the deal, was attracted.
  * Lead Source — the website from which the client, who has executed the deal, came.



### Charts in the report

The report includes multiple charts:

  * Volume — distribution of the total volume of deals, the volume of profitable deals and the volume of losing deals.
  * Profit Amount — distribution of deals profits and losses.
  * Profit Deals Count — distribution of the number of profitable and losing deals.
  * Profit Deals Volume Average — distribution of the average volume of profitable and losing deals.
  * Profit-Loss — the difference between the total profit and total loss from deals.
  * Profit-Loss Accumulated — the accumulated difference between the total profit and total loss from deals.



> The volume of deals is indicated in money. Volumes, profit and loss values are automatically converted to the same currency in accordance with current quotes. The report currency is configured on the trade server side.

### Setup in MetaTrader 5 Administrator

The additional 'Currency' parameter can be set in the report configuration in MetaTrader 5 Administrator. Appropriate values in reports will be displayed in this currency. Conversion to the specified currency is performed in accordance with the current quotes in the platform. For example, EURUSD quotes are used to convert an amount in EUR to USD.
