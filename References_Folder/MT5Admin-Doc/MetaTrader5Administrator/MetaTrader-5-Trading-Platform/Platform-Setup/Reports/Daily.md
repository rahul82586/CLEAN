[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Daily

[Previous](Credit-Facility.md) | [Next](Daily-Detailed.md)

# Daily Report

Daily Report is a report on the financial state of the requested accounts as of the end of a day.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas;
  * Period — starting and ending date of the period. The report will be generated for each day in the selected period.



> [Daily reports generation (#reports)](../Groups/Group-Settings.md#reports) must be enabled on the server for the group containing the necessary account to generate this type of reports.

The report contains the following data:

  * Time — date and time, the data is generated for;
  * Login — account number;
  * Name — account holder name;


  * Group — group the account belongs to;
  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Prev Balance — balance at the end of the previous day;
  * Deposit — total funds deposited/withdrawn from the account per day; 
  * Closed P/L — total closed profit/loss at all deals per day.
  * Balance — balance at the end of the day;
  * Credit — credit funds deposited/withdrawn from the account per day;
  * Floating P/L — floating profit/loss of all open positions at the end of the day;
  * Equity — equity at the end of the day;
  * Margin — money required to cover open positions as of the end of the day;
  * Free Margin — amount of free margin volume as of the end of the day;
  * Currency — deposit currency.


