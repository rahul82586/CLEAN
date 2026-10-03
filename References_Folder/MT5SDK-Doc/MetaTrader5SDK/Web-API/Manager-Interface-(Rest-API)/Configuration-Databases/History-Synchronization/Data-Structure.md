[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / Data Structure

[Previous](../History-Synchronization.md) | [Next](Start.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

A configuration is passed in JSON format in response to the [/api/history_sync/add](Add.md) and [/api/history_sync/next](Get-by-Index.md) requests.

Method | Type | Purpose  
Enable | Integer | Synchronization mode: 0 — disabled, 1 — enabled.  
Server | String | The IP address or the domain name of the server, which which historical data is synchronized.  
ServerType | Integer | The type of the server with which historical data is synchronized. Passed as a value of the [EnHistorySyncServer (#enhistorysyncserver)](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySync/Enumerations.md#enhistorysyncserver) enumeration.  
Mode | Integer | Historical data synchronization mode. Passed as a value of the [EnHistorySyncMode (#enhistorysyncmode)](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySync/Enumerations.md#enhistorysyncmode) enumeration.  
From | Integer | The beginning date of the period for which historical data is synchronized. The date is specified in seconds elapsed since 01.01.1970.  
To | Integer | The ending date of the period for which historical data is synchronized. The date is specified in seconds elapsed since 01.01.1970.  
TimeCorrect | Integer | Time zone correction for the synchronization server relative to the time zone of the platform. Indicated in minutes. Positive and negative values can be used to specify the correction. 0 means the mode of automatic correction of the time zone.  
Flags | Integer | Data synchronization flags. Passed as a value of the [EnHistorySyncFlags (#enhistorysyncflags)](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySync/Enumerations.md#enhistorysyncflags) enumeration.  
Data | Integer | Data types for synchronization. Passed as a value of the [EnHistoryData (#enhistorydata)](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySync/Enumerations.md#enhistorydata) enumeration.  
Symbols | Array | [Array of symbols (#symbols)](Data-Structure.md#symbols), for which historical data is synchronized.  
  
<a id="symbols"></a>
## Symbols (#symbols)

Parameter | Type | Purpose  
Path | String | Path to the symbol.
