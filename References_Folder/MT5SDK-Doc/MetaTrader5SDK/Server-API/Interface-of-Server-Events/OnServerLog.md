[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Server Events](../Interface-of-Server-Events.md) / OnServerLog

[Previous](../Interface-of-Server-Events.md) | [Next](../Interface-of-Custom-Events.md)

# IMTServerSink::OnServerLog

A handler of the event of adding a record to the server journal.
    
    
    virtual void  IMTServerSink::OnServerLog(
       const int    code,      // Message type
       const UINT   type,      // Event type
       const INT64  datetime,  // Message time
       LPCWSTR      source,    // Message source
       LPCWSTR      message    // Message text
       )

### Parameters

**code**  
[in] Logmessage type.

**type**  
[in]Event type.

**datetime**  
[in] Message time in milliseconds passed since 01.01.1970.

**source**  
[in] Message source.

**message**  
[in] Message text. The string contains only the massage text without time and type.

### Note

This method is called by the Server API to notify that a new record has been added to the server journal.
