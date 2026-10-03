[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching TypeTimeClient

[Previous](IMTHistoryMatching-TypeTime.md) | [Next](IMTHistoryMatching-Price.md)

# IMTECNHistoryMatching::TypeTimeClient

Get the expiration type in the original client order.

C++
    
    
    UINT  IMTECNHistoryMatching::TypeTimeClient()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryMatching.TypeTimeClient()

### Return Value

A value of the [IMTOrder::EnOrderTime (#enordertime)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertime) enumeration.

# IMTECNHistoryMatching::TypeTimeClient

Set the expiration type in the original client order.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::TypeTimeClient(
       const UINT  type      // expiration type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.TypeTimeClient(
       uint        type      // expiration type
       )

### Parameters

**state**  
[in] The expiration type of the matching order. The type is passed using theIMTOrder::EnOrderTimeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
