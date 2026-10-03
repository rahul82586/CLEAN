[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / Enumerations

[Previous](../IMTConHistorySync.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The IMTConHistorySync contains the following enumerations:

  * [IMTConHistorySync::EnHistoryMode (#enhistorymode)](Enumerations.md#enhistorymode)
  * [IMTConHistorySync::EnHistorySyncMode (#enhistorysyncmode)](Enumerations.md#enhistorysyncmode)
  * [IMTConHistorySync::EnHistorySyncServer (#enhistorysyncserver)](Enumerations.md#enhistorysyncserver)
  * [IMTConHistorySync::EnHistorySyncFlags (#enhistorysyncflags)](Enumerations.md#enhistorysyncflags)
  * [IMTConHistorySync::EnHistoryData (#enhistorydata)](Enumerations.md#enhistorydata)



<a id="enhistorymode"></a>
## IMTConHistorySync::EnHistoryMode (#enhistorymode)

States of time synchronization configuration are listed in the IMTConHistorySync::EnHistoryMode enumeration.

ID | Value | Description  
HISTORY_DISABLED | 0 | Synchronization is disabled.  
HISTORY_ENABLED | 1 | Synchronization is enabled.  
HISTORY_FIRST |  | Enumeration beginning. Corresponds to HISTORY_DISABLED.  
HISTORY_LAST |  | End of enumeration. It corresponds to HISTORY_ENABLED.  
  
This enumeration is used in the [IMTConHistorySync::Mode](Mode.md) method.

<a id="enhistorysyncmode"></a>
## IMTConHistorySync::EnHistorySyncMode (#enhistorysyncmode)

History data synchronization modes are listed in IMTConHistorySync::EnHistorySyncMode.

ID | Value | Description  
MODE_REPLACE | 0 | Complete replacement of existing data by the obtained data.  
MODE_MERGE | 1 | Merging obtained and existing data.  
MODE_FIRST |  | Enumeration beginning. It corresponds to MODE_REPLACE.  
MODE_LAST |  | End of enumeration. It corresponds to MODE_MERGE.  
  
This enumeration is used in the [IMTConHistorySync::ModeSync](ModeSync.md) method.

<a id="enhistorysyncserver"></a>
## IMTConHistorySync::EnHistorySyncServer (#enhistorysyncserver)

Type of servers for history data synchronization are listed in IMTConHistorySync::EnHistorySyncServer.

ID | Value | Description  
SERVER_MT4 | 0 | Synchronization with the MetaTrader 4 server.  
SERVER_MT5 | 1 | Synchronization with the MetaTrader 5 server.  
SERVER_FIRST |  | Enumeration beginning. It corresponds to SERVER_MT4.  
SERVER_LAST |  | End of enumeration. It corresponds to SERVER_MT5.  
  
This enumeration is used in the [IMTConHistorySync::ServerType](ServerType.md) method.

<a id="enhistorysyncflags"></a>
## IMTConHistorySync::EnHistorySyncFlags (#enhistorysyncflags)

History data synchronization flags are listed in IMTConHistorySync::EnHistorySyncFlags.

ID | Value | Description  
FLAG_SESSIONS | 1 | If the flag is enabled, the quoting sessions ([IMTConSymbolSession](../../Symbols/IMTConSymbolSession.md)) configured for symbols in your platform will be taken into account during history synchronization. If some of the price data available on the source are outside the quoting sessions of your symbols, these data will not be synchronized (will be skipped). The trading platform will only receive price data within the specified quoting sessions.  
FLAG_SYNONYMS | 2 | If you enable this flag, the system will further synchronize historical data for the symbol, whose "Source" ([IMTConSymbol::Source](../../Symbols/IMTConSymbol/Source.md)) contain one of the symbols [selected for synchronization](SymbolAdd.md).  
FLAG_NONE | 0 | Enumeration beginning. It corresponds to the absence of flags.  
FLAG_ALL |  | End of enumeration. All flags are enabled.  
  
This enumeration is used in the [IMTConHistorySync::Flags](Flags.md) method.

<a id="enhistorydata"></a>
## IMTConHistorySync::EnHistoryData (#enhistorydata)

Types of data to sync are contained in IMTConHistorySync::EnHistoryData.

Identifier | Value | Description  
DATA_HISTORY_CHARTS | 0 | Minute bars.  
DATA_HISTORY_TICKS | 1 | Ticks.  
DATA_HISTORY_ALL | 2 | Minute bars and ticks.  
DATA_HISTORY_FIRST |  | Enumeration beginning. Corresponds to DATA_HISTORY_CHARTS.  
DATA_HISTORY_LAST |  | End of enumeration. Corresponds to DATA_HISTORY_ALL.  
  
The enumeration is used in the [IMTConHistorySync::HistoryData](HistoryData.md) method.
