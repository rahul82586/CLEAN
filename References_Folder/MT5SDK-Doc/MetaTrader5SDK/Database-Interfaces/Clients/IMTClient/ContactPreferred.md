[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ContactPreferred

[Previous](CompanyWebsite.md) | [Next](ContactLanguage.md)

# IMTClient::ContactPreferred

Get the client's preferred contact methods.

C++
    
    
    UINT  IMTClient::ContactPreferred()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.ContactPreferred()

### Return Value

A value from the [IMTClient::EnPreferredCommunication (#enpreferredcommunication)](Enumerations.md#enpreferredcommunication) enumeration.

# IMTClient::ContactPreferred

Set the client's preferred contact methods.

C++
    
    
    MTAPIRES  IMTClient::ContactPreferred(
       const UINT  preferred   // Contact method
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ContactPreferred(
       uint        preferred   // Contact method
       )

### Parameters

**preferred**  
[in] Preferred contact method. The method is passed using theIMTClient::EnPreferredCommunicationenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
