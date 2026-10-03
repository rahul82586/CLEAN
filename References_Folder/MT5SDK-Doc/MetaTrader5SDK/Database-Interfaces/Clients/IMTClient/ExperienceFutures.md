[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ExperienceFutures

[Previous](ExperienceCFD.md) | [Next](ExperienceStocks.md)

# IMTClient::ExperienceFutures

Get information about the client's Futures trading experience.

C++
    
    
    UINT  IMTClient::ExperienceFutures()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.ExperienceFutures()

### Return Value

A value from the [IMTClient::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience) enumeration.

# IMTClient::ExperienceFutures

Set information about the client's Futures trading experience.

C++
    
    
    MTAPIRES  IMTClient::ExperienceFutures(
       const UINT  experience  // Trading experience
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ExperienceFutures(
       uint        experience  // Trading experience
       )

### Parameters

**experience**  
[in] Client's Futures trading experience. The trading experience is passed using theIMTClient::EnTradingExperienceenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
