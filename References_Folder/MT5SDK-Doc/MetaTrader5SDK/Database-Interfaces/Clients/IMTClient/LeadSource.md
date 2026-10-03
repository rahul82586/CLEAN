[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / LeadSource

[Previous](LeadCampaign.md) | [Next](Introducer.md)

# IMTClient::LeadSource

Get a lead source — a website the client has come from.

C++
    
    
    LPCWSTR  IMTClient::LeadSource()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.LeadSource()

### Return Value

If successful, the method returns a pointer to a string with the source. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::LeadSource

Set a lead source — a website the client has come from.

C++
    
    
    MTAPIRES  IMTClient::LeadSource(
       LPCWSTR       source    // Source
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.LeadSource(
       string        source    // Source
       )

### Parameters

**source**  
[in] Lead source.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The source name length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
