[🏠 Document Start](../README.md) / [Server Reports](README.md) / Orders History

[Previous](Margin-Calls.md) | [Next](Positions-History.md)

# Orders History Report

Orders History Report is a summary report on the orders over the selected period. This report includes all pending orders (filled, canceled, expired, etc.) except for currently active orders (placed).

The report features sorting the requested data. Set the following parameters before a request:

  * Groups — groups containing the accounts, on which the report should be created. You can specify one or several accounts separating them by commas;
  * Period — start and end date of the period, for which the report will be generated.



The report contains the following data on the orders:

  * Order — ticket number (unique number) of a trade operation.
  * Login — account number.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Setup time — order setup time. The record has a format of YYYY.MM.DD HH:MM (year.month.day hour:minute).
  * Type — type of a trade operation: Buy — a long position, Sell — a short position or names of pending orders Sell Stop, Sell Limit, Buy Stop, Buy Limit, Buy Stop Limit or Sell Stop Limit.
  * Symbol — financial instrument of an order.
  * Volume — volume requested in the order/executed volume, lots.
  * Price — price specified in an order, at which a trade operation should be executed.
  * Done time — order execution time.
  * Comment — order comments.


