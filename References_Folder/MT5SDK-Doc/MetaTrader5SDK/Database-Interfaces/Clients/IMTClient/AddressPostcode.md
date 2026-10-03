[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / AddressPostcode

[Previous](AddressCountry.md) | [Next](AddressStreet.md)

# IMTClient::AddressPostcode

Get the client's zip code.

C++
    
    
    LPCWSTR  IMTClient::AddressPostcode()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.AddressPostcode()

### Return Value

If successful, a pointer to a string with a zip code is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::AddressPostcode

Set a client's zip code.

C++
    
    
    MTAPIRES  IMTClient::AddressPostcode(
       LPCWSTR       postcode     // Zip code
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.AddressPostcode(
       string        postcode     // Zip code
       )

### Parameters

**postcode**  
[in] Client's zip code.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The zip code length is limited to 16 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
