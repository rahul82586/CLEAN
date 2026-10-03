[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / ExpertPositionID

[Previous](ExpertID.md) | [Next](Comment.md)

# IMTPosition::ExpertPositionID

Get the ID of a position.

C++
    
    
    UINT64  IMTPosition::ExpertPositionID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTPosition.ExpertPositionID()

### Return Value

Position ID.

# IMTPosition::ExpertPositionID

Set the ID of a position.

C++
    
    
    MTAPIRES  IMTPosition::ExpertPositionID(
       const UINT64  id      // Position ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.ExpertPositionID(
       ulong         id      // Position ID
       )

### Parameters

**id**  
[in] Position ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The position ID is used for analyzing the history of working with the position. A unique identifier ExpertPositionID is assigned to all orders and deals that open, modify and close this position, as well as to the position itself. This identifier corresponds to the ticket of the order, the execution of which resulted in position opening.
