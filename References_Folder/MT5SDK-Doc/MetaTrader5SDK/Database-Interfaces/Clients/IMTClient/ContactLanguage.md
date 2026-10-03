[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ContactLanguage

[Previous](ContactPreferred.md) | [Next](ContactEmail.md)

# IMTClient::ContactLanguage

Get the language spoken by the client.

C++
    
    
    LPCWSTR  IMTClient::ContactLanguage()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.ContactLanguage()

### Return Value

If successful, a pointer to a string with the language name is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::ContactLanguage

Set the language spoken by the client.

C++
    
    
    MTAPIRES  IMTClient::ContactLanguage(
       LPCWSTR       language     // Client language
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ContactLanguage(
       string        language     // Client language
       )

### Parameters

**language**  
[in] The language spoken by the client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The language is specified in the LANGID format used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) systems (a value from Prim.lang.identifier).
