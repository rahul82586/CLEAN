[🏠 Document Start](../README.md) / [Server Reports](README.md) / Deals History

[Previous](Daily-Expert-Advisors.md) | [Next](Deals-Profit.md)

# Deals History Report

Deals History Report is a summary report on the deals over a selected period. The report features sorting the requested data. Set the following parameters before a request:

  * Groups — groups containing the accounts, on which the report should be created. You can specify one or several accounts separating them by commas.
  * Period — start and end date of the period, for which the report will be generated.



The following data is displayed for each deal:

  * Deal — ticket number (a unique identifier) of a deal.
  * ID — ID of a deal in an external trading system.
  * Order — ticket of the order, as a result of which the deal has been performed.
  * Login — number of an account, at which a deal has been performed.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Time — time of a deal. The record has a format of YYYY.MM.DD HH:MM (year.month.day hour:minute).
  * Type — type of a trade operation: Buy — a buy deal, Sell — a sell deal.
  * Entry — direction of the deal: in (market entry), out (market exit), in/out (position reversal).
  * Symbol — financial instrument of the deal.
  * Volume — volume of an executed deal in lots.
  * Price — price, a deal was executed at.
  * Reason — [the reason (#deal-reason)](../Trading-Operations/Viewing-and-Editing.md#deal-reason) for executing the deal.
  * Commission — commission charged for a deal execution.
  * Fee — [fee (#commission-type)](../Managing-Trade-Server-Settings/Spread-Commission-and-Swap.md#commission-type) charged for the deal execution.
  * Swap — swap.
  * Dealer — number of the dealer's account who processed this deal. "0" specified in this field means that the deal was processed without a dealer.
  * Profit — financial result of a deal. For entry deals, zero profit is shown.
  * Currency — account deposit currency.
  * Comment — a comment on a deal.


