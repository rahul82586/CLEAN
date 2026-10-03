[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Trade Performance Summary

[Previous](Trade-Modifications.md) | [Next](Trade-Group-Statistics.md)

# Trade Performance Summary

The Trade Performance Summary Report is a consolidated report on the trading performance of each account for the selected period.

  * The trading metrics provide a comprehensive analysis of the trading strategy. They assess overall trading activity and intensity, financial results, including profits and losses, and the risk-reward ratio.
  * Trade performance and long/short performance metrics help identify the strengths and weaknesses of the strategy.
  * The analysis of extreme values and profit/loss sequences helps identify potential risks and the strategy's resilience to market changes.



## Configuration in MetaTrader 5 Manager

The following parameters should be configures in the Manager terminal before requesting the report:

  * Groups — groups for which account reports should be generated. You can specify one or several accounts separated by commas.
  * Period — the start and end dates of the period for which the report will be generated.



## Information in the report

The report contains the following information:

  * Login — account number.
  * Name — account holder's name.
  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Terminal — type of the terminal from which the last trading operation was performed.
  * Registration — registration date.
  * Last access — last connection date.
  * Lifetime days — the number of days from the date of registration to the date of last connection.
  * Total deals — the total number of deals.
  * Total trades — the total number of trades (deals that recorded a financial result).
  * Total net profit — total profit/loss for the entire trading period. Considers all profitable and losing trades.
  * Gross profit — the total value of all profitable trades in monetary units.
  * Gross loss — the total value of all losing trades in monetary units.
  * Profit factor — the ratio of the total gross profit to the total gross loss: Gross profit / Gross loss. One means that the gross profit is equal to the gross loss.
  * Expected payoff — the anticipated return from a deal. Calculated as Total net profit / Total trades and reflects the average profit/loss per trade.
  * Payoff ratio — the ratio of the average profit per trade to the average loss per trade: Average profit trade / Average loss trade.
  * Tharp expectancy — expected profitability of the trading system per trade: Expected payoff / -Average loss trade. Reflects the average return per dollar at risk.
  * Profit trades — the number of profitable trades.
  * Profit (%) — the percentage of profitable trades relative to the total number of trades.
  * Loss trades — the number of losing trades.
  * Loss (%) — the percentage of losing trades relative to the total number of trades.
  * Long trades — the number of Buy trades
  * Long trades profit — profit from Buy trades
  * Long trades loss — loss from Buy trades.
  * Long (%) — the percentage of profitable Buy trades.
  * Short trades — the number of Sell trades.
  * Short trades profit — profit from Sell trades.
  * Short trades loss — loss form Sell trades.
  * Short (%) — the percent of Sell trades.
  * Best trade — the trade with the highest profit.
  * Worst trade — the trade with the highest loss.
  * Average profit trade — average profit per profitable trade: Gross profit / Profit trades.
  * Average loss trade — average loss per losing trade: Gross loss / Loss trades.
  * Max Consecutive Wins — the maximum number of consecutive profitable trades.
  * Max Consecutive Losses — the maximum number of consecutive losing trades.
  * Max Consecutive Profit — the maximum profit in a series of consecutive trades.
  * Max Consecutive Loss — the maximum loss in a series of consecutive trades.


  * Account Comment — comment to the accounts.


