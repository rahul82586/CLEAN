[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyRegDate

[Previous](CompanyRegNumber.md) | [Next](CompanyRegAuthority.md)

# IMTClient::CompanyRegDate

Get the company registration date (for corporate clients).

C++
    
    
    INT64  IMTClient::CompanyRegDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTClient.CompanyRegDate()

### Return Value

Company registration date in seconds that elapsed since 01.01.1970.

# IMTClient::CompanyRegDate

Set the company registration date (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyRegDate(
       const INT64  date      // Registration date
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyRegDate(
       long         date      // Registration date
       )

### Parameters

**date**  
[in] Company registration date in seconds that elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
