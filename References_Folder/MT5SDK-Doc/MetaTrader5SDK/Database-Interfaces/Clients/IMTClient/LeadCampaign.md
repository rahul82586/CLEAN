[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / LeadCampaign

[Previous](ComplianceDateTermination.md) | [Next](LeadSource.md)

# IMTClient::LeadCampaign

Get a lead campaign — the name of a marketing campaign a client was attracted by.

C++
    
    
    LPCWSTR  IMTClient::LeadCampaign()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.LeadCampaign()

### Return Value

If successful, the method returns a pointer to a string with the campaign. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::LeadCampaign

Set a lead campaign — the name of a marketing campaign a client was attracted by.

C++
    
    
    MTAPIRES  IMTClient::LeadCampaign(
       LPCWSTR       campaign  // Campaign
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.LeadCampaign(
       string        campaign  // Campaign
       )

### Parameters

**campaign**  
[in] Campaign name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The campaign name length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
