[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / ServerType

[Previous](Server.md) | [Next](Login.md)

# IMTConHistorySync::ServerType

Gets the type of the server with which history data are synchronized.

C++
    
    
    UINT  IMTConHistorySync::ServerType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHistorySync.ServerType()

Python (Manager API)
    
    
    MTConHistorySync.ServerType

### Return Value

A value from the [IMTConHistorySync::EnHistorySyncServer (#enhistorysyncserver)](Enumerations.md#enhistorysyncserver) enumeration.

# IMTConHistorySync::ServerType

Sets the type of the server with which history data are synchronized.

C++
    
    
    MTAPIRES  IMTConHistorySync::ServerType(
       const UINT  type      // Server type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.ServerType(
       uint        type      // Server type
       )

Python (Manager API)
    
    
    MTConHistorySync.ServerType

### Parameters

**type**  
[in] The type of the server with which history data are synchronized is passed using theIMTConHistorySync::EnHistorySyncServerenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
