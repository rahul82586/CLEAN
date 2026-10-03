[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / Mode

[Previous](Password.md) | [Next](ModeSync.md)

# IMTConHistorySync::Mode

Get the state of the configuration of data synchronization.

C++
    
    
    UINT  IMTConHistorySync::Mode()  const

.NET (Gateway/Manager API)
    
    
    EnHistoryMode  CIMTConHistorySync.Mode()

Python (Manager API)
    
    
    MTConHistorySync.Mode

### Return Value

A value from the [IMTConHistorySync::EnHistoryMode (#enhistorymode)](Enumerations.md#enhistorymode) enumeration.

# IMTConHistorySync::Mode

Set the state of the configuration of data synchronization.

C++
    
    
    MTAPIRES  IMTConHistorySync::Mode(
       const UINT     mode   // State of configuration
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.Mode(
       EnHistoryMode  mode   // State of configuration
       )

Python (Manager API)
    
    
    MTConHistorySync.Mode

### Parameters

**mode**  
[in] The state of data synchronization configuration is passed using theIMTConHistorySync::EnHistoryModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
