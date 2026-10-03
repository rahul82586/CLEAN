[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / KYCStatus

[Previous](ClientStatus.md) | [Next](AssignedManager.md)

# IMTClient::KYCStatus

Get the [KYC verification](../../../Configuration-Interfaces/KYC.md) status for a client.

C++
    
    
    UINT  IMTClient::KYCStatus()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.KYCStatus()

### Return Value

A value from the [IMTClient::EnKYCStatus (#enkycstatus)](Enumerations.md#enkycstatus) enumeration.

# IMTClient::KYCStatus

Set the [KYC verification](../../../Configuration-Interfaces/KYC.md) status for a client.

C++
    
    
    MTAPIRES  IMTClient::KYCStatus(
       const UINT  status    // Verification status
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.KYCStatus(
       uint        status    // Verification status
       )

### Parameters

**status**  
[in] KYC verification status. The status is passed using theIMTClient::EnKYCStatusenumeration value.

### Return Value

An indication of success is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred and the corresponding code is returned.
