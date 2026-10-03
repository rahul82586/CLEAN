[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / Data Structure

[Previous](../Gateways.md) | [Next](Restart.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Gateway configuration is passed in JSON format in response to the [/api/gateway/add](Add.md), [/api/gateway/next](Get-by-Index.md) and [/api/gateway/get](Get-by-Name.md) requests.

Method | Type | Purpose  
Name | String | Gateway name.  
Module | String | Gateway module name.  
GatewayServer | String | The address at which the gateway accepts connections from the history and trade servers.  
GatewayLogin | String | Login for authorization of the history and trade servers on the gateway.  
GatewayPassword | String | Password for authorization of the history and trade servers on the gateway.  
TradingServer | String | Address of the server to which the gateway connects.  
TradingLogin | String | Login for the authorization of a gateway on the source server.  
TradingPassword | String | Password for the authorization of a gateway on the source server.  
Enable | Integer | Gateway operation mode. Passed as a value of the [EnGatewayMode (#engatewaymode)](../../../../Configuration-Interfaces/Gateways/IMTConGateway/Enumerations.md#engatewaymode) enumeration .  
Flags | Integer | Gateway operation options. Passed using the [EnGatewayFlags (#engatewayflags)](../../../../Configuration-Interfaces/Gateways/IMTConGateway/Enumerations.md#engatewayflags) enumeration.  
ID | Integer | The gateway ID.  
Gateway | String | Gateway license module name.  
AccountSummary | Integer | Account number on which all gateway positions are displayed.  
TimeoutReconnect | Integer | Timeout in seconds to wait between attempts to reconnect to an external server.  
TimeoutSleep | Integer | Timeout in seconds between the series of reconnections to an external server.  
TimeoutAttempts | Integer | Number of attempts in a series of reconnections to an external server.  
State | Array | [Gateway operation statistics (#state)](Data-Structure.md#state).  
Params | Array | [Gateway parameters (#param)](Data-Structure.md#param).  
Symbols | Array | The list of symbols for which the gateway provides quotes and processes trading operations.  
Groups | Array | The list of groups whose trading operations are processed by the gateway.  
Translates | Array | [Translation settings (#translate)](Data-Structure.md#translate) for the price data transmitted by the gateway.  
  
<a id="state"></a>
## Gateway operation statistics (#state)

Parameter | Type | Purpose  
SysConnection | Integer | The state of gateway connection to an external trading system: 0 — connected, 1 — disconnected.  
SysLastTime | Integer | The time of the last successful gateway connection to an external trading system in the YYYY-MM-DD HH:MM:SS.MSC format.  
Company | String | The company by which the gateway executable is signed.  
Issuer | String | The certification authority that issued the certificate to the above company.  
StateReceivedTicks | Integer | The number of price changes ([MTTick](../../../../Structures/MTTick.md)) received by the gateway from the external system for the current session.  
StateReceivedBooks | Integer | The number of Market Depth changes ([MTBookDiff](../../../../Structures/MTBookMTBookDiff.md)) received by the gateway from an external trading system for the current session.  
TradeAverageTime | Integer | Average time in milliseconds spent by the gateway to process one trading operation.  
TradeRequestsCount | Integer | The number of trading operations processed by the gateway during the current session.  
BytesReceived | Integer | Traffic volume received by the gateway during the current session.  
BytesSent | Integer | Traffic volume sent by the gateway during the current session.  
StateFlags | Integer | Flags of states. Currently not used.  
  
<a id="param"></a>
## Gateway parameters (#param)

Parameter | Type | Purpose  
Type | Integer | Parameter type. Passed as a value of the [ParamType](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Enumerations.md) enumeration.  
Name | Integer | Parameter name.  
Value | String | Parameter value.  
  
<a id="translate"></a>
## Translation settings (#translate)

Parameter | Type | Purpose  
Source | String | The symbol name in the data feed, to which the gateway connects.  
Symbol | String | The name of the symbol in the trading platform.  
BidMarkup | Integer | Correction for the Bid price received for a symbol from the data source, to which the gateway connects.  
AskMarkup | Integer | Correction for the Ask price received for a symbol from the data source, to which the gateway connects.  
Digits | Integer | The number of digits after the decimal point in the price of the symbol that receives quotes.  
  
<a id="module"></a>
## Gateway module parameters (#module)

Parameter | Type | Purpose  
Name | String | The gateway name, which is inserted by default to a configuration when this module is selected.  
Module | String | The name of the gateway module file.  
Gateway | String | Gateway module name.  
Server | String | The default address of the server to which the gateway module will connect.  
Login | String | The default login that will be used by the gateway to connect to the server.  
Password | String | The default password that will be used by a gateway to connect to the server.  
Copyright | String | Copyright of the gateway module.  
Description | String | Gateway module description.  
Version | Integer | The version of the gateway module.  
Flags | Integer | Available options for gateway module operation. Passed using the [EnGatewayFlags (#engatewayflags)](../../../../Configuration-Interfaces/Gateways/IMTConGateway/Enumerations.md#engatewayflags) enumeration.  
Fields | Integer | Editable gateway fields. Passed using the [EnGatewayFieldMask](../../../../Configuration-Interfaces/Gateways/IMTConGatewayModule/Enumerations.md) enumeration.  
VersionAPI | Integer | The version of the Gateway API with which the module is compiled.  
BuildDate | String | Gateway module creation date.  
VersionAPIDate | String | Released date of the Gateway API version with which the module is compiled.  
Params | Array | [Gateway module parameters (#param)](Data-Structure.md#param).
