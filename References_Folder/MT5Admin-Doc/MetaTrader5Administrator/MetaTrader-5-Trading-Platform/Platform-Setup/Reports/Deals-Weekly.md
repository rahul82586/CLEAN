[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Deals Weekly

[Previous](Deals-Geography.md) | [Next](Deposit-and-Withdrawal.md)

# Deals Weekly

Use the report to assess your traders' activity. It displays information on executed deals grouped by week. Data can be filtered by groups.

![The "Deals Weekly" report](images/deals_weekly.png)

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



### Charts in the report

The report includes multiple charts grouped into categories:

  * Volume — distribution of deals volume: a total volume diagram and distribution by weeks.
  * Profit Deals Volume — distribution of the volume of profitable deals.
  * Loss Deals Volume — distribution of the volume of losing deals.
  * Profit Amount — distribution of deal profits.
  * Loss Amount — distribution of deal losses.
  * Profit Deals Count — distribution of the number of profitable deals.
  * Loss Deals Count — distribution of the number of losing deals.
  * Profit Deals Volume Average — distribution of the average volume of profitable deals.
  * Loss Deals Volume Average — distribution of the average volume of losing deals.
  * Profit-Loss — the difference between the total profit and total loss from deals.
  * Profit-Loss Accumulated — the accumulated difference between the total profit and total loss from deals.



> The volume of deals is indicated in money. Volumes, profit and loss values are automatically converted to the same currency in accordance with current quotes. The report currency is configured on the trade server side.

### Setup in MetaTrader 5 Administrator

The additional 'Currency' parameter can be set in the report configuration in MetaTrader 5 Administrator. Appropriate values in reports will be displayed in this currency. Conversion to the specified currency is performed in accordance with the current quotes in the platform. For example, EURUSD quotes are used to convert an amount in EUR to USD.
