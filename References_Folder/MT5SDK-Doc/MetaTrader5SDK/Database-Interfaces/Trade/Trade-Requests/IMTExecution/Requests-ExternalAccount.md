[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests ExternalAccount

[Previous](Requests-ExternalID.md) | [Next](Requests-Action.md)

# IMTExecution::ExternalAccount

Gets the account number in an external trading system.

C++
    
    
    LPCWSTR  IMTExecution::ExternalAccount()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.ExternalAccount()

### Return Value

If successful, it returns a pointer to a string with the account number in an external trading system. Otherwise, it returns NULL. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of [IMTExecution](../Requests-IMTExecution.md) object.

# IMTExecution::ExternalAccount

Set the number of a client's account in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::ExternalAccount(
       LPCWSTR  account      // Account number
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.ExternalAccount(
       string   account      // Account number
       )

### Parameters

**account**  
[in] The number of a client's account in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The account length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
