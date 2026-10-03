[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Risk Appetite

[Previous](Fund-Overview.md) | [Next](Fast-Profit-Deals.md)

# Risk Appetite

The "Risk Appetite" report reflects the risk level accepted by traders.

![The "Risk Appetite" report](images/risk_appetite_report.png)

## Report Data

The report consists of a chart showing the ratio of total profit to total loss and the ratio of Take Profit to Stop Loss, along with a table with detailed variables for each account:

  * Stop Loss, % — the average percentile between the position open price and the Stop Loss level.
  * Take Profit, % — the average percentile between the position open price and the Take Profit level.
  * Loss, % — the average percentile between the position open price and the losing position close price.
  * Profit, % — the average percentile between the position open price and the winning position close price.
  * TP/SL Ratio — the ratio between the earlier mentioned 'Take Profit, %' and 'Stop Loss, %' values.
  * Profit/Loss Ratio — the ratio between 'Profit, %' and 'Loss, %'.



The y-axis shows the number of accounts. Thus, it reflects how many accounts have certain values of profit-to-loss and Take Profit-to-Stop Loss ratio.

The table contains 100 accounts with the highest profit-to-loss ratio.

## Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Lead Source — the website from which the client came.
  * Lead Campaign — the name of an advertising campaign by which the client was attracted.
  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated. The filter sets the time frame for which deals are analyzed.



## Setup in MetaTrader 5 Administrator

The following parameters can be specified in the report configuration in MetaTrader 5 Administrator:

  * Top Count — the number of data series which will be shown in the report: profit-to-risk ratio and Take Profit-to-Stop Loss ratio. The default is 10. Data series with the highest values are selected for the report, while all other series are summed up and are displayed as the "Other" variable.
  * Cache Rebuild Period, sec — the maximum time by which data in the report can lag. This is done in seconds. 30 on default. If the latest data in the server cache is within the specified interval from the report request time, the data cache will not be refreshed. It means that the data in the report will not be refreshed in the case of frequent repeated requests. This enables fast generation of reports while avoiding extra server load.
  * Distribution Percentile, % — parameter indicating the data display percentile. The parameter cuts off the specified percentage of low chart values. The value is set to 80 by default. This means that only 20% of all values are shown in the report, which include the largest profit-to-loss and Take Profit-to-Stop Loss ratios.
  * Minimum Deals — parameter for the minimum number of deals required for an account to be included in the report. Only out deals are counted. The default value is 10. The ratio calculation is considered irrelevant for less deals and the appropriate value is excluded from the report.


