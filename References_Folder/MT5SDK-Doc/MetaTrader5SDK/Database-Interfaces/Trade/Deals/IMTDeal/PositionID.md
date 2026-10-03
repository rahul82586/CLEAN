[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / PositionID

[Previous](ExpertID.md) | [Next](Comment.md)

# IMTDeal::PositionID

Gets the position ID (ticket) specified in the deal.

C++
    
    
    UINT64  IMTDeal::PositionID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.PositionID()

### Return Value

The position ID set in the deal.

### Note

The position ID is used for analyzing the history of working with the position. A unique identifier PositionID is assigned to all orders and deals that open, modify and close this position, as well as to the position itself. This identifier corresponds to the ticket of the order, the execution of which resulted in position opening.

# IMTDeal::PositionID

Sets the position ID (ticket) for a deal.

C++
    
    
    MTAPIRES  IMTDeal::PositionID(
       const UINT64  id      // Position ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.PositionID(
       ulong         id      // Position ID
       )

### Parameters

**id**  
[in] The position identifier for a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The position ID is used for analyzing the history of working with the position. A unique identifier PositionID is assigned to all orders and deals that open, modify and close this position, as well as to the position itself. This identifier corresponds to the ticket of the order, the execution of which resulted in position opening.
