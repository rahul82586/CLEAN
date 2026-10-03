[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyWebsite

[Previous](CompanyAddress.md) | [Next](ContactPreferred.md)

# IMTClient::CompanyWebsite

Get the website address (for corporate clients).

C++
    
    
    LPCWSTR  IMTClient::CompanyWebsite()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyWebsite()

### Return Value

If successful, the method returns a pointer to a string with the address. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::CompanyWebsite

Set the website address (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyWebsite(
       LPCWSTR       website      // Website address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyWebsite(
       string        website      // Website address
       )

### Parameters

**website**  
[in] Website address.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The address length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
