[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Daily Orders

[Previous](Daily-Trades.md) | [Next](Daily-Positions.md)

# Daily Orders Report

Daily Orders Report features information about [market and pending orders](../../Database-Interfaces/Trade/Orders/IMTOrder.md) which remained open (active) at the end of the selected day.

## Configuration in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting a report:

  * Groups — the report will be generated on accounts listed in these groups.
  * Period — a day, for which the report must be generated.



> [Daily reports (#enreportsmode)](../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enreportsmode) must be enabled on the server for the group containing the necessary accounts, to generate this type of reports.

## Data in the report

The report represents a table with the information about orders:

  * Order — ticket number (unique number) of a trade operation.
  * ID — order ID in the external system.
  * Position — ticket of the position opened, modified or closed due to this order. For "close by" orders, two tickets are displayed: closed position ticket and opposite position ticket.
  * Login — account number.
  * Name — account holder's name.


  * Group — group the account belongs to.


  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Setup time — order setup time. The record has a format of YYYY.MM.DD HH:MM.MSC (year.month.day hour:minute.millisecond).
  * Type — order type: "Buy", "Sell", "Buy Limit", "Sell Limit", "Buy Stop", "Sell Stop", "Buy Stop Limit", "Sell Stop Limit" or "Close By".
  * Symbol — the financial instrument for which the order is placed.
  * Volume — volume requested in the order/executed volume, lots.
  * Price — price specified in the order at which the trade operation should be executed.
  * S/L — Stop Loss level.
  * T/P — Take Profit level.
  * Done time — order execution time. The record has a format of YYYY.MM.DD HH:MM.MSC (year.month.day hour:minute.millisecond).
  * Current price — the current price of the financial instrument for which the order is placed. 
  * Reason — [reason](../../Database-Interfaces/Trade/Orders/IMTOrder/Reason.md) for placing the order.
  * State — [order state](../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) at the end of the day for which the report is generated.
  * Comment — a comment to the order.


