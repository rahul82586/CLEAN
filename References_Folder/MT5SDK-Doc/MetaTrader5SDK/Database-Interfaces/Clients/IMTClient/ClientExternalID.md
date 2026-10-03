[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ClientExternalID

[Previous](ClientOriginLogin.md) | [Next](../IMTClientArray.md)

# IMTClient::ClientExternalID

Get the client ID in an external trading system.

C++
    
    
    LPCWSTR  IMTClient::ClientExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.ClientExternalID()

### Return Value

If successful, the method returns a pointer to the string with the identifier. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::ClientExternalID

Set the client ID in an external trading system.

C++
    
    
    MTAPIRES  IMTClient::ClientExternalID(
       LPCWSTR       external_id   // ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ClientExternalID(
       string        external_id   // ID
       )

### Parameters

**external_id**  
[in] Client ID in the external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The ID length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
