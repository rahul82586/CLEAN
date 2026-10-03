[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PositionByExternalID

[Previous](Requests-PositionExternalID.md) | [Next](Requests-Reason.md)

# IMTRequest::PositionByExternalID

Gets the ticket (a unique number) of an opposite position in an external trading system.

C++
    
    
    LPCWSTR  IMTRequest::PositionByExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.PositionByExternalID()

### Return Value

The ticket of an opposite position in an external trading system.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTRequest](../Requests-IMTRequest.md) object.

# IMTRequest::PositionByExternalID

Sets the ticket (a unique number) of an opposite position in an external trading system.

C++
    
    
    MTAPIRES  IMTRequest::PositionByExternalID(
       LPCWSTR       id    // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.PositionByExternalID(
       string        id    // Position ticket
       )

### Parameters

**id**  
[in] The ticket of an opposite position in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

IMTExecution::PositionBy is used for Close By operations.
