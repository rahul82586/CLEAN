[🏠 Document Start](../README.md) / [Server Reports](README.md) / Segregated

[Previous](Positions-History.md) | [Next](Summary.md)

# Segregated Report

Segregated Report is a summary report on the change of financial state of the requested accounts for a specified period. The report is generated on the basis of daily reports. Thus, each rate is calculated as the difference between its value in the daily report for the last date and the value in the daily report for the first date specified when requesting the report. Summarized data of the accounts (for example, balance, equity and floating profit) are taken from the daily reports generated for the last date within the time range the report is requested for. If there is no report generated for that date, zero value will be displayed.

The report features sorting the requested data. Set the following parameters before a request:

  * Groups — groups containing the accounts, on which the report should be created. You can specify one or several accounts separating them by commas;
  * Period — start and end date of the period, for which the report will be generated.



> The report can only be received if the generation of daily reports is enabled for the appropriate groups on the trade server.

The report contains the following data:

  * Login — account number.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Deposit — total funds deposited/withdrawn from the account per specified period.
  * Credit — final amount of credit funds submitted for the selected period (the difference between provided and withdrawn funds).
  * Commission — commission in the account for the specified period. Both blocked commission (in case they are accumulated within a day/a month and then withdrawn in a single balance deal), and commission charged immediately during a transaction are considered here.
  * Swap — total amount of swaps accumulated during a selected period. The amount is calculated based on swap values in deals.
  * Profit — net profit (profit - loss) obtained for a selected period.
  * Interest — annual interest accrued for a selected period.
  * Balance — balance at the moment of generation of the daily report for the last date within the time range the report is requested for.
  * Floating P/L — floating profit/loss in the account at the moment of generation of the daily report for the last date within the time range the report is requested for.
  * Equity — amount of funds in the account at the moment of generation of the daily report for the last date within the time range the report is requested for.
  * Currency — account deposit currency.


