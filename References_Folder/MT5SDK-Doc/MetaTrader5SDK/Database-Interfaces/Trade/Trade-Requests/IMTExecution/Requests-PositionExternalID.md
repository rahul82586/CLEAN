[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests PositionExternalID

[Previous](Requests-PositionBy.md) | [Next](Requests-PositionByExternalID.md)

# IMTExecution::PositionExternalID

Gets the ticket (a unique number) of a position in an external trading system.

C++
    
    
    LPCWSTR  IMTExecution::PositionExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.PositionExternalID()

### Return Value

The ticket of a position in an external trading system.

# IMTExecution::PositionExternalID

Sets the ticket (a unique number) of a position in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::PositionExternalID(
       LPCWSTR       id    // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.PositionExternalID(
       string        id    // Position ticket
       )

### Parameters

**id**  
[in] The ticket of a position in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
