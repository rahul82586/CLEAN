[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching TypeFill

[Previous](IMTHistoryMatching-TypeClient.md) | [Next](IMTHistoryMatching-TypeFillClient.md)

# IMTECNHistoryMatching::TypeFill

Get the fill policy of the matching order created in the ECN.

C++
    
    
    UINT  IMTECNHistoryMatching::TypeFill()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryMatching.TypeFill()

### Return Value

A value of the [IMTOrder::EnOrderFilling (#enorderfilling)](../../Trade/Orders/IMTOrder/Enumerations.md#enorderfilling) enumeration.

# IMTECNHistoryMatching::TypeFill

Set the fill policy of the matching order created in the ECN.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Type(
       const UINT  type      // fill policy
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.Type(
       uint        type      // fill policy
       )

### Parameters

**state**  
[in] The fill policy of a matching order. The fill policy is passed using theIMTOrder::EnOrderFillingenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
