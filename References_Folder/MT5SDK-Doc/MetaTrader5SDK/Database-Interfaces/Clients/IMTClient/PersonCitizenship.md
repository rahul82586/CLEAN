[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonCitizenship

[Previous](PersonBirthDate.md) | [Next](PersonGender.md)

# IMTClient::PersonCitizenship

Get the client's citizenship.

C++
    
    
    LPCWSTR  IMTClient::PersonCitizenship()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonCitizenship()

### Return Value

If successful, the method returns a pointer to a string with the client's citizenship. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonCitizenship

Set the client's citizenship.

C++
    
    
    MTAPIRES  IMTClient::PersonCitizenship(
       LPCWSTR       citizenship   // Client's citizenship
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonCitizenship(
       string        citizenship   // Client's citizenship
       )

### Parameters

**citizenship**  
[in] Client's citizenship.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The citizenship length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
