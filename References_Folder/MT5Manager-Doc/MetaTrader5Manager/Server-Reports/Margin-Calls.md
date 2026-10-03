[🏠 Document Start](../README.md) / [Server Reports](README.md) / Margin Calls

[Previous](Equity.md) | [Next](Orders-History.md)

# Margin Call Report

Margin Call Report is a report on the state of margin call or stop out accounts. The report features sorting the requested data. Before a request, specify the groups the report is to be generated for. Besides, you can specify one or several comma-separated accounts in the Groups field.

The report contains the following data concerning the accounts:

  * Login — account number.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Leverage — leverage.
  * Balance — current balance.
  * Credit — current amount of credit funds.
  * Floating P/L — current floating profit/loss of all open positions in an account.
  * Equity — current amount of funds.
  * Margin — current amount of funds necessary to cover open positions.
  * Free Margin — current amount of free margin.
  * Margin Limits — margin level, at which an account enters the state of Margin Call/Stop Out.
  * Margin Level — margin level. It corresponds to the account equity or equity percentage to the margin volume (Equity / Margin * 100) depending on the group settings on the server.
  * Add. Margin — amount of funds necessary to be deposited in an account to be out of Margin Call.
  * Currency — account deposit currency.


