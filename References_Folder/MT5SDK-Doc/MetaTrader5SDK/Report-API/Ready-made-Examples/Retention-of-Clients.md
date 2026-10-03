[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Retention of Clients

[Previous](Retention-of-Trading-Accounts.md) | [Next](NFA.md)

# Retention of Clients

The report visualizes the efficiency of your client retention efforts: trading account activity dynamics during the first month after registration, i.e. the percentage of registered accounts, which connected to the server on the first day, on the second day and so on until the 28th day. The information is displayed in four modes: by registration month, by Lead Source, by Lead Campaign and by country.

![The "Retention of Clients" report](images/retention_of_clients.png)

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
  * Period — starting and ending date of the period, for which the report will be generated.



### Charts in the report

The report includes multiple charts:

  * Retention by Registration Date — the percentage of clients who connected to the server on the 1st day, on the 2nd day and so on until the 28th day.
  * Retention by Lead Campaign — the percentage of clients with a specified campaign, who connected to the server on the 1st day, on the 2nd day and so on until the 28th day.
  * Retention by Lead Source — the percentage of clients with the specified lead source, who connected to the server on the 1st day, on the 2nd day and so on until the 28th day.
  * Retention by Country — the percentage of clients from the specified country, who connected to the server on the 1st day, on the 2nd day and so on until the 28th day.



The report is generated based on [clients](../../Database-Interfaces/Clients/IMTClient.md). A client can have multiple trading accounts, and thus only one (the first) connection from any of the accounts will be reflected in the report.

> Lead Campaign and Lead Source data are available in appropriate fields of [trading accounts](../../Database-Interfaces/Users/IMTUser/LeadCampaign.md).

### Setup in MetaTrader 5 Administrator

The following parameters can be specified in the report configuration in MetaTrader 5 Administrator:

  * Top Count — the number of data series which will be shown in the report: registration dates, campaigns, sources and countries. The default is 10. Data series with the highest values are selected for the report, while all other series are summed up and are displayed as the "Other" variable.
  * Cache Rebuild Period, sec — the maximum time by which data in the report can lag. Time is specified in seconds. The default is 30. If the latest data in the server cache is within the specified interval from the report request time, the data cache will not be refreshed. It means that the data in the report will not be refreshed in the case of frequent repeated requests. This enables fast generation of reports while avoiding extra server load.


