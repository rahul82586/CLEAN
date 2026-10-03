[🏠 Document Start](../README.md) / [Server Reports](README.md) / Positions History

[Previous](Orders-History.md) | [Next](Segregated.md)

# Positions History Report

Positions History Report is a summary report on positions for the selected period.

The platform does not explicitly store the history of positions. The history is presented based on deals executed for the selected period. The platform collects data on deals related to a position (position opening, additional volume, partial and full closure), and then combines the data into one record.

The report only shows the positions that were closed during the selected period. If the position is still open or its close time does not fall within the selected interval, it will not be displayed in history.

## Setup

The following parameters must be specified in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



The report displays the following information on positions:

  * Position — position ticket (unique number). Usually, the position ticket matches the ticket of the order, as a result of which the position was opened.
  * Login — account number on which the position was opened.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Open Time — position opening time. The time is determined based on the first deal.
  * Type — position type, buy or sell.
  * Volume — position volume. For partially closed positions, the report shows the closed volume and the original volume.
  * Symbol — the symbol for which the position was opened.
  * Open Price — the weighted average position opening time: (price of deal 1 * volume of deal 1 + ... + price of deal N * volume of deal N) / (volume of deal 1 + ... + volume of deal N).
  * S / L — position Stop Loss. The value is filled in accordance with the Stop Loss value of the deals by which the position was opened and closed.
  * T / P — position Take Profit. The value is filled in accordance with the Take Profit value of the deals by which the position was opened and closed.
  * Close Time — position closing time. The time is set according to the last deal.
  * Close Price — position closing price.
  * Reason — [reason for (#position-reason)](../Trading-Operations/Viewing-and-Editing.md#position-reason) opening a position.
  * Commission — total commission for all deals related to the position.
  * Fee — total [fee (#commission-type)](../Managing-Trade-Server-Settings/Spread-Commission-and-Swap.md#commission-type) for all deals related to the position.
  * Swap — total swap for all deals related to the position.
  * Profit — total profit from all deals related to the position.
  * Currency — account deposit currency.
  * Comment — comments on the transaction.


