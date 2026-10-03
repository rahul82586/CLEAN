[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonEducation

[Previous](PersonIndustry.md) | [Next](PersonWealthSource.md)

# IMTClient::PersonEducation

Get the client's education level.

C++
    
    
    UINT  IMTClient::PersonEducation()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.PersonEducation()

### Return Value

A value from the [IMTClient::EnEducationLevel (#eneducationlevel)](Enumerations.md#eneducationlevel) enumeration.

# IMTClient::PersonEducation

Set the client's education level.

C++
    
    
    MTAPIRES  IMTClient::PersonEducation(
       const UINT  education   // Client's education
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonEducation(
       uint        education   // Client's education
       )

### Parameters

**education**  
[in] Client's education level. The value is passed using theIMTClient::EnEducationLevelenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
