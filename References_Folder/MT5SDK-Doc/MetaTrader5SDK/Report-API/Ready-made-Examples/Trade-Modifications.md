[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Trade Modifications

[Previous](Trade-Transactions.md) | [Next](Trade-Performance-Summary.md)

# Trade Modifications Report

Trade Modification Report — report on manually modified orders, trades and positions. It allows you to easily monitor the work of the platform administrators and managers.

## Configuration in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated. The period is only taken into account for the history of orders and deals. All open and modified positions and orders are included in the report, regardless of their opening date.



## Report Data

The report is divided into four units that provide information on modified open orders, history orders, deals and positions:

• Ticket

• Login

• Open Time

• Type

• Lots

• Symbol

• Open Price

• Market Price

• Swap

• Profit

• Modified

• Administrator

• Manager

• Restore

• Position

• Admin API

• Manager API

• Server API

• Gateway API

Apart from the data on modified operations, reports contain excerpts from the related entries in the trade server journal.
