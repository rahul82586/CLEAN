[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ComplianceApprovedBy

[Previous](DateModified.md) | [Next](ComplianceClientCategory.md)

# IMTClient::ComplianceApprovedBy

Get the manager who checked the client data and approved registration.

C++
    
    
    UINT64  IMTClient::ComplianceApprovedBy()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTClient.ComplianceApprovedBy()

### Return Value

The login of the manager who approved the client.

# IMTClient::ComplianceApprovedBy

Set the manager who checked the client data and approved registration.

C++
    
    
    MTAPIRES  IMTClient::ComplianceApprovedBy(
       const UINT64  manager   // Manager
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ComplianceApprovedBy(
       ulong         manager   // Manager
       )

### Parameters

**manager**  
[in] The login of the manager who approved the client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

[IMTConManager::Login](../../../Configuration-Interfaces/Managers/IMTConManager/Login.md) is used for the login.
