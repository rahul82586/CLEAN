[🏠 Document Start](../README.md) / [Server Reports](README.md) / Trade Modifications

[Previous](Trade-Transactions.md) | [Next](Trade-Performance-Summary.md)

# Trade Modifications Report

Trade Modification Report — report on manually modified orders, trades and positions. It allows you to easily monitor the work of the platform administrators and managers.

## Configuration in MetaTrader 5 Manager

The report features sorting the requested data. Set the following parameters before a request:

  * Groups — groups containing the accounts, on which the report should be created. You can specify one or several accounts separating them by commas.
  * Period — start and end date of the period, for which the report will be generated. The period is only taken into account for the history of orders and deals. All open and modified positions and orders are included in the report, regardless of their opening date.



## Report data

The report is divided into four units that provide information on modified open orders, history orders, deals and positions:

  * Ticket — trade operation number (ticket).
  * Login — client account number.
  * Open Time — trade operation creation time.
  * Type — trade operation type.
  * Lots — operation volume in lots.
  * Symbol — financial instrument of a deal.
  * Open Price — open price.
  * Market Price — current market price.
  * Swap — swap.
  * Profit — profit target in the client deposit currency.
  * Modified — operation modification attributes:
    * Administrator — changed by an administrator.
    * Manager — open price changed by a manager.
    * Restore — restored from the archive.
    * Position — modification attributes are inherited by the deal from a position closed by that deal.
    * Admin API — changed via Manager API administrator interface.
    * Manager API — changed via Manager API manager interface.
    * Server API — changed via Server API.
    * Gateway API — changed via Gateway API.



Apart from the data on modified operations, reports contain excerpts from the related entries in the trade server journal.
