[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Daily Trades

[Previous](Daily-Dealing.md) | [Next](Daily-Orders.md)

# Daily Trade Report

Daily Trade Report is a report on trading operations for a specified day.

## Configuration in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report will be created;
  * Period — a day, for which the report must be generated.



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

This report shows 10 most profitable and loss-making deals per day and 10 accounts having the greatest profit for the day.

The following data on the deals is shown:

  * Deal — deal ticket;
  * Login — number of the account, at which the deal has been performed;
  * Name — account holder name;
  * Symbol — symbol, for which a deal is executed;
  * Group — group the account belongs to;


  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Type — deal type (buy/sell);
  * Volume — deal volume in lots;
  * Price — the price, at which the deal was executed;
  * Swap — swap size;
  * Profit, currency — profit/loss in a specified currency.



The following data on the most profitable accounts is displayed:

  * Login — account number;
  * Name — account holder name;
  * Group — group the account belongs to;
  * Leverage — leverage;
  * Placed Orders — number of active pending orders in the account at the moment of report request;
  * Orders — number of orders in the account history for the selected day;
  * Deals — number of performed deals;
  * Balance, currency — account balance at the time of the report request;
  * Floating P/L, currency — floating profit/loss on the account at the time of the report request;
  * Closed P/L, currency — closed profit/loss per day.



### Open positions

This table shows 10 most profitable and 10 most loss-making positions as of the end of the day. The following data is displayed for each item:

  * Login — the number of an account having an open position;
  * Name — account holder name;
  * Symbol — symbol, by which the position has been opened;
  * Group — group the account belongs to;
  * Type — position direction (buy/sell);
  * Volume — position volume in lots;
  * Open Price — weighted average position open price;
  * S/L — Stop Loss level;
  * T/P — Take Profit level;
  * Market Price — financial instrument price at the moment of a request.
  * Swap — swap size;
  * Points — profit/loss in points at the moment of a request;
  * Profit, currency — profit/loss in a specified currency at the moment of a request.


