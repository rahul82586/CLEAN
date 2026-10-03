[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling OrderMatching

[Previous](IMTHistoryFilling-Order.md) | [Next](IMTHistoryFilling-OrderGateway.md)

# IMTECNHistoryFilling::OrderMatching

Get the ticket of the matching orders used to fill the current order.

C++
    
    
    UINT64  IMTECNHistoryFilling::OrderMatching()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryFilling.OrderMatching()

### Return Value

The ticket of the matching orders used to fill the current order.

# IMTECNHistoryFilling::OrderMatching

Set the ticket of the matching orders used to fill the current order.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::OrderMatching(
       const UINT64  order      // order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.OrderMatching(
       ulong         order      // order ticket
       )

### Parameters

**order**  
[in] The ticket of the matching orders used to fill the current order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
