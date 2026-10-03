[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonLastName

[Previous](PersonMiddleName.md) | [Next](PersonBirthDate.md)

# IMTClient::PersonLastName

Get the client's last name.

C++
    
    
    LPCWSTR  IMTClient::PersonLastName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonLastName()

### Return Value

If successful, the method returns a pointer to a string with the last name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonLastName

Set the client's last name.

C++
    
    
    MTAPIRES  IMTClient::PersonLastName(
       LPCWSTR       last_name     // Client's last name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonLastName(
       string        last_name     // Client's last name
       )

### Parameters

**last_name**  
[in] Client's last name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The last name length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
