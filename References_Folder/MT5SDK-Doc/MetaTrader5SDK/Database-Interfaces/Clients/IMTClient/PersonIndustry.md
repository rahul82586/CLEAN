[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonIndustry

[Previous](PersonEmployment.md) | [Next](PersonEducation.md)

# IMTClient::PersonIndustry

Get the client's employment industry.

C++
    
    
    UINT  IMTClient::PersonIndustry()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.PersonIndustry()

### Return Value

A value of the [IMTClient::EnEmploymentIndustry (#enemploymentindustry)](Enumerations.md#enemploymentindustry) enumeration.

# IMTClient::PersonIndustry

Set the client's employment industry.

C++
    
    
    MTAPIRES  IMTClient::PersonIndustry(
       const UINT  industry    // Employment industry
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonIndustry(
       uint        industry    // Employment industry
       )

### Parameters

**industry**  
[in] Client's employment industry. The value is passed using theIMTClient::EnEmploymentIndustryenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
