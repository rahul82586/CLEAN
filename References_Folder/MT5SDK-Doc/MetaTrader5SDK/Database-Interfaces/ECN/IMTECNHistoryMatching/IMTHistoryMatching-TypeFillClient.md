[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching TypeFillClient

[Previous](IMTHistoryMatching-TypeFill.md) | [Next](IMTHistoryMatching-TypeTime.md)

# IMTECNHistoryMatching::TypeFillClient

Get the fill policy used in the original client order.

C++
    
    
    UINT  IMTECNHistoryMatching::TypeFillClient()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryMatching.TypeFillClient()

### Return Value

A value of the [IMTOrder::EnOrderFilling (#enorderfilling)](../../Trade/Orders/IMTOrder/Enumerations.md#enorderfilling) enumeration.

# IMTECNHistoryMatching::TypeFillClient

Set the fill policy used in the original client order.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::TypeFillClient(
       const UINT  type      // fill policy
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.TypeFillClient(
       uint        type      // fill policy
       )

### Parameters

**state**  
[in] The fill policy of a matching order. The fill policy is passed using theIMTOrder::EnOrderFillingenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
