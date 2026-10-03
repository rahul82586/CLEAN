[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / LeadSource

[Previous](Leverage.md) | [Next](LeadCampaign.md)

# IMTUser::LeadSource

Get a lead source — a website a client has come from.

C++
    
    
    LPCWSTR  IMTUser::LeadSource()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.LeadSource()

### Return Value

If successful, it returns a pointer to a string with a comment to the client. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/ios?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/android?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
---  
  
# IMTUser::LeadSource

Sets a lead source — a website a client has come from.

C++
    
    
    MTAPIRES  IMTUser::LeadSource(
       LPCWSTR  lead_source      // Lead source
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.LeadSource(
       string   lead_source      // Lead source
       )

### Parameters

**lead_source**  
[in]A lead source— a websitea client has come from.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum comment length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/ios?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/android?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
---
