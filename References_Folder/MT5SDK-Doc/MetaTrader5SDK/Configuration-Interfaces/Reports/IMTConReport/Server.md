[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / Server

[Previous](Name.md) | [Next](Module.md)

# IMTConReport::Server

Get the ID of the server on which the report is installed.

C++
    
    
    UINT64  IMTConReport::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConReport.Server()

Python (Manager API)
    
    
    MTConReport.Server

### Return Value

The ID of the server on which the report is installed.

# IMTConReport::Server

Set the ID of the server.

C++
    
    
    MTAPIRES  IMTConReport::Server(
       const UINT64  server      // Server ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.Server(
       ulong         server      // Server ID
       )

Python (Manager API)
    
    
    MTConReport.Server

### Parameters

**server**  
[in] Server ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
