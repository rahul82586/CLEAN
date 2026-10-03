[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching Order

[Previous](IMTHistoryMatching-Clear.md) | [Next](IMTHistoryMatching-Login.md)

# IMTECNHistoryMatching::Order

Get the ticket of the matching order.

C++
    
    
    UINT64  IMTECNHistoryMatching::Order()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryMatching.Order()

### Return Value

The ticket of the matching order.

# IMTECNHistoryMatching::Order

Set the ticket of the matching order.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Order(
       const UINT64  order      // order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.Order(
       ulong         order      // order ticket
       )

### Parameters

**order**  
[in] The ticket of the matching order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
