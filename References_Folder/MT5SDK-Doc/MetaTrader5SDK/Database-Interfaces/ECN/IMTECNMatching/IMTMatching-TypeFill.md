[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching TypeFill

[Previous](IMTMatching-Type.md) | [Next](IMTMatching-TypeTime.md)

# IMTECNMatching::TypeFill

Get the fill policy used for the matching order.

C++
    
    
    UINT  IMTECNMatching::TypeFill()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNMatching.TypeFill()

### Return Value

A value of the [IMTOrder::EnOrderFilling (#enorderfilling)](../../Trade/Orders/IMTOrder/Enumerations.md#enorderfilling) enumeration.

# IMTECNMatching::TypeFill

Set the fill policy used for the matching order.

C++
    
    
    MTAPIRES  IMTECNMatching::Type(
       const UINT  type      // fill policy
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Type(
       uint        type      // fill policy
       )

### Parameters

**state**  
[in] The fill policy of a matching order. The fill policy is passed using theIMTOrder::EnOrderFillingenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
