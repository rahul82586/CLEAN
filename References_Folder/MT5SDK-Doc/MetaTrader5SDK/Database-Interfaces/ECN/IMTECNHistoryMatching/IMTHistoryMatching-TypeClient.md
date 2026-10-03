[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching TypeClient

[Previous](IMTHistoryMatching-Type.md) | [Next](IMTHistoryMatching-TypeFill.md)

# IMTECNHistoryMatching::TypeClient

Get the type of the order placed on the client side.

C++
    
    
    UINT  IMTECNHistoryMatching::TypeClient()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryMatching.TypeClient()

### Return Value

A value of the [IMTOrder::EnOrderType (#enordertype)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertype) enumeration.

# IMTECNHistoryMatching::TypeClient

Set the type of the order placed on the client side.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::TypeClient(
       const UINT  type      // order type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.TypeClient(
       uint        type      // order type
       )

### Parameters

**state**  
[in] Order type. The type is passed using theEnOrderTypeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
