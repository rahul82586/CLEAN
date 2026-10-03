[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealExternalID

[Previous](Requests-OrderPriceTP.md) | [Next](Requests-DealAction.md)

# IMTExecution::DealExternalID

Gets a deal ID in an external trading system.

C++
    
    
    LPCWSTR  IMTExecution::DealExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.DealExternalID()

### Return Value

If successful, it returns a pointer to the string with the deal identifier. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of [IMTExecution](../Requests-IMTExecution.md) object.

# IMTExecution::DealExternalID

Sets the ID of a deal in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::DealExternalID(
       LPCWSTR  id      // Deal ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealExternalID(
       string   id      // Deal ID
       )

### Parameters

**id**  
[in] The ID of a deal in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The ID length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
