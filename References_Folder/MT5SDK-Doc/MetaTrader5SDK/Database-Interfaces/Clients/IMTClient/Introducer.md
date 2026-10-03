[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / Introducer

[Previous](LeadSource.md) | [Next](PersonTitle.md)

# IMTClient::Introducer

Get the login (trading account) of the user who introduced this client.

C++
    
    
    LPCWSTR  IMTClient::Introducer()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.Introducer()

### Return Value

If successful, the method returns a pointer to a string with the login. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::Introducer

Set the login (trading account) of the user who introduced this client.

C++
    
    
    MTAPIRES  IMTClient::Introducer(
       LPCWSTR       introducer  // Source
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.Introducer(
       string        introducer  // Source
       )

### Parameters

**introducer**  
[in] The login (trading account) of the user who attracted this client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The login length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
