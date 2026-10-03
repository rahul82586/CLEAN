[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [History Synchronization](../History-Synchronization.md) / IMTConHistorySync

[Previous](../History-Synchronization.md) | [Next](IMTConHistorySync/Enumerations.md)

# IMTConHistorySync

The IMTConHistorySync class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTConHistorySync/Release.md) | Delete the current object.  
[Assign](IMTConHistorySync/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConHistorySync/Clear.md) | Clear an object.  
[Server](IMTConHistorySync/Server.md) | Get and set the IP address or the domain name of the server, with which history data are synchronized.  
[ServerType](IMTConHistorySync/ServerType.md) | Get and set the type of the server with which history data are synchronized.  
[Login](IMTConHistorySync/Login.md) | Get and set the trading account login used to connect to the server the data is synchronized with.  
[Password](IMTConHistorySync/Password.md) | Get and set the trading account password used to connect to the server the data is synchronized with.  
[Mode](IMTConHistorySync/Mode.md) | Get and set the state of the configuration of data synchronization.  
[ModeSync](IMTConHistorySync/ModeSync.md) | Get and set the mode of history data synchronization.  
[HistoryData](IMTConHistorySync/HistoryData.md) | Get and set the type of data to synchronize.  
[TimeCorrection](IMTConHistorySync/TimeCorrection.md) | Get and set the correction of the time zone of the synchronization server relative to the time zone of the platform.  
[From](IMTConHistorySync/From.md) | Get and set the beginning date of the period for which history data are synchronized.  
[To](IMTConHistorySync/To.md) | Get and set the end date of the period for which history data are synchronized.  
[SymbolAdd](IMTConHistorySync/SymbolAdd.md) | Add a symbol for which history data will be synchronized.  
[SymbolUpdate](IMTConHistorySync/SymbolUpdate.md) | Modify the symbol for which history data are synchronized, based on the position in the list.  
[SymbolShift](IMTConHistorySync/SymbolShift.md) | Change the position of a symbol for which history data are synchronized.  
[SymbolDelete](IMTConHistorySync/SymbolDelete.md) | Delete a symbol for which history data are synchronized, based on the position in the list.  
[SymbolTotal](IMTConHistorySync/SymbolTotal.md) | Get the entries in the list of symbols, for which history data are synchronized.  
[SymbolNext](IMTConHistorySync/SymbolNext.md) | Get a symbol for which history data are synchronized, based on the position in the list.  
[Flags](IMTConHistorySync/Flags.md) | Get and set data synchronization flags.  
  
The IMTConHistorySync contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnHistoryMode (#enhistorymode)](IMTConHistorySync/Enumerations.md#enhistorymode) | The state of the configuration of history data synchronization.  
[EnHistorySyncMode (#enhistorysyncmode)](IMTConHistorySync/Enumerations.md#enhistorysyncmode) | History data synchronization mode.  
[EnHistorySyncServer (#enhistorysyncserver)](IMTConHistorySync/Enumerations.md#enhistorysyncserver) | Type of the server for synchronization.  
[EnHistorySyncFlags (#enhistorysyncflags)](IMTConHistorySync/Enumerations.md#enhistorysyncflags) | History data synchronization flags.
