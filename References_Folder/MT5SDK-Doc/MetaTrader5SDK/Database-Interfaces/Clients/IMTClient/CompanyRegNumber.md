[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyRegNumber

[Previous](CompanyName.md) | [Next](CompanyRegDate.md)

# IMTClient::CompanyRegNumber

Get the company registration number (for corporate clients).

C++
    
    
    LPCWSTR  IMTClient::CompanyRegNumber()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyRegNumber()

### Return Value

If successful, a pointer to a string with the registration number is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::CompanyRegNumber

Set the company registration number (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyRegNumber(
       LPCWSTR       number       // Registration number
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyRegNumber(
       string        number       // Registration number
       )

### Parameters

**number**  
[in] Registration number.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The number length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
