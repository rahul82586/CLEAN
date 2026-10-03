[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Type

[Previous](IMTMatching-SymbolClient.md) | [Next](IMTMatching-TypeFill.md)

# IMTECNMatching::Type

Get the type of the order added into the ECN order book.

C++
    
    
    UINT  IMTECNMatching::Type()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNMatching.Type()

### Return Value

A value of the [IMTOrder::EnOrderType (#enordertype)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertype) enumeration.

# IMTECNMatching::Type

Set the type of the order added into the ECN order book.

C++
    
    
    MTAPIRES  IMTECNMatching::Type(
       const UINT  type      // order type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Type(
       uint        type      // order type
       )

### Parameters

**state**  
[in] Order type. The type is passed using theEnOrderTypeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
