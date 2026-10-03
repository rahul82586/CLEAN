[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching TypeTime

[Previous](IMTMatching-TypeFill.md) | [Next](IMTMatching-Price.md)

# IMTECNMatching::TypeTime

Get the matching order expiration type.

C++
    
    
    UINT  IMTECNMatching::TypeTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNMatching.TypeTime()

### Return Value

A value of the [IMTOrder::EnOrderTime (#enordertime)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertime) enumeration.

# IMTECNMatching::TypeTime

Set the matching order expiration type.

C++
    
    
    MTAPIRES  IMTECNMatching::TypeTime(
       const UINT  type      // expiration type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.TypeTime(
       uint        type      // expiration type
       )

### Parameters

**state**  
[in] The expiration type of the matching order. The type is passed using theIMTOrder::EnOrderTimeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
