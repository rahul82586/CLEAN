[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyLicenseAuthority

[Previous](CompanyLicenseNumber.md) | [Next](CompanyCountry.md)

# IMTClient::CompanyLicenseAuthority

Get the name of the licensing authority (for corporate clients).

C++
    
    
    LPCWSTR  IMTClient::CompanyLicenseAuthority()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyLicenseAuthority()

### Return Value

If successful, it returns a pointer to a string with the name of the licensing authority. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::CompanyLicenseAuthority

Set the name of the licensing authority (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyLicenseAuthority(
       LPCWSTR       authority    // Licensing authority
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyLicenseAuthority(
       string        authority    // Licensing authority
       )

### Parameters

**authority**  
[in] Licensing authority.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The name length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
