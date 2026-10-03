[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonName

[Previous](PersonTitle.md) | [Next](PersonMiddleName.md)

# IMTClient::PersonName

Get the name of a client.

C++
    
    
    LPCWSTR  IMTClient::PersonName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonName()

### Return Value

If successful, a pointer to a string with the name is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonName

Set the name of a client.

C++
    
    
    MTAPIRES  IMTClient::PersonName(
       LPCWSTR       name         // Client name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonName(
       string        name         // Client name
       )

### Parameters

**name**  
[in] The name of a client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The name length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
