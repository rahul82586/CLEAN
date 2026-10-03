[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching Type

[Previous](IMTHistoryMatching-SymbolClient.md) | [Next](IMTHistoryMatching-TypeClient.md)

# IMTECNHistoryMatching::Type

Get the type of the order added into the ECN order book.

C++
    
    
    UINT  IMTECNHistoryMatching::Type()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryMatching.Type()

### Return Value

A value of the [IMTOrder::EnOrderType (#enordertype)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertype) enumeration.

# IMTECNHistoryMatching::Type

Set the type of the order added into the ECN order book.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Type(
       const UINT  type      // order type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.Type(
       uint        type      // order type
       )

### Parameters

**state**  
[in] Order type. The type is passed using theEnOrderTypeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
