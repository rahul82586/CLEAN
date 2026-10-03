[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Margin Calls

[Previous](Equity.md) | [Next](Orders-History.md)

# Margin Calls Report

Margin Call Report is a report on the state of margin call or stop out accounts.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas;



The report contains the following data concerning the accounts:

  * Login — account number;
  * Name — account holder name;


  * Group — group the account belongs to;
  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Leverage — leverage;
  * Balance — current balance;
  * Credit — current amount of credit funds;
  * Floating P/L — floating profit/loss of all open positions in the account;
  * Equity — current amount of funds;
  * Margin — current amount of funds necessary to cover open positions;
  * Free Margin — current amount of free margin;
  * Margin Limits — a margin level, at which the account enters the state of Margin Call/Stop Out;
  * Margin Level — margin level. It corresponds to the account equity or equity percentage to the margin volume (Equity / Margin * 100) depending on the group settings on the server;
  * Add. Margin — amount of funds necessary to be deposited in the account to be out of Margin Call state;
  * Currency — account deposit currency.


