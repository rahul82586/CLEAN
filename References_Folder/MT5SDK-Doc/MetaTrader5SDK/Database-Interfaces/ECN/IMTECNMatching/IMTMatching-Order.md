[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Order

[Previous](IMTMatching-Clear.md) | [Next](IMTMatching-Login.md)

# IMTECNMatching::Order

Get the ticket of the matching order.

C++
    
    
    UINT64  IMTECNMatching::Order()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNMatching.Order()

### Return Value

The ticket of the matching order.

# IMTECNMatching::Order

Set the ticket of the matching order.

C++
    
    
    MTAPIRES  IMTECNMatching::Order(
       const UINT64  order      // order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Order(
       ulong         order      // order ticket
       )

### Parameters

**order**  
[in] The ticket of the matching order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
