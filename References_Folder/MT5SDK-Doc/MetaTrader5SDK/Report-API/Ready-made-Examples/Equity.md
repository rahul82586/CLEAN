[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Equity

[Previous](Deposit-and-Withdrawal.md) | [Next](Margin-Calls.md)

# Equity Report

Equity Report is a report on the financial state of the requested accounts as of the end of a day. The accounts are grouped according to their "Comment" field value. This report allows to generate reports on clients' accounts grouping them by custom criteria.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas;
  * Period — starting and ending date of the period, for which the report will be generated. The report is based on daily reports. Therefore, it cannot be generated for the current day, as daily reports are generated only at the end of a day.



> Daily reports generation must be enabled on the server for the appropriate account groups to generate this type of reports.

The report contains the following data:

  * Bank — bank name. Accounts are grouped by a value of this field. The value is taken from the "Comment" field of the client record.
  * Accounts — number of accounts in a group;
  * Prev Balance — sum of accounts balances as of the end of each previous day included in the selected period. It is calculated as Prev Balance for day 1 + Prev Balance for day 2, etc.;
  * Closed P/L — total closed profit/loss in the accounts for the selected period;
  * Deposit — summary total of balance transactions in the accounts for the selected period;
  * Balance — sum of accounts balances as of the end of each day included in the specified period. It is calculated as Balance for day 1 + Balance for day 2, etc.;
  * Floating P/L — total floating profit/loss as of the end of each day included in the specified period. It is calculated as Floating P/L for day 1 + Floating P/L for day 2, etc.;
  * Credit — the amount of credit transactions in the accounts for the specified period;
  * Equity — total amount of funds in the accounts as of the end of each day included in the specified period. It is calculated as Equity for day 1 + Equity for day 2, etc.;
  * Margin — the amount of funds necessary to cover open positions in the accounts as of the end of each day included in the specified period. It is calculated as Margin for day 1 + Margin for day 2, etc.;
  * Free Margin — amount of free margin in the accounts as of the end of each day included in the specified period. It is calculated as Free Margin for day 1 + Free Margin for day 2, etc.;
  * Currency — currency for parameters display.


