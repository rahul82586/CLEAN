[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching TypeTime

[Previous](IMTHistoryMatching-TypeFillClient.md) | [Next](IMTHistoryMatching-TypeTimeClient.md)

# IMTECNHistoryMatching::TypeTime

Get the expiration type of the matching order created in the ECN.

C++
    
    
    UINT  IMTECNHistoryMatching::TypeTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryMatching.TypeTime()

### Return Value

A value of the [IMTOrder::EnOrderTime (#enordertime)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertime) enumeration.

# IMTECNHistoryMatching::TypeTime

Set the expiration type of the matching order created in the ECN.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::TypeTime(
       const UINT  type      // expiration type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.TypeTime(
       uint        type      // expiration type
       )

### Parameters

**state**  
[in] The expiration type of the matching order. The type is passed using theIMTOrder::EnOrderTimeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
