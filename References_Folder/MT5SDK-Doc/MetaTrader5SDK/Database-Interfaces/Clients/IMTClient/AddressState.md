[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / AddressState

[Previous](AddressStreet.md) | [Next](AddressCity.md)

# IMTClient::AddressState

Get the client's region of residence.

C++
    
    
    LPCWSTR  IMTClient::AddressState()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.AddressState()

### Return Value

If successful, the method returns a pointer to a string with the region. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::AddressState

Set the client's region of residence.

C++
    
    
    MTAPIRES  IMTClient::AddressState(
       LPCWSTR       state         // Region
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.AddressState(
       string        state         // Region
       )

### Parameters

**street**  
[in] Client's region of residence.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The region length is limited to 64 characters (with the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
