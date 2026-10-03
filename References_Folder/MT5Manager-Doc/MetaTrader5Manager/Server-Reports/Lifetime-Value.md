[🏠 Document Start](../README.md) / [Server Reports](README.md) / Lifetime Value

[Previous](Money-Flow-Weekly.md) | [Next](First-Time-Deposit.md)

# Lifetime Value

The report presents the generalized LTV picture for accounts from a selected group, which were registered in a certain period.

The report enables the analysis of changes in the client's lifetime value over time, after account registration. Also, the report provides data on the amount and number of deposit operations. Select the distribution type for information display: by Lead Source, by Lead Campaign and by countries. Thus you can evaluate the real effectiveness of each advertising campaign and attraction channel.

![The "Lifetime Value" report](images/life_time_value.png)

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the report will be generated for accounts from the specified groups. You can specify one or several groups separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



### Charts in the report

The report includes multiple charts:

  * LTV by Lifetime and Lead Source / Lead Campaign / Country — the life-time value of accounts is presented with the distribution by Lead Source, Lead Campaign and Country (in three different charts). The lifetime value is calculated as (amount of deposits)/(number of deposits). For example, a period of 2018.08.01-2019.02.01 is selected for the report. The report retrieves data on accounts created during this period (taking into account specified group filtration parameters). The system calculates LTV for each month of account existence with the data accumulation: LTV for the first month, the first two months, the first three months, etc.
  * Deposits Amount by Lifetime and Lead Source / Lead Campaign / Country — deposit values over the entire lifetime, distributed by Lead Source, Lead Campaign and Country (in three different charts). Information is presented separately for each month of the account existence.
  * Deposits Count by Lifetime and Lead Source / Lead Campaign / Country — number of deposit operations over the entire lifetime, distributed by Lead Source, Lead Campaign and Country (in three different charts). Information is presented separately for each month of the account existence.
  * Inactive Clients Count by Lead Source / Lead Campaign / Country — the number of clients who did not make any deposit over the selected period, distributed by Lead Source, Lead Campaign and Country (in three different charts).



  * Balance operation values reflected in charts are automatically converted to the same currency in accordance with current quotes. The report currency is configured on the trade server side.


  * Lead Campaign and Lead Source data are available in appropriate fields of [trading accounts (#leadsource)](../Clients-and-Trading-Accounts/Personal-Data.md#leadsource).

  
---  
  
### Setup in MetaTrader 5 Administrator

The additional 'Currency' parameter can be set in the report configuration in MetaTrader 5 Administrator. Appropriate values in reports will be displayed in this currency. Conversion to the specified currency is performed in accordance with the current quotes in the platform. For example, EURUSD quotes are used to convert an amount in EUR to USD.

## Lifetime Value Daily

This report is similar to the previous one, except that the LTVs and data on deposits are distributed in accordance with client registration dates (account opening dates). Additional filters are available in the report: by Lead Campaign and by Lead Source.

## Lifetime Value Detailed by Client

This report features FTD (first-time deposit) and LTV (lifetime value) metrics concerning your [clients](../Clients-and-Trading-Accounts/Clients.md) rather than separate accounts. The report collects data on all accounts belonging to a client and generates summary information: the date and amount of the first deposit, as well as the amount of deposits on all accounts over a selected period of time.

![Report "Lifetime Value Detailed by Client"](images/life_time_value_detailed.png)

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the report will be generated for accounts from the specified groups. You can specify one or several groups separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.
  * Lead Campaign — the name of an advertising campaign by which the client was attracted.
  * Lead Source — the website from which the client came.



### Data in the report

The report presented as table displaying the following data:

  * Client Id — client identifier.
  * Name — client's name.
  * Country — client's country of residence.
  * Registration Time — client registration date (when the first account owned by the client was opened).
  * First Deposit Time — the date when the first deposit was made.
  * Trading Accounts — the number of the client's trading accounts.
  * Deposits — the number of deposit operations made by the client on all his or her accounts.
  * First Deposit — the amount of the first deposit.
  * Lifetime Value — lifetime value information on all accounts owned by the client. LTV is calculated as (amount of deposits + amount of withdrawals)/(number of deposits + number of withdrawals).



Double click on a table row to open a window with the detailed client information.

> Balance operation values reflected in charts are automatically converted to the same currency in accordance with current quotes. The report currency is configured on the trade server side.

### Setup in MetaTrader 5 Administrator

The additional 'Currency' parameter can be set in the report configuration in MetaTrader 5 Administrator. Appropriate values in reports will be displayed in this currency. Conversion to the specified currency is performed in accordance with the current quotes in the platform. For example, EURUSD quotes are used to convert an amount in EUR to USD.

## Lifetime Value Detailed by Trading Account

This report is similar to the previous one, except that the data is provided by separate trading accounts, not clients.

## Lifetime Value Detailed by Lead Source / Lead Campaign / Country

These reports present summary tables of FTD and LTV, the number and total amount of deposits and withdrawals. The data can be presented in three modes: by attraction channels, campaigns and countries.

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the report will be generated for accounts from the specified groups. You can specify one or several groups separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



### Data in the report

The report presented as table displaying the following data:

  * Lead Campaign — the report presents data concerning this lead campaign.
  * Lead Source — the report presents data concerning this lead source.
  * Country — data concerning this country is presented in the report.
  * Login — the account data for which is presented in the report.
  * LTV — lifetime value. LTV is calculated as (amount of deposits + amount of withdrawals)/(number of deposits + number of withdrawals).
  * Deposits — the number of deposit operations.
  * Deposit Amount — the total amount of all deposits.
  * Deposit Medium — the average deposit amount. The value is calculated as (amount of deposits)/(number of deposits).
  * Withdrawals — the number of withdrawal operations.
  * Withdrawals Amount — the total amount of all withdrawal operations.
  * Withdrawals Medium — the average amount of withdrawals. The value is calculated as (amount of withdrawals)/(number of withdrawals).



> Balance operation values reflected in charts are automatically converted to the same currency in accordance with current quotes. The report currency is configured on the trade server side.

### Setup in MetaTrader 5 Administrator

The additional 'Currency' parameter can be set in the report configuration in MetaTrader 5 Administrator. Appropriate values in reports will be displayed in this currency. Conversion to the specified currency is performed in accordance with the current quotes in the platform. For example, EURUSD quotes are used to convert an amount in EUR to USD.
