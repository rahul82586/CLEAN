[🏠 Document Start](../README.md) / [Server Reports](README.md) / Daily Detailed

[Previous](Daily.md) | [Next](Daily-Server-Logs.md)

# Daily Detailed Report

Daily Detailed Report is a detailed report on the financial state of the one selected account as of the end of a day.

## Setup

The report features sorting the requested data. Set the following parameters before a request:

  * Groups — number of the account, for which the report should be generated;
  * Period — day, for which the report should be generated. Since the daily data, based on which the report is created, is only generated at the end of the trading day, a current day report cannot be requested.



  * Daily data generation should be enabled for the client or group for which the request is created. Otherwise, the report on them will not be available.
  * If the report for the selected day is not available for some reason (for example, daily data generation was disabled on the server), the system will try to show the next available report.

  
---  
  
The report is divided into several blocks.

## Header

The header contains:

  * Brokerage company name;
  * Account number;
  * Account holder name;
  * Deposit currency;
  * Report generation date.



## Orders

This block contains the table displaying the orders set during the specified day. The table displays all data fields available by orders in the [History (#orders)](../Clients-and-Trading-Accounts/Account-History.md#orders) tab when viewing the account.

## Deals

The deals performed during the selected day are displayed here. The table displays all data fields available by deals in the [History (#deals)](../Clients-and-Trading-Accounts/Account-History.md#deals) tab when viewing the account. Additional parameters are displayed at the bottom of the orders block:

  * Closed P/L — total closed profit/loss at all deals per day.
  * Deposit/Withdrawal — total funds deposited/withdrawn from the account per day.
  * Credit Facility — credit funds deposited/withdrawn from the account per day.
  * Round Commission — commission by orders and positions accumulated during a day/month. Depending on the settings (specified for the group in the Administrator terminal), preliminary commission calculation is performed during a day/month and the appropriate funds are blocked in the account and displayed here. Final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account by the balance operation.  
In case commission is charged immediately during a deal, its value is shown in the Commission field.
  * Additional Operations — financial result of other transactions performed in the account. These are additional charges, corrections, bonuses, agent commissions and annual interests.
  * Total — total sum for the above operations.



## Positions

This block shows the positions remaining open in the account at the moment of the report generation (the end of the selected day). The table displays all data fields available by positions on the [Overview (#positions)](../Clients-and-Trading-Accounts/Account-Overview.md#positions) tab. An additional parameter is displayed at the bottom of the positions block:

  * Floating P/L — floating profit/loss of all open positions at the end of the day.



## Working orders

Active orders (pending and unfilled market orders) are displayed in this block. The table displays all data fields available by orders on the [Overview (#pending)](../Clients-and-Trading-Accounts/Account-Overview.md#pending) tab.

## A/C summary

Summary values of the account are shown here:

  * Closed P/L — total closed profit/loss at all deals per day.
  * Deposit/Withdrawal — total funds deposited/withdrawn from the account per day.
  * Credit Facility — credit funds deposited/withdrawn from the account per day.
  * Round Commission — commission by orders and positions accumulated during a day/month. Depending on the settings (specified for the group in the administrator terminal), preliminary commission calculation is performed during a day/month and the appropriate funds are blocked in the account and displayed here. Final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account by the balance operation.
  * Additional Operations — financial result of other transactions performed in the account. These are additional charges, corrections, bonuses, agent commissions and annual interests.
  * Total — total sum for the above operations.
  * Previous Ledger Balance — balance as of the end of the previous day.
  * Previous Equity — equity as of the end of the previous day.
  * Balance — balance at the end of the day.
  * Equity — equity at the end of the day.
  * Floating P/L — floating profit/loss of all open positions at the end of the day.
  * Margin Requirements — money required to cover open positions as of the end of the day.
  * Free Margin — amount of free margin volume as of the end of the day.


