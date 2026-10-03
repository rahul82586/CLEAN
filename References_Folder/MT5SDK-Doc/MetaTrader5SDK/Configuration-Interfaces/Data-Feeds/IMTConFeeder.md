[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Data Feeds](../Data-Feeds.md) / IMTConFeeder

[Previous](../Data-Feeds.md) | [Next](IMTConFeeder/Enumerations.md)

# IMTConFeeder

The IMTConFeeder interface contains methods for configuring data feeds.

Method | Purpose  
---|---  
[Release](IMTConFeeder/Release.md) | Delete the current object.  
[Assign](IMTConFeeder/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConFeeder/Clear.md) | Clear an object.  
[Name](IMTConFeeder/Name.md) | Get and set the data feed name.  
[Module](IMTConFeeder/Module.md) | Get and set the data feed module name.  
[FeedServer](IMTConFeeder/FeedServer.md) | Get and set the address of the server to which the data feed connects.  
[FeedLogin](IMTConFeeder/FeedLogin.md) | Get and set a login for the authorization of a data feed on the source server.  
[FeedPassword](IMTConFeeder/FeedPassword.md) | Get and set a password for the authorization of a data feed on the source server.  
[GatewayServer](IMTConFeeder/GatewayServer.md) | Get and set an address, at which the data feed will receive connections from the history server.  
[GatewayLogin](IMTConFeeder/GatewayLogin.md) | Get and set a login for the authorization of the history server on the data feed.  
[GatewayPassword](IMTConFeeder/GatewayPassword.md) | Get and set a password for the authorization of the history server on the data feed.  
[Mode](IMTConFeeder/Mode.md) | Get and set the data feed operation mode.  
[Flags](IMTConFeeder/Flags.md) | Get and set flags of types of information, which is received from the data feed.  
[Keywords](IMTConFeeder/Keywords.md) | Get and set the key words for the news received from a data feed.  
[Categories](IMTConFeeder/Categories.md) | Get and set the category of news received from a data feed.  
[Timeout](IMTConFeeder/Timeout.md) | Get and set the timeout of a data feed before reconnecting. The method is obsolete and is no longer used.  
[TimeoutReconnect](IMTConFeeder/TimeoutReconnect.md) | Get and set timeout to wait between attempts to reconnect to the source server.  
[TimeoutSleep](IMTConFeeder/TimeoutSleep.md) | Get and set timeout to wait between series of attempts to reconnect to the source server.  
[TimeoutAttempts](IMTConFeeder/TimeoutAttempts.md) | Get and set the number of attempts in the series of reconnections to the source server.  
[ParameterAdd](IMTConFeeder/ParameterAdd.md) | Add a parameter of a data feed.  
[ParameterUpdate](IMTConFeeder/ParameterUpdate.md) | Update a parameter of a data feed.  
[ParameterDelete](IMTConFeeder/ParameterDelete.md) | Delete a parameter of a data feed by its index.  
[ParameterClear](IMTConFeeder/ParameterClear.md) | Clear the list of parameters of a data feed.  
[ParameterShift](IMTConFeeder/ParameterShift.md) | Change the position of the data feed parameter in the list.  
[ParameterTotal](IMTConFeeder/ParameterTotal.md) | Get the number of parameters of data feeds.  
[ParameterNext](IMTConFeeder/ParameterNext.md) | Get a data feed parameter by the index.  
[ParameterGet](IMTConFeeder/ParameterGet.md) | Get a data feed parameter by the name.  
[SymbolAdd](IMTConFeeder/SymbolAdd.md) | Add a symbol for which the data feed will transmit quotes.  
[SymbolUpdate](IMTConFeeder/SymbolUpdate.md) | Change the symbol with a specified index, for which the data feed transmits quotes.  
[SymbolShift](IMTConFeeder/SymbolShift.md) | Change the position of a symbol in the list of symbols transmitted by the data feed.  
[SymbolDelete](IMTConFeeder/SymbolDelete.md) | Remove a symbol from the list of symbols transmitted by the data feed by the index.  
[SymbolClear](IMTConFeeder/SymbolClear.md) | Clear the list of symbols of a data feed.  
[SymbolTotal](IMTConFeeder/SymbolTotal.md) | Get the number of symbol settings in the list transmitted by the data feed.  
[SymbolNext](IMTConFeeder/SymbolNext.md) | Get a symbol from the list of symbols transmitted by the data feed by the index.  
[TranslateAdd](IMTConFeeder/TranslateAdd.md) | Add a setting of conversion of data transmitted by the data feed.  
[TranslateUpdate](IMTConFeeder/TranslateUpdate.md) | Update the data conversion settings of the data feed.  
[TranslateDelete](IMTConFeeder/TranslateDelete.md) | Remove a setting of conversion of data transmitted by the data feed by the index.  
[TranslateClear](IMTConFeeder/TranslateClear.md) | Clear the list of data conversion parameters of a data feed.  
[TranslateShift](IMTConFeeder/TranslateShift.md) | Move a setting of conversion of data transmitted by the data feed in the list.  
[TranslateTotal](IMTConFeeder/TranslateTotal.md) | Get the number of settings for converting data transmitted by the data feed.  
[TranslateNext](IMTConFeeder/TranslateNext.md) | Get a setting of conversion of data transmitted by the data feed by the index.  
[TranslateGet](IMTConFeeder/TranslateGet.md) | Get a setting of conversion of data transmitted by the data feed by the symbol.  
[StateConnected](IMTConFeeder/StateConnected.md) | Get the state of the data feed connection to an external data source.  
[StateReceivedTicks](IMTConFeeder/StateReceivedTicks.md) | Request number of price changes ([MTTick](../../Structures/MTTick.md)), received by the data feed from an external data source during the current session.  
[StateReceivedBooks](IMTConFeeder/StateReceivedBooks.md) | Request number of the Depth of Market changes ([MTBook](../../Structures/MTBookMTBookDiff.md)), received by the data feed from an external data source during the current session.  
[StateReceivedNews](IMTConFeeder/StateReceivedNews.md) | Request number news ([MTNews](../../Structures/MTNews.md)) received by the data feed from an external data source during the current session.  
[StateTrafficIn](IMTConFeeder/StateTrafficIn.md) | Request traffic volume received by the data feed during the current session.  
[StateTrafficOut](IMTConFeeder/StateTrafficOut.md) | Request traffic volume sent by the data feed during the current session.  
  
The IMTConFeeder class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnFeedersFlags (#enfeederflags)](IMTConFeeder/Enumerations.md#enfeederflags) | Predefined settings of a data feed.  
[EnFeedersMode (#enfeedersmode)](IMTConFeeder/Enumerations.md#enfeedersmode) | The data feed operation mode.
