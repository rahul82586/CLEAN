[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / Flags

[Previous](SymbolNext.md) | [Next](../IMTConHistorySyncSink.md)

# IMTConHistorySync::Flags

Gets data synchronization flags.

C++
    
    
    UINT64  IMTConHistorySync::Flags()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConHistorySync.Flags()

Python (Manager API)
    
    
    MTConHistorySync.Flags

### Return Value

A value from the [IMTConHistorySync::EnHistorySyncFlags (#enhistorysyncflags)](Enumerations.md#enhistorysyncflags) enumeration.

# IMTConHistorySync::Flags

Sets data synchronization flags.

C++
    
    
    MTAPIRES  IMTConHistorySync::Flags(
       const UINT64  flags      // Flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.Flags(
       ulong         flags      // Flags
       )

Python (Manager API)
    
    
    MTConHistorySync.Flags

### Parameters

**mode**  
[in] Data synchronization flags are passed using theIMTConHistorySync::EnHistorySyncFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
