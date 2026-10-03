[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / LeadCampaign

[Previous](LeadSource.md) | [Next](InterestRate.md)

# IMTUser::LeadCampaign

Get a lead campaign — name of a marketing campaign a client was attracted by.

C++
    
    
    LPCWSTR  IMTUser::LeadCampaign()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.LeadCampaign()

### Return Value

If successful, it returns a pointer to a string with a comment to the client. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/ios?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/android?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
---  
  
# IMTUser::LeadCampaign

Sets a lead campaign — name of a marketing campaign a client was attracted by.

C++
    
    
    MTAPIRES  IMTUser::LeadCampaign(
       LPCWSTR  lead_campaign    // Lead campaign
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.LeadCampaign(
       string   lead_campaign    // Lead campaign
       )

### Parameters

**lead_campaign**  
[in] A lead campaign — name of a marketing campaign a client was attracted by.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum comment length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/ios?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/android?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
---
