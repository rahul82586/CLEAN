[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonTitle

[Previous](Introducer.md) | [Next](PersonName.md)

# IMTClient::PersonTitle

Get the client title, such as Mr. or Mrs.

C++
    
    
    LPCWSTR  IMTClient::PersonTitle()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonTitle()

### Return Value

If successful, the method returns a pointer to a string with the title. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonTitle

Set the client title, such as Mr. or Mrs.

C++
    
    
    MTAPIRES  IMTClient::PersonTitle(
       LPCWSTR       title       // Title
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonTitle(
       string        title       // Title
       )

### Parameters

**title**  
[in] Client title, such as Mr. or Mrs.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The title length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
