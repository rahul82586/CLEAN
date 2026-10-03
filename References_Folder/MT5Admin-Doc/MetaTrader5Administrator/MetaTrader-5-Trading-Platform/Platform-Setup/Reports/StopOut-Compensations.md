[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / StopOut Compensations

[Previous](Trade-Group-Statistics.md) | [Next](Money-Flow-Daily.md)

# StopOuts Compensation Report

StopOuts Compensation Report reflects operations relating to the [compensation of a negative balance after the Stop Out state (#compensate)](../Groups/Group-Settings.md#compensate). All trades with the "so compensation" type are included into this report.

The report features sorting the requested data. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



The following data on each compensation deal is available in the report:

  * Deal — the ticket of the deal.
  * Login — account number.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Group — group the account belongs to.
  * Time — time of the compensation operation.
  * Amount — the compensation amount.
  * Currency — the currency, in which the compensation was performed. Corresponds to the account deposit currency.


