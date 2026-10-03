[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / ServiceTime

[Previous](PasswordCheck.md) | [Next](AdaptersCurrent.md)

# IMTConServer::ServiceTime

Get the service time (time of optimization), when various operations aimed at increasing the performance and reliability of the platform are conducted.

C++
    
    
    UINT  IMTConServer::ServiceTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.ServiceTime()

Python (Manager API)
    
    
    MTConServer.ServiceTime

### Return Value

Service time in minutes elapsed since 00:00.

# IMTConServer::ServiceTime

Set the service time (time of optimization), when various operations aimed at increasing the performance and reliability of the platform are conducted.

C++
    
    
    MTAPIRES  IMTConServer::ServiceTime(
       const UINT  stime      // Service time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.ServiceTime(
       uint        stime      // Service time
       )

Python (Manager API)
    
    
    MTConServer.ServiceTime

### Parameters

**stime**  
[in] Service time in minutes elapsed since 00:00.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
