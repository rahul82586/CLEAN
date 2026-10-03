[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Summary

[Previous](Segregated.md) | [Next](Gateways-Turnover.md)

# Summary Report

Summary Report is a report on a summary motion of funds and funds cycles in the requested accounts over the selected period.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas;
  * Period — starting and ending date of the period, for which the report will be generated.



The report contains the following data:

  * Login — account number.
  * Name — account holder name.


  * Group — group the account belongs to.


  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Deposit — the amount of deposited funds for the specified period.
  * Withdrawal — the amount of withdrawn funds for the specified period.
  * In/Out — difference between Deposit and Withdrawal parameters.
  * Credit — total amount of credit funds submitted to the account for the selected period (difference between provided and withdrawn funds).
  * Additional — total amount of additional tansactions in the account for the selected period. These are additional charges, corrections, bonuses, agent commissions and annual interests.
  * Volume — total amount of all the above mentioned transactions in the account.
  * Commission — commissions debited from the account for the specified period.
  * Fee — amount of [fees (#encommmode)](../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode) debited from the account for the specified period.
  * Swap — swaps withdrawn from the account for the specified period. The amount is calculated based on swap values in deals.
  * Profit — net profit obtained for the selected period.
  * Cur. Balance — account balance at the moment of the report request.
  * Cur. Equity — account equity at the moment of the report request.
  * Currency — account deposit currency.


