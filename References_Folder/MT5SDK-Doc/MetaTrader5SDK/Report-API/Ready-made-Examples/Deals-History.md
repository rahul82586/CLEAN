[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Deals History

[Previous](Daily-Expert-Advisors.md) | [Next](Deals-Profit.md)

# Deals History Report

Deals History Report is a summary report on the deals over the selected period.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



The following data is displayed for each deal:

  * Deal — ticket number (a unique identifier) of a deal.
  * ID — ID of a deal in an external trading system.
  * Order — ticket of the order, as a result of which the deal has been performed.
  * Login — number of the account, at which the deal has been performed.
  * Name — account holder name.


  * Group — group the account belongs to.


  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Time — time of the deal. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute).
  * Type — type of a trade operation: "Buy" — a buy deal, "Sell" — a sell deal.
  * Entry — direction of the deal: in (market entry), out (market exit), in/out (position reversal).
  * Symbol — a financial instrument of the deal.
  * Volume — volume of an executed deal in lots.
  * Price — the price, the deal was executed at.
  * Reason — [the reason (#endealreason)](../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealreason) for executing the deal.
  * Commission — commission charged for the deal execution.
  * Fee — [fee (#encommmode)](../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode) charged for the deal execution.
  * Swap — swap size.
  * Profit — financial result of the deal. For entry deals, zero profit is shown.
  * Dealer — number of the dealer's account who processed this deal. "0" specified in this field means that the deal was processed without a dealer.
  * Currency — account deposit currency.
  * Comment — a comment on a deal.


