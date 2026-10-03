[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ExperienceStocks

[Previous](ExperienceFutures.md) | [Next](TradingGroup.md)

# IMTClient::ExperienceStocks

Get information about the client's Stock trading experience.

C++
    
    
    UINT  IMTClient::ExperienceStocks()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.ExperienceStocks()

### Return Value

A value from the [IMTClient::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience) enumeration.

# IMTClient::ExperienceStocks

Set information about the client's Stock trading experience.

C++
    
    
    MTAPIRES  IMTClient::ExperienceStocks(
       const UINT  experience  // Trading experience
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ExperienceStocks(
       uint        experience  // Trading experience
       )

### Parameters

**experience**  
[in] Client's Stocks trading experience. The trading experience is passed using theIMTClient::EnTradingExperienceenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
