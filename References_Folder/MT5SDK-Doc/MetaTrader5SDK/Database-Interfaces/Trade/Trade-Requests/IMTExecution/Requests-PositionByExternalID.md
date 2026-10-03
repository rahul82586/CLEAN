[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests PositionByExternalID

[Previous](Requests-PositionExternalID.md) | [Next](Requests-PositionPriceSL.md)

# IMTExecution::PositionByExternalID

Gets the ticket (a unique number) of an opposite position in an external trading system.

C++
    
    
    LPCWSTR  IMTExecution::PositionByExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.PositionByExternalID()

### Return Value

The ticket of an opposite position in an external trading system.

### Note

IMTExecution::PositionBy is used for Close By operations.

# IMTExecution::PositionByExternalID

Sets the ticket (a unique number) of an opposite position in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::PositionByExternalID(
       LPCWSTR       id    // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.PositionByExternalID(
       string        id    // Position ticket
       )

### Parameters

**id**  
[in] The ticket of an opposite position in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

IMTExecution::PositionBy is used for Close By operations.
