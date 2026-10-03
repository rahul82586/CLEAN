[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonDocumentExtra

[Previous](PersonDocumentExpiration.md) | [Next](PersonEmployment.md)

# IMTClient::PersonDocumentExtra

Get additional information (comment) to the identification document.

C++
    
    
    LPCWSTR  IMTClient::PersonDocumentExtra()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonDocumentExtra()

### Return Value

If successful, a pointer to a string with the additional document data is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonDocumentExtra

Set additional information (comment) to the identification document.

C++
    
    
    MTAPIRES  IMTClient::PersonDocumentExtra(
       LPCWSTR       extra         // Document information
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonDocumentExtra(
       string        extra         // Document information
       )

### Parameters

**extra**  
[in] Additional information about the document.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The data length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
