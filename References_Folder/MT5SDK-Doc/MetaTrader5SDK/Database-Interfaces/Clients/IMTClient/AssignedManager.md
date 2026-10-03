[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / AssignedManager

[Previous](KYCStatus.md) | [Next](DateCreated.md)

# IMTClient::AssignedManager

Get the manager responsible for the client.

C++
    
    
    UINT64  IMTClient::AssignedManager()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTClient.AssignedManager()

### Return Value

The manager login.

# IMTClient::AssignedManager

Set the manager responsible for the client.

C++
    
    
    MTAPIRES  IMTClient::AssignedManager(
       const UINT64  manager   // Client manager
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.AssignedManager(
       ulong         manager   // Client manager
       )

### Parameters

**manager**  
[in] Client manager login.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

[IMTConManager::Login](../../../Configuration-Interfaces/Managers/IMTConManager/Login.md) is used for the login.
