[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / Server

[Previous](Clear.md) | [Next](ServerType.md)

# IMTConHistorySync::Server

Get the IP address or the domain name of the server, with which history data are synchronized.

C++
    
    
    LPCWSTR  IMTConHistorySync::Server()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConHistorySync.Server()

Python (Manager API)
    
    
    MTConHistorySync.Server

### Return Value

If successful, it returns a pointer to the string with the IP address or the domain name of the synchronization server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConHistorySync](../IMTConHistorySync.md) object.

To use the string after the object removal (call of the [IMTConHistorySync::Release](Release.md) method of this object), a copy of it should be created.

# IMTConHistorySync::Server

Set the IP address or the domain name of the server, with which history data are synchronized.

C++
    
    
    MTAPIRES  IMTConHistorySync::Server(
       LPCWSTR  server      // Synchronization server
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.Server(
       string   server      // Synchronization server
       )

Python (Manager API)
    
    
    MTConHistorySync.Server

### Parameters

**server**  
[in] The IP address or the domain name of the history data synchronization server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note
