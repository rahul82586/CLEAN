[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Daily Detailed

[Previous](Daily.md) | [Next](Daily-Server-Logs.md)

# Daily Detailed Report

Daily Detailed Report is a detailed report on the financial state of the one selected account as of the end of a day.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — number of the account, for which the report must be generated;
  * Period — a day, for which the report must be generated. Since the daily data, based on which the report is created, is only generated at the end of the trading day, a current day report cannot be requested.



  * [Daily data generation (#reports)](../Groups/Group-Settings.md#reports) should be enabled for the client or group for which the request is created. Otherwise, the report on them will not be available.
  * If the report for the selected day is not available for some reason (for example, daily data generation was disabled on the server), the system will try to show the next available report.

  
---  
  
The report is divided into several blocks.

## Header

The following data is specified here:

  * Brokerage company name;
  * Account number;
  * Account holder name;
  * Deposit currency;
  * Report generation date.



## Orders

This block contains the table displaying the orders set during the specified day. The table displays all data fields available by orders in the ["Orders"](../Orders.md) section.

## Deals

The deals performed during the selected day are displayed here. The table displays all data fields available by deals in the ["Deals"](../Deals.md) section. Additional parameters are displayed at the bottom of the orders block:

  * Closed P/L — total closed profit/loss at all deals per day.
  * Deposit/Withdrawal — total funds deposited/withdrawn from the account per day; 
  * Credit Facility — credit funds deposited/withdrawn from the account per day;
  * Round Commission — commission by orders and positions accumulated during a day/month. Depending on the settings (specified for the group in the administrator terminal), preliminary commission calculation is performed during a day/month and the appropriate funds are blocked in the account and displayed here. Final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account by the balance operation.  
In case commission is charged immediately during a deal, its value is shown in the "Commission" field.
  * Additional Operations — financial result of other transactions performed in the account. These are additional charges, corrections, bonuses, agent commissions and annual interests;
  * Total — total sum for the above operations.



## Positions

This block shows the positions remaining open in the account at the moment of the report generation (the end of the selected day). The table displays all data fields available by positions in the ["Positions"](../Positions.md) section. Additional parameter is displayed at the bottom of the positions block:

  * Floating P/L — floating profit/loss of all open positions at the end of the day.



## Working Orders

Active [orders](../Orders.md) (pending and unfilled market orders) are displayed in this block.

## A/C Summary

This block displays the aggregate account figures:

  * Closed P/L — total closed profit/loss at all deals per day.
  * Deposit/Withdrawal — total funds deposited/withdrawn from the account per day; 
  * Credit Facility — credit funds deposited/withdrawn from the account per day;
  * Round Commission — commission by orders and positions accumulated during a day/month. Depending on the settings (specified for the group in the administrator terminal), preliminary commission calculation is performed during a day/month and the appropriate funds are blocked in the account and displayed here. Final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account by the balance operation.
  * Additional Operations — financial result of other transactions performed in the account. These are additional charges, corrections, bonuses, agent commissions and annual interests;
  * Total — total sum for the above operations;
  * Previous Ledger Balance — balance as of the end of the previous day;
  * Previous Equity — equity as of the end of the previous day;
  * Balance — balance at the end of the day;
  * Equity — equity at the end of the day;
  * Floating P/L — floating profit/loss of all open positions at the end of the day;
  * Margin Requirements — money required to cover open positions as of the end of the day;
  * Free Margin — amount of free margin volume as of the end of the day.


