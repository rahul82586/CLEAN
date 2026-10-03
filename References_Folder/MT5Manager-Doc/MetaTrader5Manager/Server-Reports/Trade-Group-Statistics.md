[🏠 Document Start](../README.md) / [Server Reports](README.md) / Trade Group Statistics

[Previous](Trade-Performance-Summary.md) | [Next](StopOut-Compensations.md)

# Trade Group Statistics

The comprehensive report provides a wide range of statistical information by groups, such as the number of accounts, commission amounts, the share of trades by terminal types and sources, and more.

## Configuration in MetaTrader 5 Manager

The following parameters should be configures in the Manager terminal before requesting the report:

  * Groups — groups for which account reports should be generated. You can specify one or several accounts separated by commas.
  * Period — the start and end dates of the period for which the report will be generated.



## Information in the report

The information in the report is divided into blocks by group types: real, demo and contest.

  * Group — the group the account belongs to.
  * Accounts — the number of accounts in the group.
  * Deals — the number of deals executed on accounts within the groups during the selected period.
  * Commissions — the total commissions charged for deals during the selected period.
  * Mean commission — average commissions per deal. 
  * Currency — group's deposit currency.
  * Trade: Manual — the share of trades executed manually.
  * Trade: Algo — the share of trades executed using Expert Advisors.
  * Trade: Signals — the share of trades copied through the [Signals](https://www.mql5.com/en/signals) service.
  * Trade: Other — the share of trades executed by [other methods (#deal-reason)](../Trading-Operations/Viewing-and-Editing.md#deal-reason).
  * Terminal: Desktop — the share of trades executed through the desktop trading terminal.
  * Terminal: Mobile — the share of trades executed through the mobile trading terminal.
  * Terminal: Web — the share of trades executed through the web-version of the trading terminal.
  * Terminal: Other — the share of trades executed through other client applications.


