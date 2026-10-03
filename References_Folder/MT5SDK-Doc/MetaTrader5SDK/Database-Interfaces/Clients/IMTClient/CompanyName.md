[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyName

[Previous](PersonAnnualDeposit.md) | [Next](CompanyRegNumber.md)

# IMTClient::CompanyName

Get the company name (for corporate clients).

C++
    
    
    LPCWSTR  IMTClient::CompanyName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyName()

### Return Value

If successful, a pointer to a string with the company name is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::CompanyName

Set the company name (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyName(
       LPCWSTR       name         // Company name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyName(
       string        name         // Company name
       )

### Parameters

**name**  
[in] Company name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The name length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
