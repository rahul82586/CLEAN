[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ContactMessengers

[Previous](ContactPhone.md) | [Next](ContactSocialNetworks.md)

# IMTClient::ContactMessengers

Get the list of the client's accounts in instant messengers.

C++
    
    
    LPCWSTR  IMTClient::ContactMessengers()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.ContactMessengers()

### Return Value

If successful, a pointer to a string with the list of accounts is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::ContactMessengers

Set the list of the client's accounts in instant messengers.

C++
    
    
    MTAPIRES  IMTClient::ContactMessengers(
       LPCWSTR       messengers   // Instant messengers
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ContactMessengers(
       string        messengers   // Instant messengers
       )

### Parameters

**messengers**  
[in] The list of the client's accounts in instant messengers.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The length of the accounts list is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
