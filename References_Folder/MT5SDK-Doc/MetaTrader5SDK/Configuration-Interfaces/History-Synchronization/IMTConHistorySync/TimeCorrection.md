[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / TimeCorrection

[Previous](HistoryData.md) | [Next](From.md)

# IMTConHistorySync::TimeCorrection

Gets the correction of the time zone of the synchronization server relative to the time zone of the platform.

C++
    
    
    int  IMTConHistorySync::TimeCorrection()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConHistorySync.TimeCorrection()

Python (Manager API)
    
    
    MTConHistorySync.TimeCorrection

### Return Value

The correction of the time zone of the synchronization server relative to the time zone of the platform, in minutes.

### Note

Positive and negative values can be used to specify the correction. 0 means the mode of automatic correction of the time zone.

# IMTConHistorySync::TimeCorrection

Sets the correction of the time zone of the synchronization server relative to the time zone of the platform.

C++
    
    
    MTAPIRES  IMTConHistorySync::TimeCorrection(
       const int  correction      // Time zone correction
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.TimeCorrection(
       int        correction      // Time zone correction
       )

Python (Manager API)
    
    
    MTConHistorySync.TimeCorrection

### Parameters

**correction**  
[in] Time zone correction in minutes. Positive and negative values can be used to specify the correction. 0 means the mode of automatic correction of the time zone.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
