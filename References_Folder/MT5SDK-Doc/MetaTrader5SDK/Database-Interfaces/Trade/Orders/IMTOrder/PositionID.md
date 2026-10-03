[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / PositionID

[Previous](ExpertID.md) | [Next](PositionByID.md)

# IMTOrder::PositionID

Gets the position ID (ticket) specified in the order.

C++
    
    
    UINT64  IMTOrder::PositionID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTOrder.PositionID()

Python
    
    
    MTOrder.PositionID()

### Return Value

The position ID set in the order.

### Note

The position ID is used for analyzing the history of working with the position. A unique identifier PositionID is assigned to all orders and deals that open, modify and close this position, as well as to the position itself.

# IMTOrder::PositionID

Sets the position ID (ticket) for the order.

C++
    
    
    MTAPIRES  IMTOrder::PositionID(
       const UINT64  id      // Position ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.PositionID(
       ulong         id      // Position ID
       )

Python
    
    
    MTOrder.PositionID()

### Parameters

**id**  
[in] The position identifier for an order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The position ID is used for analyzing the history of working with the position. A unique identifier PositionID is assigned to all orders and deals that open, modify and close this position, as well as to the position itself.
