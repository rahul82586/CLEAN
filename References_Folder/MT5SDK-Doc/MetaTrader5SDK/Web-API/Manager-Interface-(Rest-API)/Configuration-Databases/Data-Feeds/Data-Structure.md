[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / Data Structure

[Previous](../Data-Feeds.md) | [Next](Restart.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

The data feed configuration is passed in JSON format in response to the [/api/feeder/add](Add.md), [/api/feeder/next](Get-by-Index.md) and [/api/feeder/get](Get-by-Name.md) requests.

Parameter | Type | Purpose  
Feeder | String | Data feed configuration name.  
Module | String | The name of the data feed module.  
GatewayServer | String | The address at which the data feed accepts connections from the history and trade servers.  
GatewayLogin | String | Login for authorization of the history and trade servers on data feed.  
GatewayPassword | String | Password for authorization of the history and trade servers on the data feed.  
FeedServer | String | Address of the server to which the data feed connects.  
FeedLogin | String | Login for the authorization of a data feed on the source server.  
FeedPassword | String | Password for the authorization of a data feed on the source server.  
Enable | Integer | Configuration status. Passed as a value of the [EnFeedersMode (#enfeedersmode)](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Enumerations.md#enfeedersmode) enumeration.  
Mode | Integer | Data feed operation mode. Passed as a value of the [EnFeederFlags (#enfeederflags)](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Enumerations.md#enfeederflags) enumeration.  
TimeoutReconnect | Integer | Timeout in seconds between attempts to reconnect to the source server.  
TimeoutSleep | Integer | Timeout in seconds between the series of reconnections to the source server.  
AttemptSleep | Integer | The number of attempts in the series of reconnections to the source server.  
State | Array | [Data feed operation statistics (#state)](Data-Structure.md#state).  
Params | Array | [Data feed parameters (#param)](Data-Structure.md#param).  
Symbols | Array | The list of symbols for which the data feed provides quotes.  
Translates | Array | [Translation settings (#translate)](Data-Structure.md#translate) for the price data transmitted by the data feed.  
  
<a id="state"></a>
## Data feed operation statistics (#state)

Parameter | Type | Purpose  
SysConnection | Integer | The state of the data feed connection to a source: 0 — connected, 1 — disconnected.  
SysLastTime | Integer | The time of the last successful data feed connection to a source in the YYYY-MM-DD HH:MM:SS.MSC format.  
Company | String | The company by which the data feed executable is signed.  
Issuer | String | The certification authority that issued the certificate to the above company.  
TicksStatsCount | Integer | The number of price statistics changes ([MTTickStat](../../../../Structures/MTTickStat.md)) received by the data feed for the current session.  
TicksCount | Integer | Number of price changes ([MTTick](../../../../Structures/MTTick.md)) received by the data feed for the current session.  
BooksCount | Integer | The number of Market Depth changes ([MTBookDiff](../../../../Structures/MTBookMTBookDiff.md)) received by the data feed for the current session.  
NewsCount | Integer | The number OF news items ([MTNews](../../../../Structures/MTNews.md)) received by the data feed for the current session.  
BytesReceived | Integer | The amount of traffic received by the data feed for the current session.  
BytesSent | Integer | The amount of traffic sent by the data feed for the current session.  
StateFlags | Integer | Flags of states. Currently not used.  
  
<a id="param"></a>
## Data Feed Parameters (#param)

Parameter | Type | Purpose  
Type | Integer | Parameter type. Passed as a value of the [ParamType](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Enumerations.md) enumeration.  
Name | Integer | Parameter name.  
Value | String | The value of the parameter.  
  
<a id="translate"></a>
## Translation settings (#translate)

Parameter | Type | Purpose  
Source | String | The symbol name in the data feed, to which the data feed connects.  
Symbol | String | The name of the symbol in the trading platform.  
BidMarkup | Integer | Correction for the Bid price received for a symbol from the data source, to which the data feed connects.  
AskMarkup | Integer | Correction for the Ask price received for a symbol from the data source, to which the data feed connects.  
Digits | Integer | The number of digits after the decimal point in the price of the symbol that receives quotes.  
  
<a id="module"></a>
## Data Feed Module Parameters (#module)

Parameter | Type | Purpose  
Name | String | The data feed name, which is inserted by default to a configuration when this module is selected.  
Module | String | The name of the data feed module file.  
Server | String | The default address of the server to which the data feed module will connect.  
Login | String | The default login that will be used by the data feed to connect to the server.  
Password | String | The default password that will be used by the data feed to connect to the server.  
Copyright | String | Copyright of the data feed module.  
Description | String | Data feed module description.  
Version | Integer | The version of the data feed module.  
Modes | Integer | Available options for data feed module operation. Passed using the [EnFeedersFlags (#enfeederflags)](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Enumerations.md#enfeederflags) enumeration.  
Fields | Integer | Editable data feed fields. Passed using the [EnFeedersFieldFlags (#enfeedersfieldflags)](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederModule/Enumerations.md#enfeedersfieldflags) enumeration.  
VersionAPI | Integer | The version of the Gateway API with which the module is compiled.  
BuildDate | String | Data feed module creation date.  
VersionAPIDate | String | Released date of the Gateway API version with which the module is compiled.  
Params | Array | [Data feed module parameters (#param)](Data-Structure.md#param).
