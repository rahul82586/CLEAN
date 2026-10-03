[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_gateways

[Previous](mt5-time-weekdays.md) | [Next](mt5-gateways-params.md)

# mt5_gateways

Data on the [gateway settings](../../../Platform-Setup/Gateways.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Name | String | Gateway configuration name.  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has been changed.  
Module | String | Gateway module name.  
GatewayServer |  | The address at which the gateway accepts connections from the history and trade servers.  
TradingServer |  | Address of the server to which the gateway connects.  
Enable | Integer | Gateway operation mode: 0 — disabled, 1 — enabled.  
Flags | Integer | Gateway operation flags:

  * 0x00000001 — gateway works as a remote application.
  * 0x00000002 — gateway is allowed to import symbol settings.
  * 0x00000004 — do not broadcast quotes from the gateway in the system.
  * 0x00000008 — gateway can manage clients' balances using IMTExecution::TE_BALANCE_CHANGE and IMTExecution::TE_BALANCE_CORRECT trade executions.
  * 0x00000010 — if enabled, the gateway log receives additional operation data, including the results of measuring the trading operations handling speed. A more detailed information on extended logging is provided in the [Journal of Gateways](../../../Platform-Setup/Gateways/Journal-of.md) section.
  * 0x00000020 — gateway supports requesting the state of external trading system positions. The request is made from the [Positions](../../../Platform-Setup/Gateways/Positions.md) tab of the gateway. 
  * 0x00000040 — collect advanced metrics related to request processing by the gateway.
  * 0x00000100 — gateway is running in demo mode. The mode is checked based on the license at the time the module is loaded.
  * 0x00000200 — gateway is integrated into the platform.

  
Gateway | String | Gateway module name.  
TimeoutReconnect | Integer | Timeout between attempts to reconnect to an external server in seconds.  
TimeoutSleep | Integer | Timeout between the series of reconnections to an external server in seconds.  
AttempsSleep | Integer | Number of attempts in a series of reconnections to an external server.  
ID | Integer | The gateway ID.  
Symbols | Array | The list of symbols for which the gateway provides quotes and processes trading operations.  
SysConnection | Integer | The state of gateway connection to an external trading system: 0 — connected, 1 — disconnected.  
SysLastTime | Integer | The time of the last successful gateway connection to an external trading system in the YYYY-MM-DD HH:MM:SS.MS format.  
Company | String | The company by which the gateway executable is signed.  
Issuer | String | The certification authority that issued the certificate to the above company.  
TickStatsCount | Integer | The number of price statistics changes received by the gateway from the external system for the current session.  
TicksCount | Integer | The number of price changes received by the gateway from the external system for the current session.  
BooksCount | Integer | The number of Market Depth changes received by the gateway from an external trading system for the current session.  
TradeAverageTime | Integer | Average time spent by the gateway to process one trading operation in milliseconds.  
TradeRequestsCount | Integer | The number of trading operations processed by the gateway during the current session.  
BytesReceived | Integer | Traffic volume received by the gateway during the current session.  
BytesSent | Integer | Traffic volume sent by the gateway during the current session.  
StateFlags | Integer | Flags of states. Currently not used.
