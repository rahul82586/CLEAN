[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_network_trade_servers

[Previous](mt5-network-history-servers.md) | [Next](mt5-network-backup-servers.md)

# mt5_network_trade_servers

Data on the [trade servers settings](../../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Login | Integer | Server ID.  
DemoMode | Integer | Mode of demo account allocation:

  * 0 — creation of demo accounts is disabled.
  * 1 — prolong the period of demo accounts after connection.
  * 2 — demo accounts with a fixed expiration date.

  
DemoPeriod | Integer | The validity of demo accounts.  
OvernightMode | Integer | The overnight mode.  
OvernightTime | Integer | The time of transition to the next day in minutes after 00:00.  
OvernightTimeLast | DateTime | The time of the last transition to the next day in the YYYY-MM-DD HH:MM:SS.MSC format.  
OvernightTimePrev | DateTime | The time of the penultimate transition to the next day in the YYYY-MM-DD HH:MM:SS.MSC format.  
OvernightDays | Integer | Schedule of operations related to the trading day closure. Set as a sum of flags:

  * 0x00000001 — Sunday
  * 0x00000002 — Monday
  * 0x00000004 — Tuesday
  * 0x00000008 — Wednesday
  * 0x00000010 — Thursday
  * 0x00000020 — Friday
  * 0x00000040 — Saturday

Further flags specify days, on which swaps are charged:

  * 0x00000080 — Sunday
  * 0x00000100 — Monday
  * 0x00000200 — Tuesday
  * 0x00000400 — Wednesday
  * 0x00000800 — Thursday
  * 0x00001000 — Friday
  * 0x00002000 — Saturday

  
OvermonthMode | Integer | The overmonth mode:

  * 0 — on the last day of the month.
  * 1 — on the first day of the month.

  
OvermonthTimeLast | DateTime | The time of the last transition to the next month in the YYYY-MM-DD HH:MM:SS.MSC format.  
OvermonthTimePrev | DateTime | The time of the penultimate transition to the next month in the YYYY-MM-DD HH:MM:SS.MSC format.  
TotalUsers | Integer | The total number of client accounts on the trade server.  
TotalUsersReal | Integer | The total number of real clients on the trade server.  
TotalDeals | Integer | The total number of deals executed on the trade server.  
TotalOrders | Integer | The total number of active orders placed on the trade server.  
TotalOrdersHistory | Integer | The total number of orders in the history on the trade server.  
TotalPositions | Integer | The total number of positions on the trade server.  
LoginsRange | String | Account ranges on the trade server. For example, 1000-1000000,2000001-2999001.  
LoginsRangeUsed | String | Ranges of actually used logins from LoginsRange. For example, 1000-1004,0-0.  
OrdersRange | String | Order ticket ranges on the trade server. For example, 1-1000000,2000001-2999001.  
OrdersRangeUsed | String | Ranges of actually used order tickets from OrdersRange. For example, 1-53,0-0.  
DealsRange | String | Trade ticket ranges on the trade server. For example, 1-1000000,2000001-2999001.  
DealsRangeUsed | String | Ranges of actually used trade tickets and DealsRange. For example, 1-56,0-0.
