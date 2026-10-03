[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ExperienceFX

[Previous](AddressCity.md) | [Next](ExperienceCFD.md)

# IMTClient::ExperienceFX

Get information about the client's Forex trading experience.

C++
    
    
    UINT  IMTClient::ExperienceFX()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.ExperienceFX()

### Return Value

A value from the [IMTClient::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience) enumeration.

# IMTClient::ContactPreferred

Set information about the client's Forex trading experience.

C++
    
    
    MTAPIRES  IMTClient::ExperienceFX(
       const UINT  experience  // Trading experience
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ExperienceFX(
       uint        experience  // Trading experience
       )

### Parameters

**experience**  
[in] Client's Forex trading experience. The trading experience is passed using theIMTClient::EnTradingExperienceenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
