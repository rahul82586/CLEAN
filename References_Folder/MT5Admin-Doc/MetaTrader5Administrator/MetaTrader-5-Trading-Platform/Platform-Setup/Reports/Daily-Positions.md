[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Daily Positions

[Previous](Daily-Orders.md) | [Next](Daily-Expert-Advisors.md)

# Daily Positions

Daily Positions Report features information about [trading positions](../Positions.md) which remained open at the end of the selected day.

## Configuration in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting a report:

  * Groups — the report will be generated on accounts listed in these groups.
  * Period — a day, for which the report must be generated.



> [Daily reports (#reports)](../Groups/Group-Settings.md#reports) must be enabled on the server for the group containing the necessary accounts, to generate this type of reports.

## Data in the report

The report is presented as a table displaying the following position data:

  * Position — position ticket (unique number).
  * ID — position identifier in the external system.
  * Login — the account of the [number](../Accounts.md) on which the position was opened.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Creation time — position opening time. The record has a format of YYYY.MM.DD HH:MM.MSC (year.month.day hour:minute.millisecond).
  * Action — position type, Buy or Sell.
  * Symbol — financial instrument for which the position as opened.
  * Volume — position volume in lots.
  * Price — weight-average position opening price: (price of deal 1 * volume of deal 1 + ... + price of deal N * volume of deal N) / (volume of deal 1 + ... + volume of deal N). The rounding accuracy of the average weighted price is equal to the number of decimal places in the symbol price plus three additional digits.
  * S/L — Stop Loss level.
  * T/P — Take Profit level.


  * Current price — price of the symbol a position was opened for as of the report generation time.


  * Commission — the amount of position withheld on the position. It is calculated as the sum of commissions on [deals](../Deals.md) by which the position was formed.
  * Fee — total position fees. It is calculated as the sum of fees on deals by which the position was formed.
  * Swap — calculated swaps.
  * Profit — position profit at the end of the selected day.
  * Currency — the currency in which the profit is indicated.
  * Reason — [reason for (#reason)](../Positions.md#reason) opening a position.
  * Comment — a comment to position.


