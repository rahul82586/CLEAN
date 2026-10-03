[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / AddressStreet

[Previous](AddressPostcode.md) | [Next](AddressState.md)

# IMTClient::AddressStreet

Get the address of a client.

C++
    
    
    LPCWSTR  IMTClient::AddressPostcode()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.AddressPostcode()

### Return Value

If successful, the method returns a pointer to a string with the address. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::AddressPostcode

Set the address of a client.

C++
    
    
    MTAPIRES  IMTClient::AddressPostcode(
       LPCWSTR       street        // Address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.AddressPostcode(
       string        street        // Address
       )

### Parameters

**street**  
[in] The client's address, including the street name, building number, etc.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum address length is 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
