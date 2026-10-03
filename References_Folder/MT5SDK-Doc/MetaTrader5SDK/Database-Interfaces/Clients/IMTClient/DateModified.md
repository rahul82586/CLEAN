[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / DateModified

[Previous](DateCreated.md) | [Next](ComplianceApprovedBy.md)

# IMTClient::DateModified

Get the client's last modification date.

C++
    
    
    INT64  IMTClient::DateModified()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTClient.DateModified()

### Return Value

The date the client was last modified in seconds since 01.01.1970.

# IMTClient::DateModified

Set the client approval date.

C++
    
    
    MTAPIRES  IMTClient::DateModified(
       const INT64  date      // last modification date
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.DateModified(
       long         date      // last modification date
       )

### Parameters

**time**  
[in] The date the client was last modified in seconds since 01.01.1970.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error occurred corresponding to the response code.

### 
