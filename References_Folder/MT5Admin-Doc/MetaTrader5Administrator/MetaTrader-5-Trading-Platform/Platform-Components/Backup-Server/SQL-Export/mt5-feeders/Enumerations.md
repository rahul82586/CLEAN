[🏠 Document Start](../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../../Platform-Components.md) / [Backup Server](../../../Backup-Server.md) / [SQL Export](../../SQL-Export.md) / [mt5_feeders](../mt5-feeders.md) / Enumerations

[Previous](../mt5-feeders.md) | [Next](../mt5-feeder-translates.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The following enumerations are used for passing information about data feed configurations:

  * [EnFeederFlags (#enfeederflags)](Enumerations.md#enfeederflags)
  * [EnFeedersFieldFlags (#enfeedersfieldflags)](Enumerations.md#enfeedersfieldflags)



<a id="enfeederflags"></a>
## EnFeederFlags (#enfeederflags)

Flags of predefined data feed settings are listed in EnFeederFlags.

Identifier | Value | Description  
FEED_FLAG_QUOTES | 1 | The data feed sends quotes.  
FEED_FLAG_NEWS | 2 | The data feed sends news.  
FEED_FLAG_REMOTE | 8 | The data feed is running on a remote computer.  
  
<a id="enfeedersfieldflags"></a>
## EnFeedersFieldFlags (#enfeedersfieldflags)

Flags of editable fields are listed in EnFeedersFieldFlags.

Identifier | Value | Description  
FEED_FIELD_SERVER | 1 | The "Server" field.  
FEED_FIELD_LOGIN | 2 | The "Login" field.  
FEED_FIELD_PASS | 4  | The "Password" field.  
FEED_FIELD_PARAM | 8 | The "Parameters" field.
