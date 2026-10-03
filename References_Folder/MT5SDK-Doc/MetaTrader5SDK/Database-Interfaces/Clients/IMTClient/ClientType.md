[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ClientType

[Previous](RecordID.md) | [Next](ClientStatus.md)

# IMTClient::ClientType

Get the client type.

C++
    
    
    UINT  IMTClient::ClientType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.ClientType()

### Return Value

A value of the [IMTClient::EnClientType (#enclienttype)](Enumerations.md#enclienttype) enumeration.

# IMTClient::ClientType

Set the client type.

C++
    
    
    MTAPIRES  IMTClient::ClientType(
       const UINT  type       // Client type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ClientType(
       uint        type      // Client type
       )

### Parameters

**type**  
[in] Client type. The client type is passed using theIMTClient::EnClientTypeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
