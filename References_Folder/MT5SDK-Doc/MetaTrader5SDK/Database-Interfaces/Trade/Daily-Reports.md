[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Trade](../Trade.md) / Daily Reports

[Previous](Assets/IMTExposureSink/OnExposureUpdate.md) | [Next](Daily-Reports/IMTDaily.md)

# Daily Reports

In the MetaTrader 5 platform, daily reports can be generated for each [group of users](../../Configuration-Interfaces/Groups/IMTConGroup/ReportsMode.md). A database of daily reports is a specialized storage of statuses of trading accounts. Statuses of accounts is saved at [the end of each trading day](../../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md). In addition, daily reports contain other information about an account (status as of the previous day and month, totals for a trading day, etc.).

MetaTrader 5 API interfaces allow obtaining data of users' daily reports. The following daily report interfaces are available:

  * [IMTDaily](Daily-Reports/IMTDaily.md)  
An interface that provides access to all parameters of daily reports.
  * [IMTDailyArray](Daily-Reports/IMTDailyArray.md)  
An interface for working with the arrays of daily reports.
  * [IMTDailySink](Daily-Reports/IMTDailySink.md)  
An interface for handling events associated with change of a database of reports.


