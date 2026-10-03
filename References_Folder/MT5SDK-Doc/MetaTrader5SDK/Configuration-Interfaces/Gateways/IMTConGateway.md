[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Gateways](../Gateways.md) / IMTConGateway

[Previous](../Gateways.md) | [Next](IMTConGateway/Enumerations.md)

# IMTConGateway

The IMTConGateway class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTConGateway/Release.md) | Delete the current object.  
[Assign](IMTConGateway/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConGateway/Clear.md) | Clear an object.  
[Name](IMTConGateway/Name.md) | Get and set the gateway name.  
[ID](IMTConGateway/ID.md) | Gets and sets the gateway ID.  
[Module](IMTConGateway/Module.md) | Get and set the gateway module name.  
[TradingServer](IMTConGateway/TradingServer.md) | Get and set the address of the server to which the gateway connects.  
[TradingLogin](IMTConGateway/TradingLogin.md) | Get and set a login for the authorization of a gateway on the source server.  
[TradingPassword](IMTConGateway/TradingPassword.md) | Get and set a password for the authorization of a gateway on the source server.  
[Gateway](IMTConGateway/Gateway.md) | Gets the gateway license module name.  
[GatewayServer](IMTConGateway/GatewayServer.md) | Gets and sets the address, at which the gateway will accept connections from the history and trade servers.  
[GatewayLogin](IMTConGateway/GatewayLogin.md) | Gets and sets a login for the authorization of the history and trade servers on the gateway server.  
[GatewayPassword](IMTConGateway/GatewayPassword.md) | Gets a password for the authorization of the trade and history server on the gateway.  
[Mode](IMTConGateway/Mode.md) | Get and set the gateway operation mode.  
[Flags](IMTConGateway/Flags.md) | Get and set the gateway operation options.  
[Timeout](IMTConGateway/Timeout.md) | Get and set the timeout of a gateway before reconnecting. The method is obsolete and is no longer used.  
[TimeoutReconnect](IMTConGateway/TimeoutReconnect.md) | Get and set timeout to wait between attempts to reconnect to an external server.  
[TimeoutSleep](IMTConGateway/TimeoutSleep.md) | Get and set timeout to wait between series of attempts to reconnect to an external server.  
[TimeoutAttempts](IMTConGateway/TimeoutAttempts.md) | Get and set the number of attempts in the series of reconnections to an external server.  
[ParameterAdd](IMTConGateway/ParameterAdd.md) | Add a gateway parameter.  
[ParameterUpdate](IMTConGateway/ParameterUpdate.md) | Update a gateway parameter.  
[ParameterDelete](IMTConGateway/ParameterDelete.md) | Delete a gateway parameter by the index.  
[ParameterClear](IMTConGateway/ParameterClear.md) | Clear the list of gateway parameters.  
[ParameterShift](IMTConGateway/ParameterShift.md) | Change the position of a gateway parameter in the list.  
[ParameterTotal](IMTConGateway/ParameterTotal.md) | Get the number of gateway parameters.  
[ParameterNext](IMTConGateway/ParameterNext.md) | Get the gateway parameters by the index.  
[ParameterGet](IMTConGateway/ParameterGet.md) | Get the gateway parameter by the name.  
[SymbolAdd](IMTConGateway/SymbolAdd.md) | Add a symbol, for which the gateway will transmit quotes and process trade operations.  
[SymbolUpdate](IMTConGateway/SymbolUpdate.md) | Change the symbol with the specified index, for which the gateway transmits quotes and processes trade operations.  
[SymbolShift](IMTConGateway/SymbolShift.md) | Change the position of a symbol in the list of symbols, for which the gateway transmits quotes and processes trade operations.  
[SymbolDelete](IMTConGateway/SymbolDelete.md) | Delete a symbol from the list of symbols processed by the gateway by the index.  
[SymbolClear](IMTConGateway/SymbolClear.md) | Clear the list of symbols processed by the gateway.  
[SymbolTotal](IMTConGateway/SymbolTotal.md) | Get the number of symbol settings in the list of symbols processed by the gateway.  
[SymbolNext](IMTConGateway/SymbolNext.md) | Get a symbol from the list of symbols processed by the gateway by the index.  
[GroupAdd](IMTConGateway/GroupAdd.md) | Add a group, trade operations from which will be processed by the gateway.  
[GroupUpdate](IMTConGateway/GroupUpdate.md) | Change the group with a specified index, trade operations of which are processed by the gateway.  
[GroupShift](IMTConGateway/GroupShift.md) | Change the position of a group in the list of groups processed by the gateway.  
[GroupDelete](IMTConGateway/GroupDelete.md) | Delete a group with a specified index from the list of groups, trade operations of which are processed by the gateway.  
[GroupClear](IMTConGateway/GroupClear.md) | Clear the list of groups, trade operations from which are processed by the gateway.  
[GroupTotal](IMTConGateway/GroupTotal.md) | Get the number of group settings in the list of groups processed by the gateway.  
[GroupNext](IMTConGateway/GroupNext.md) | Get a group from the list of groups processed by the gateway by the index.  
[TranslateAdd](IMTConGateway/TranslateAdd.md) | Add a setting of the price data transmitted by the gateway.  
[TranslateUpdate](IMTConGateway/TranslateUpdate.md) | Update the price data conversion settings of a gateway.  
[TranslateDelete](IMTConGateway/TranslateDelete.md) | Remove a setting of conversion of data transmitted by the gateway by the index.  
[TranslateClear](IMTConGateway/TranslateClear.md) | Clear the list of price data conversion parameters of a gateway.  
[TranslateShift](IMTConGateway/TranslateShift.md) | Shift a setting of conversion of price data transmitted by the gateway in the list.  
[TranslateTotal](IMTConGateway/TranslateTotal.md) | Get the number of settings for converting the price data transmitted by the gateway.  
[TranslateNext](IMTConGateway/TranslateNext.md) | Get a setting of conversion of price data transmitted by the gateway by the index.  
[TranslateGet](IMTConGateway/TranslateGet.md) | Gets a price conversion setting applied to the price data transmitted by the gateway based on the specified symbol name in the trading platform.  
[TranslateGetSource](IMTConGateway/TranslateGetSource.md) | Gets a price conversion setting applied to the price data transmitted by the gateway based on the specified symbol name in the data source.  
[StateConnected](IMTConGateway/StateConnected.md) | Get the state of the gateway connection to an external trading system.  
[StateReceivedTicks](IMTConGateway/StateReceivedTicks.md) | Request number of price changes ([MTTick](../../Structures/MTTick.md)) received by the gateway from an external trading system during the current session.  
[StateReceivedBooks](IMTConGateway/StateReceivedBooks.md) | Request number of the Depth of Market changes ([MTBookDiff](../../Structures/MTBookMTBookDiff.md)) received by the gateway from an external trading system during the current session.  
[StateTrafficIn](IMTConGateway/StateTrafficIn.md) | Request traffic volume received by the gateway during the current session.  
[StateTrafficOut](IMTConGateway/StateTrafficOut.md) | Request traffic volume sent by the gateway during the current session.  
[StateTradesTotal](IMTConGateway/StateTradesTotal.md) | Get a number of trades handled by the gateway during the current session.  
[StateTradesAverageTime](IMTConGateway/StateTradesAverageTime.md) | Get an average time of handling one trade by the gateway.  
  
The IMTConGateway class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnGatewayMode (#engatewaymode)](IMTConGateway/Enumerations.md#engatewaymode) | The gateway operation mode.  
[EnGatewayFlags (#engatewayflags)](IMTConGateway/Enumerations.md#engatewayflags) | The gateway operation options.
