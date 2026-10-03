[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyAddress

[Previous](CompanyCountry.md) | [Next](CompanyWebsite.md)

# IMTClient::CompanyAddress

Get the company's legal address (for corporate clients).

C++
    
    
    LPCWSTR  IMTClient::CompanyAddress()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyAddress()

### Return Value

If successful, the method returns a pointer to a string with the address. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::CompanyAddress

Set the company's legal address (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyAddress(
       LPCWSTR       address      // Legal address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyAddress(
       string        address      // Legal address
       )

### Parameters

**address**  
[in] Company's legal address.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The address length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
