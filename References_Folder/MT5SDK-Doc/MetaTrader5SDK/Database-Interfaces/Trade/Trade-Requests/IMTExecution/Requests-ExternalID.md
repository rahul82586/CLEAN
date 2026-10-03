[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests ExternalID

[Previous](Requests-ID.md) | [Next](Requests-ExternalAccount.md)

# IMTExecution::ExternalID

Gets the ID of a trade execution in an external trading system.

C++
    
    
    LPCWSTR  IMTExecution::ExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.ExternalID()

### Return Value

If successful, it returns a pointer to the string with the trade execution identifier. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of [IMTExecution](../Requests-IMTExecution.md) object.

# IMTExecution::ExternalID

Sets the ID of a trade execution in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::ExternalID(
       LPCWSTR  id      // Trade execution ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.ExternalID(
       string   id      // Trade execution ID
       )

### Parameters

**id**  
[in] The ID of a trade execution in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The ID length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
