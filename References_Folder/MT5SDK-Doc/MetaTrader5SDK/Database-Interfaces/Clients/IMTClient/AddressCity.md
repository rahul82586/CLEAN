[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / AddressCity

[Previous](AddressState.md) | [Next](ExperienceFX.md)

# IMTClient::AddressCity

Get the client's city of residence.

C++
    
    
    LPCWSTR  IMTClient::AddressCity()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.AddressCity()

### Return Value

If successful, it returns a pointer to a string with the client's city. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::AddressCity

Set the client's city of residence.

C++
    
    
    MTAPIRES  IMTClient::AddressCity(
       LPCWSTR       city          // City
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.AddressCity(
       string        city          // City
       )

### Parameters

**city**  
[in] The client's city of residence.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The city name length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
