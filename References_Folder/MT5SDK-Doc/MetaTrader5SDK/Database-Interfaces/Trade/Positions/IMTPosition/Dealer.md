[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Dealer

[Previous](ApiDataClearAll.md) | [Next](APIDataNext.md)

# IMTPosition::Dealer

Gets the login of a dealer, who has processed the order that opened the position.

C++
    
    
    UINT64  IMTPosition::Dealer()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTPosition.Dealer()

### Return Value

The login of a dealer, who has processed the order that opened the position. If an order was processed automatically by the server, 0 is returned.

# IMTPosition::Dealer

Set the login of a dealer, who has processed an order.

C++
    
    
    MTAPIRES  IMTPosition::Dealer(
       const UINT64  dealer      // Dealer
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Dealer(
       ulong         dealer      // Dealer
       )

### Parameters

**dealer**  
[in] The login of a dealer, who has processed the order that opened the position. 0 means that the order was processed automatically by the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The dealer identifier is specified in positions in accordance with the dealer ID in the order, the execution of which resulted in position creation.
