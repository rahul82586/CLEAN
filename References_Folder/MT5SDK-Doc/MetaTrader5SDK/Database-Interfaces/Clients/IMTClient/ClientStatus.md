[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ClientStatus

[Previous](ClientType.md) | [Next](KYCStatus.md)

# IMTClient::ClientStatus

Get a client's status.

C++
    
    
    UINT  IMTClient::ClientStatus()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.ClientStatus()

### Return Value

A value of the [IMTClient::EnClientStatus (#enclientstatus)](Enumerations.md#enclientstatus) enumeration.

# IMTClient::ClientType

Set the client type.

C++
    
    
    MTAPIRES  IMTClient::ClientStatus(
       const UINT  status    // Client status
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ClientStatus(
       uint        status    // Client status
       )

### Parameters

**status**  
[in] Client status. The status is passed using theIMTClient::EnClientStatusenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
