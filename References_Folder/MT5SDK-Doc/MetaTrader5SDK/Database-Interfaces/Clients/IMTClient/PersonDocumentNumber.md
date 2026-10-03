[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonDocumentNumber

[Previous](PersonDocumentType.md) | [Next](PersonDocumentDate.md)

# IMTClient::PersonDocumentNumber

Get the number of the identification document (of passport, driver's license, etc.).

C++
    
    
    LPCWSTR  IMTClient::PersonDocumentNumber()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonDocumentNumber()

### Return Value

If successful, a pointer to a string with the document number is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonDocumentNumber

Set the number of the identification document (of passport, driver's license, etc.).

C++
    
    
    MTAPIRES  IMTClient::PersonDocumentNumber(
       LPCWSTR       number        // Document number
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonDocumentNumber(
       string        number        // Document number
       )

### Parameters

**number**  
[in] Identification document number.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The document number length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
