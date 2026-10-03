[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonTaxID

[Previous](PersonGender.md) | [Next](PersonDocumentType.md)

# IMTClient::PersonTaxID

Get the client's tax ID, for example TIN.

C++
    
    
    LPCWSTR  IMTClient::PersonTaxID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.PersonTaxID()

### Return Value

If successful, a pointer to a string with the tax payer ID is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::PersonTaxID

Set the client's tax ID, for example TIN.

C++
    
    
    MTAPIRES  IMTClient::PersonTaxID(
       LPCWSTR       taxid         // Tax ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonTaxID(
       string        taxid         // Tax ID
       )

### Parameters

**taxid**  
[in] Tax ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The ID length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
