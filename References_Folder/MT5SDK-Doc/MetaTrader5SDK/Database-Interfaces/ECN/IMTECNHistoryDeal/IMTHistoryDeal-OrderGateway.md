[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal OrderGateway

[Previous](IMTHistoryDeal-Order.md) | [Next](IMTHistoryDeal-DealGateway.md)

# IMTECNHistoryDeal::OrderGateway

Get the internal ticket of the filling order (which is used within the ECN for internal purposes).

C++
    
    
    UINT64  IMTECNHistoryDeal::OrderGateway()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryDeal.OrderGateway()

### Return Value

The internal ticket of the filling order.

# IMTECNHistoryDeal::OrderGateway

Set the internal ticket of the filling order (which is used within the ECN for internal purposes).

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::OrderGateway(
       const UINT64  order      // order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.OrderGateway(
       ulong         order      // order ticket
       )

### Parameters

**order**  
[in] The internal ticket of the filling order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
