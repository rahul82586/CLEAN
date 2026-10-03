[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonMiddleName

[Previous](PersonName.md) | [Next](PersonLastName.md)

# IMTClient::PersonMiddleName

Get the client's middle name.

C++
    
    
    LPCWSTR  IMTClient::PersonMiddleName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonMiddleName()

### Return Value

If successful, the method returns a pointer to a string with the middle name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonMiddleName

Set the client's middle name.

C++
    
    
    MTAPIRES  IMTClient::PersonMiddleName(
       LPCWSTR       middle_name   // Client's middle name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonMiddleName(
       string        middle_name   // Client's middle name
       )

### Parameters

**middle_name**  
[in] Client's middle name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The middle name length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
