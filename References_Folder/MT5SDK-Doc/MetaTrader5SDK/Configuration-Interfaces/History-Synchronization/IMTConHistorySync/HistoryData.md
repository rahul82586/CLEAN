[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / HistoryData

[Previous](ModeSync.md) | [Next](TimeCorrection.md)

# IMTConHistorySync::HistoryData

Getting the type of data used in synchronization.

C++
    
    
    UINT  IMTConHistorySync::HistoryData()  const

.NET (Gateway/Manager API)
    
    
    EnHistoryData  CIMTConHistorySync.HistoryData()

Python (Manager API)
    
    
    MTConHistorySync.HistoryData

### Return Value

A value from the [IMTConHistorySync::EnHistoryData (#enhistorydata)](Enumerations.md#enhistorydata) enumeration.

# IMTConHistorySync::HistoryData

Set the type of data to synchronize.

C++
    
    
    MTAPIRES  IMTConHistorySync::HistoryData(
       const UINT     data   // Data type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.HistoryData(
       EnHistoryData  data   // Data type
       )

Python (Manager API)
    
    
    MTConHistorySync.HistoryData

### Parameters

**data**  
[in] The data type is passed using theIMTConHistorySync::EnHistoryDataenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
