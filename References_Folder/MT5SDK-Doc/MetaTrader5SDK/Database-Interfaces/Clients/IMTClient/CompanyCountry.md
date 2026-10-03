[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyCountry

[Previous](CompanyLicenseAuthority.md) | [Next](CompanyAddress.md)

# IMTClient::CompanyCountry

Get the company's country of incorporation (for corporate clients).

C++
    
    
    LPCWSTR  IMTClient::CompanyCountry()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyCountry()

### Return Value

If successful, a pointer to a string with the country of incorporation is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::CompanyCountry

Set the company's country of incorporation (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyCountry(
       LPCWSTR       country      // Registration country
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyCountry(
       string        country      // Registration country
       )

### Parameters

**country**  
[in] Company's country of incorporation.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The country name length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
