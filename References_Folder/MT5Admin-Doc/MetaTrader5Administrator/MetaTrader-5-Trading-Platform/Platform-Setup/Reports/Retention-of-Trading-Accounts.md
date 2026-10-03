[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Retention of Trading Accounts

[Previous](First-Time-Deposit.md) | [Next](Retention-of-Clients.md)

# Retention of Trading Accounts

The report visualizes the efficiency of your client retention efforts: activity dynamics during the first month after registration, i.e. the percentage of registered accounts, which connected to the server on the first day, on the second day and so on until the 28th day. The information is displayed in four modes: by registration month, by Lead Source, by Lead Campaign and by country.

![The "Retention of Trading Accounts" report](images/retention_of_trading_accounts.png)

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



### Charts in the report

The report includes multiple charts:

  * Retention by Registration Date — the percentage of accounts with the specified registration date, which connected to the server on the 1st day after registration, on the 2nd day and so on until the 28th day.
  * Retention by Lead Campaign — the percentage of accounts with the specified campaign, which connected to the server on the 1st day, on the 2nd day and so on until the 28th day.
  * Retention by Lead Source — the percentage of accounts with the specified lead source, which connected to the server on the 1st day, on the 2nd day and so on until the 28th day.
  * Retention by Country — the percentage of accounts from the specified country, which connected to the server on the 1st day, on the 2nd day and so on until the 28th day.



> Lead Campaign and Lead Source data are available in appropriate fields of [trading accounts (#leadsource)](../Accounts/Editing-Account.md#leadsource).

### Setup in MetaTrader 5 Administrator

The following parameters can be specified in the report configuration in MetaTrader 5 Administrator:

  * Top Count — the number of data series which will be shown in the report: registration dates, campaigns, sources and countries. The default is 10. Data series with the highest values are selected for the report, while all other series are summed up and are displayed as the "Other" variable.
  * Cache Rebuild Period, sec — the maximum time by which data in the report can lag. Time is specified in seconds. The default is 30. If the latest data in the server cache is within the specified interval from the report request time, the data cache will not be refreshed. It means that the data in the report will not be refreshed in the case of frequent repeated requests. This enables fast generation of reports while avoiding extra server load.


