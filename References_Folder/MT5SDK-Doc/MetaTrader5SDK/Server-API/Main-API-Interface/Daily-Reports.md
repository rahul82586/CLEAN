[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / Daily Reports

[Previous](News-Database/NewsSend.md) | [Next](Daily-Reports/DailyCreate.md)

# Daily Reports

In the MetaTrader 5 platform, daily reports can be generated for each [group of users](../../Configuration-Interfaces/Groups/IMTConGroup/ReportsMode.md). A database of daily reports is a specialized storage of statuses of trading accounts. Statuses of accounts is saved at [the end of each trading day](../../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md). In addition, daily reports contain other information about an account (status as of the previous day and month, totals for a trading day, etc.).

Functions of the MetaTrader 5 Server API allow receiving information from the daily reports and responding to events associated with changes in the database.

Function | Purpose  
---|---  
[DailyCreate](Daily-Reports/DailyCreate.md) | Create an object of a daily report.  
[DailyCreateArray](Daily-Reports/DailyCreateArray.md) | Create an object of the array of daily reports.  
[DailySubscribe](Daily-Reports/DailySubscribe.md) | Subscribe to events and hooks associated with changes in the database of daily reports.  
[DailyUnsubscribe](Daily-Reports/DailyUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the database of daily reports.  
[DailyGet](Daily-Reports/DailyGet.md) | Get an array of daily reports by the date range and login.  
[DailyGetLight](Daily-Reports/DailyGetLight.md) | Get an array of light daily reports by the date range and login. Unlike full daily reports, light reports do not include open client orders and positions.  
[DailySelectByGroup](Daily-Reports/DailySelectByGroup.md) | Request daily reports from a database for a group of accounts using additional criteria.  
[DailySelectByLogins](Daily-Reports/DailySelectByLogins.md) | Request daily reports from a database for a list of logins using additional criteria.
