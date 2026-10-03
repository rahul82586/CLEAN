[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ExperienceCFD

[Previous](ExperienceFX.md) | [Next](ExperienceFutures.md)

# IMTClient::ExperienceCFD

Get information about the client's CFD trading experience.

C++
    
    
    UINT  IMTClient::ExperienceCFD()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.ExperienceCFD()

### Return Value

A value from the [IMTClient::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience) enumeration.

# IMTClient::ExperienceCFD

Set information about the client's CFD trading experience.

C++
    
    
    MTAPIRES  IMTClient::ExperienceCFD(
       const UINT  experience  // Trading experience
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ExperienceCFD(
       uint        experience  // Trading experience
       )

### Parameters

**experience**  
[in] Client's CFD trading experience. The trading experience is passed using theIMTClient::EnTradingExperienceenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
