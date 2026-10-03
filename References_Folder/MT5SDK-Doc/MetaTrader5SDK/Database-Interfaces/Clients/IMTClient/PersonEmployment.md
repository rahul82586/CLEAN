[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonEmployment

[Previous](PersonDocumentExtra.md) | [Next](PersonIndustry.md)

# IMTClient::PersonEmployment

Get the client's employment status.

C++
    
    
    UINT  IMTClient::PersonEmployment()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.PersonEmployment()

### Return Value

A value from the [IMTClient::EnEmployment (#enemployment)](Enumerations.md#enemployment) enumeration.

# IMTClient::PersonEmployment

Set the client's employment status.

C++
    
    
    MTAPIRES  IMTClient::PersonEmployment(
       const UINT  employment  // Employment
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonEmployment(
       uint        employment  // Employment
       )

### Parameters

**employment**  
[in] Client's employment status. The status is passed using theIMTClient::EnEmploymentenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
