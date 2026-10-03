[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / DateCreated

[Previous](AssignedManager.md) | [Next](DateModified.md)

# IMTClient::DateCreated

Get the client creation date.

C++
    
    
    INT64  IMTClient::DateCreated()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTClient.DateCreated()

### Return Value

Client creation date in seconds since 01.01.1970.

# IMTClient::DateCreated

Set the client creation date.

C++
    
    
    MTAPIRES  IMTClient::DateCreated(
       const INT64  date      // creation date
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.DateCreated(
       long         date      // creation date
       )

### Parameters

**time**  
[in] Client creation date in seconds since 01.01.1970.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error occurred corresponding to the response code.

### 
