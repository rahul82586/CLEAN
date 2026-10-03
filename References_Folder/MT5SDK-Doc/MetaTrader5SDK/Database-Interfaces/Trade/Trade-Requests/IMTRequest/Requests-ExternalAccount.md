[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ExternalAccount

[Previous](Requests-Login.md) | [Next](Requests-Group.md)

# IMTRequest::ExternalAccount

Gets a client's account in an external trading system.

C++
    
    
    LPCWSTR  IMTRequest::ExternalAccount()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.ExternalAccount()

### Return Value

If successful, it returns a pointer to a string with the account number. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTRequest](../Requests-IMTRequest.md) object.

# IMTRequest::ExternalAccount

Sets a client's account in an external trading system.

C++
    
    
    MTAPIRES  IMTRequest::ExternalAccount(
       LPCWSTR  account      // Account
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.ExternalAccount(
       string   account      // Account
       )

### Parameters

**symbol**  
[in] An account in the external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The account length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
