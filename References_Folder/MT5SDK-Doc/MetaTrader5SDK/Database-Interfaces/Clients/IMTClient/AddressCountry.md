[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / AddressCountry

[Previous](ContactLastDate.md) | [Next](AddressPostcode.md)

# IMTClient::AddressCountry

Get the client's country of residence.

C++
    
    
    LPCWSTR  IMTClient::AddressCountry()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.AddressCountry()

### Return Value

If successful, a pointer to the string with the country is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::AddressCountry

Set the client's country of residence.

C++
    
    
    MTAPIRES  IMTClient::AddressCountry(
       LPCWSTR       country      // Client's country
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.AddressCountry(
       string        country      // Client's country
       )

### Parameters

**country**  
[in] The client's country of residence.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The country name length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
