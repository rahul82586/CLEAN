[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ClientOrigin

[Previous](TradingGroup.md) | [Next](ClientOriginLogin.md)

# IMTClient::ClientOrigin

Get the client record creation method.

C++
    
    
    UINT  IMTClient::ExperienceCFD()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.ExperienceCFD()

### Return Value

A value of the [IMTClient::EnClientOrigin (#enclientorigin)](Enumerations.md#enclientorigin) enumeration.

# IMTClient::ExperienceCFD

Set the client record creation method.

C++
    
    
    MTAPIRES  IMTClient::ExperienceCFD(
       const UINT  origin      // Client record creation method
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ExperienceCFD(
       uint        origin      // Client record creation method
       )

### Parameters

**origin**  
[in] Client record creation method. The method is passed using theIMTClient::EnClientOriginenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
