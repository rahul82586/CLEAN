[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Orders History

[Previous](Margin-Calls.md) | [Next](Positions-History.md)

# Orders History Report

Orders History Report is a summary report on the orders over the selected period. This report includes all pending orders (filled, canceled, expired, etc.) except for currently active orders (placed).

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas;
  * Period — starting and ending date of the period, for which the report will be generated.



The report contains the following data on the orders:

  * Order — ticket number (unique number) of a trade operation;
  * Login — account number;
  * Name — account holder name;


  * Group — group the account belongs to;


  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Setup time — order setup time. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
  * Type — type of a trade operation: "Buy" — a long position, "Sell" — a short position or names of pending orders "Sell Stop", "Sell Limit", "Buy Stop", "Buy Limit", "Buy Stop Limit" or "Sell Stop Limit".
  * Symbol — a financial instrument of the order;
  * Volume — the volume requested in the order/executed volume, lots;
  * Price — price specified in the order at which the trade operation should be executed;
  * Done time — order execution time;
  * Comment — comments on the order.


