[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / OrderNext

[Previous](OrderTotal.md) | [Next](OrderGet.md)

# IMTDaily::OrderNext

Get a [trade order](../../Orders.md) by the index.

C++
    
    
    MTAPIRES  IMTDaily::OrderNext(
       const UINT  pos,       // Position in the list
       IMTOrder*   order      // An order object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.OrderNext(
       uint        pos,       // Position in the list
       CIMTOrder   order      // An order object
       )

### Parameters

**pos**  
[in] Position of a trade order, starting with 0.

**order**  
[out] An object of a trade order. The 'order' object must be first created using theIMTManagerAPI::OrderCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies parameters of a trade order with the specified index to the order object.
