[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_feeders

[Previous](mt5-routing-conds.md) | [Next](mt5-feeders/Enumerations.md)

# mt5_feeders

Data about [data feed settings](../../../Platform-Setup/Data-Feeds.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Name | String | Get and set the data feed name.  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has been changed.  
Module | String | The name of the data feed module.  
GatewayServer | String | The addresses at which the data feed will accept connections from the history server.  
FeedServer | String | The addresses of the server to which the data feed is connected.  
Enable | Integer | The data feed configuration status: 0 — disabled, 1 — enabled.  
Mode | Integer | Data feed operation mode. Passed using the [EnFeedersMode (#enfeederflags)](mt5-feeders/Enumerations.md#enfeederflags) enumeration as a sum of flags. For example, 1 means that the data feed receives news, 9 — receives news while working in the "remote datafeed" mode.  
Timeout | Integer | Timeout of a data feed before reconnecting.  
TimeoutReconnect | Integer | Timeout between attempts to reconnect to the source server.  
TimeoutSleep | Integer | Timeout between the series of reconnections to the source server.  
AttemptsSleep | Integer | The number of attempts in the series of reconnections to the source server.  
Symbols | String | The list of symbols for which the data feed provides quotes.  
SysConnection | Integer | The status of the data feed connection to a source server. 0 — no connection, 1 — connected.  
SysLastTime | DateTime | The time of the last reconnection to the source server in the YYYY-MM-DD HH:MM:SS.MSC format.  
Company | String | The name of the company who signed the executable file of the data feed.  
Issuer | String | The certification authority that issued the certificate of the above company.  
TickStatsCount | Integer | The amount of price statistics received by the data feed from an external data source during the current session.  
TicksCount | Integer | The number of price changes received by the data feed from an external data source during the current session.  
BooksCount | Integer | The number of Market Depth changes received by the data feed from an external data source during the current session.  
NewsCounts | Integer | The number of news items received by the data feed from an external data source during the current session.  
BytesReceived | Integer | The volume of traffic (in bytes) received by the data feed during the current session.  
BytesSent | Integer | The volume of traffic (in bytes) sent by the data feed during the current session.  
StateFlags | Integer | Flags of states.
