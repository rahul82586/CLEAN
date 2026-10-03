[🏠 Document Start](../README.md) / [Server Reports](README.md) / Daily Trades

[Previous](Daily-Dealing.md) | [Next](Daily-Orders.md)

# Daily Trades Report

Daily Trade Report is a report on trading operations for a specified day.

## Configuration in MetaTrader 5 Manager

The report features sorting the requested data. Set the following parameters before a request:

  * Groups — report will be generated on accounts listed in these groups.
  * Period — day, for which the report should be generated.



## Configuration in MetaTrader 5 Administrator

Additional parameters are specified in the report configuration of MetaTrader 5 Administrator:

  * Currency — the currency used when displaying various parameters in the report (Balance, Profit, etc.).
  * Top Profit Deals — the number of the most profitable deals to be displayed in the relevant report table. The maximum value is 10,000.
  * Top Loss Deals — the number of deals with the largest losses to be displayed in the relevant report table. The maximum value is 10,000.
  * Top Profit Positions — the number of the most profitable positions to be displayed in the relevant report table. The maximum value is 10,000.
  * Top Loss Positions — the number of positions with the largest losses to be displayed in the relevant report table. The maximum value is 10,000.
  * Top Profit Accounts — the number of accounts with the highest profits to be displayed in the relevant report table. The maximum value is 10,000.



## Diagrams

The report contains several diagrams:

  * Profit and Loss of Clients — distribution of closed profit, closed loss and net profit by accounts.
  * Number of Client Trades — distribution of the number of clients' profitable and loss-making deals.
  * Total Profit/Loss of Current Client Positions — total profit/loss of the current clients' positions.



## Tables

The report contains two tables:

### Daily trades

This report shows 10 most profitable and loss-making deals per day and 10 accounts having the greatest profit for a day.

The following data on the deals is shown:

  * Deal — ticket of a deal.
  * Login — number of an account, at which a deal has been performed.
  * Name — account holder's name.
  * Symbol — symbol, for which a deal was executed.
  * Group — group an account belongs to.


  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Type — deal type (buy/sell).
  * Volume — deal volume in lots.
  * Price — price at which a deal is executed.
  * Swap — swap.
  * Profit, currency — profit/loss in a specified currency.



The following data on the most profitable accounts is displayed:

  * Login — account number.
  * Name — account holder's name.
  * Group — group an account belongs to.
  * Leverage — leverage.
  * Placed Orders — number of active pending orders in an account at the moment of report request.
  * Orders — number of orders in the account history for the selected day.
  * Deals — number of performed deals.
  * Balance, currency — account balance at the moment of the report request.
  * Floating P/L, currency — floating profit/loss on an account at the time of the report request.
  * Closed P/L, currency — closed profit/loss per day.



### Open positions

This table shows 10 most profitable and 10 most loss-making positions as of the end of a day. The following data is displayed for each item:

  * Login — number of an account having an open position.
  * Name — account holder's name.
  * Symbol — symbol, by which a position has been opened.
  * Group — group an account belongs to.
  * Type — position direction (buy/sell).
  * Volume — position volume in lots.
  * Open Price — weighted average position open price.
  * S/L — stop loss level.
  * T/P — take profit level.
  * Market Price — financial instrument price at the moment of a request.
  * Swap — swap.
  * Points — profit/loss in points at the moment of a request.
  * Profit, currency — profit/loss in a specified currency at the moment of a request.


