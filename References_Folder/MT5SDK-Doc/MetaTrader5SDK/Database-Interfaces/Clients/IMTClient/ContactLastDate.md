[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ContactLastDate

[Previous](ContactSocialNetworks.md) | [Next](AddressCountry.md)

# IMTClient::ContactLastDate

Get the date of the last client contact.

C++
    
    
    INT64  IMTClient::ContactLastDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTClient.ContactLastDate()

### Return Value

Date of the last contact in seconds elapsed since 01.01.1970.

# IMTClient::ContactLastDate

Set the date of the last client contact.

C++
    
    
    MTAPIRES  IMTClient::ContactLastDate(
       const INT64  date      // Date of contact
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ContactLastDate(
       long         date      // Date of contact
       )

### Parameters

**date**  
[in] Date of the last contact in seconds elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
