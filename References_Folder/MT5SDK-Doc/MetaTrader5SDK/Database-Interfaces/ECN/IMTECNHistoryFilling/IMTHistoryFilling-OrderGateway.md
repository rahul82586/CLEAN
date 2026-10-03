[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling OrderGateway

[Previous](IMTHistoryFilling-OrderMatching.md) | [Next](IMTHistoryFilling-Login.md)

# IMTECNHistoryFilling::OrderGateway

Get the ticket of the filling order (used within the ECN).

C++
    
    
    UINT64  IMTECNHistoryFilling::OrderGateway()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryFilling.OrderGateway()

### Return Value

The ticket of the filling order.

# IMTECNHistoryFilling::OrderGateway

Set the ticket of the filling order (used within the ECN).

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::OrderGateway(
       const UINT64  order      // order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.OrderGateway(
       ulong         order      // order ticket
       )

### Parameters

**order**  
[in] The ticket of the filling order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
