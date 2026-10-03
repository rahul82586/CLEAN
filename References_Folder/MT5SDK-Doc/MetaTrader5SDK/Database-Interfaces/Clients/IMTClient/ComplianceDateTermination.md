[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ComplianceDateTermination

[Previous](ComplianceDateApproval.md) | [Next](LeadCampaign.md)

# IMTClient::ComplianceDateTermination

Get the date of service termination for the client.

C++
    
    
    INT64  IMTClient::ComplianceDateTermination()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTClient.ComplianceDateTermination()

### Return Value

Date on which provision of services to the client was terminated, in seconds since 01.01.1970.

# IMTClient::ComplianceDateTermination

Set the date of service termination for the client.

C++
    
    
    MTAPIRES  IMTClient::ComplianceDateTermination(
       const INT64  date      // Date of termination
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ComplianceDateTermination(
       long         date      // Date of termination
       )

### Parameters

**time**  
[in] Date on which provision of services to the client was terminated, in seconds since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
