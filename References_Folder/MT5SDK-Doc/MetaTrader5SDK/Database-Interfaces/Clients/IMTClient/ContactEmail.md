[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ContactEmail

[Previous](ContactLanguage.md) | [Next](ContactPhone.md)

# IMTClient::ContactEmail

Get the client's email address.

C++
    
    
    LPCWSTR  IMTClient::ContactEmail()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.ContactEmail()

### Return Value

If successful, the method returns a pointer to a string with the address. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::ContactEmail

Set the client's email address.

C++
    
    
    MTAPIRES  IMTClient::ContactEmail(
       LPCWSTR       email        // Email address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ContactEmail(
       string        email        // Email address
       )

### Parameters

**email**  
[in] The email address of a client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The address length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
