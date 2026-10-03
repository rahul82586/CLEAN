[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTime](../IMTCon.md) / IMTCon Zone

[Previous](IMTCon-Clear.md) | [Next](IMTCon-Server.md)

# IMTConTime::TimeZone

Get the time zone of a server.

C++
    
    
    int  IMTConTime::TimeZone()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConTime.TimeZone()

Python (Manager API)
    
    
    MTConTime.TimeZone

### Return Value

The time zone of a server in minutes from GMT.

### Note

Examples: 0 = GMT; -60 = GMT - 1; 60 = GMT + 1.

# IMTConTime::TimeZone

Set the time zone of a server.

C++
    
    
    MTAPIRES  IMTConTime::TimeZone(
       const int  zone      // Time zone
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConTime.TimeZone(
       int        zone      // Time zone
       )

Python (Manager API)
    
    
    MTConTime.TimeZone

### Parameters

**zone**  
[in] The time zone of a server in minutes from GMT. For example,0 = GMT; -60 = GMT - 1; 60 = GMT + 1.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
