[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTime](../IMTCon.md) / IMTCon Server

[Previous](IMTCon-Zone.md) | [Next](IMTCon-TableGet.md)

# IMTConTime::TimeServer

Get the address of the current time synchronization server.

C++
    
    
    LPCWSTR  IMTConTime::TimeServer()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConTime.TimeServer()

Python (Manager API)
    
    
    MTConTime.TimeServer

### Return Value

If successful, it returns a pointer to a string with the address of the synchronization server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConTime](../IMTCon.md) object.

# IMTConTime::TimeServer

Set the address of the current time synchronization server.

C++
    
    
    MTAPIRES  IMTConTime::TimeServer(
       LPCWSTR  server      // Server address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConTime.TimeServer(
       string   server      // Server address
       )

Python (Manager API)
    
    
    MTConTime.TimeServer

### Parameters

**server**  
[in] The address of the time synchronization server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Supports time synchronization through the TIME and NTP protocols.
