[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonDocumentType

[Previous](PersonTaxID.md) | [Next](PersonDocumentNumber.md)

# IMTClient::PersonDocumentType

Get the client's identification document type: passport, driver's license, etc.

C++
    
    
    LPCWSTR  IMTClient::PersonDocumentType()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonDocumentType()

### Return Value

If successful, a pointer to a string with the document name is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonDocumentType

Set the client's identification document type: passport, driver's license, etc.

C++
    
    
    MTAPIRES  IMTClient::PersonDocumentType(
       LPCWSTR       type          // Document name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonDocumentType(
       string        type          // Document name
       )

### Parameters

**type**  
[in] Identification document name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The document name length is limited to 16 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
