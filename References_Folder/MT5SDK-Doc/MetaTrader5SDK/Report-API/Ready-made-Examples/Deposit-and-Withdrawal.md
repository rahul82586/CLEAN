[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Deposit and Withdrawal

[Previous](Deals-Weekly.md) | [Next](Equity.md)

# Deposit and Withdrawal Report

Deposit and Withdrawal Report is a report on deposit and withdrawal operations over the selected period.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas;
  * Period — starting and ending date of the period, for which the report will be generated.



The following data is displayed for each balance operation:

  * Deal — ID of the deal, in which a balance operation has been executed;
  * Login — number of the account, at which the deals has been performed;
  * Name — account holder name;


  * Group — group the account belongs to;


  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Time — transaction time;
  * Comment — comments on the transaction;
  * Amount — transaction amount. A positive value means that the funds have been credited, while a negative one means that the funds have been withdrawn;
  * Currency — account deposit currency.


