[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyRegAuthority

[Previous](CompanyRegDate.md) | [Next](CompanyVat.md)

# IMTClient::CompanyRegAuthority

Get the name of the registration authority with which the company was registered (for corporate body).

C++
    
    
    LPCWSTR  IMTClient::CompanyRegAuthority()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyRegAuthority()

### Return Value

If successful, it returns a pointer to a string with the name of the registration authority. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

To be able to use the string after the object removal (call of the [IMTClient::Release](Release.md) method of this object), a copy of it should be created.

# IMTClient::CompanyRegAuthority

Set the name of the registration authority with which the company was registered (for corporate body).

C++
    
    
    MTAPIRES  IMTClient::CompanyRegAuthority(
       LPCWSTR       authority    // Registration authority
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyRegAuthority(
       string        authority    // Registration authority
       )

### Parameters

**authority**  
[in] Registration authority.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The name length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
