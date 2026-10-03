[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ComplianceDateApproval

[Previous](ComplianceClientCategory.md) | [Next](ComplianceDateTermination.md)

# IMTClient::ComplianceDateApproval

Get the client approval date.

C++
    
    
    INT64  IMTClient::ComplianceDateApproval()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTClient.ComplianceDateApproval()

### Return Value

Client approval date in seconds since 01.01.1970.

# IMTClient::ComplianceDateApproval

Set the client approval date.

C++
    
    
    MTAPIRES  IMTClient::ComplianceDateApproval(
       const INT64  date      // Date of approval
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ComplianceDateApproval(
       long         date      // Date of approval
       )

### Parameters

**time**  
[in] Client approval date in seconds since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
