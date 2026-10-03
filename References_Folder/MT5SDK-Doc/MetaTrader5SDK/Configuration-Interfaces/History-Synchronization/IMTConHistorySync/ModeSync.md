[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / ModeSync

[Previous](Mode.md) | [Next](HistoryData.md)

# IMTConHistorySync::ModeSync

Get the mode of history data synchronization.

C++
    
    
    UINT  IMTConHistorySync::ModeSync()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHistorySync.ModeSync()

Python (Manager API)
    
    
    MTConHistorySync.ModeSync

### Return Value

A value from the [IMTConHistorySync::EnHistorySyncMode (#enhistorysyncmode)](Enumerations.md#enhistorysyncmode) enumeration.

# IMTConHistorySync::ModeSync

Set the mode of history data synchronization.

C++
    
    
    MTAPIRES  IMTConHistorySync::ModeSync(
       const UINT  type      // Synchronization mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.ModeSync(
       uint        type      // Synchronization mode
       )

Python (Manager API)
    
    
    MTConHistorySync.ModeSync

### Parameters

**type**  
[in] History data synchronization mode is passed using theIMTConHistorySync::EnHistorySyncModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
