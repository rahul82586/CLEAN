[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / First Time Deposit

[Previous](Lifetime-Value.md) | [Next](Retention-of-Trading-Accounts.md)

# First Time Deposit

The report is available as a set of diagrams presenting information about first-time deposits made by clients.

![The "First Time Deposit" report](images/first_time_deposit.png)

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the report will be generated for accounts from the specified groups. You can specify one or several groups separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



### Charts in the report

The report includes three types of charts:

  * FTD — the average value of clients' first deposits.
  * FTD Amount — the total amount of clients' first-time deposits over the selected period.
  * FTD Count — the number of clients' first-time deposits over the selected period.



The first-time deposit is registered per [client](../Clients.md). A client may have multiple trading accounts, so the report will reflect only one deposit (the first one) on one of these accounts.

In addition to the diagram type, you can select from various distribution options based on different parameters:

  * Lead Campaign — the name of an advertising campaign by which the client was attracted.
  * Lead Source — the website from which the client came.
  * Country — the client's country of residence.
  * Value — first-time deposit (different ranges).



  * Balance operation values reflected in charts are automatically converted to the same currency in accordance with current quotes. The report currency is configured on the trade server side.


  * Lead Campaign and Lead Source data are available in appropriate fields of [trading accounts (#leadsource)](../Accounts/Editing-Account.md#leadsource).

  
---  
  
### Setup in MetaTrader 5 Administrator

The additional 'Currency' parameter can be set in the report configuration in MetaTrader 5 Administrator. Appropriate values in reports will be displayed in this currency. Conversion to the specified currency is performed in accordance with the current quotes in the platform. For example, EURUSD quotes are used to convert an amount in EUR to USD.

## First Time Deposit Detailed

This report features the distribution of clients' first-time deposits based on the client property and based on the time.

![The "First Time Deposit Daily" report](images/first_time_deposit_daily.png)

The report features the same metrics and parameters while additionally enabling the analysis of first-time deposit distribution over time.

## First Time Deposit Amount

This report features the distribution of clients' first-time deposits according to different related parameters:

  * Lead Campaign — the name of an advertising campaign by which the client was attracted.
  * Lead Source — the website from which the client came.
  * Country — the client's country of residence.



In addition to groups and dates, the report provides filtering by campaign and lead source.

![The "First Time Deposit Amount" report](images/first_time_deposit_amount.png)
