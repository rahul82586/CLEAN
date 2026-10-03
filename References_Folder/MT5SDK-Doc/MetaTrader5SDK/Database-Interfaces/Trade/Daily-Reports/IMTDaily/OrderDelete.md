[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / OrderDelete

[Previous](OrderUpdate.md) | [Next](OrderClear.md)

# IMTDaily::OrderDelete

Delete a [trade order](../../Orders.md) from a daily report by its index.

C++
    
    
    MTAPIRES  IMTDaily::OrderDelete(
       const UINT  pos      // Position in the list
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.OrderDelete(
       uint        pos      // Position in the list
       )

### Parameters

**pos**  
[in] The position of a trade order in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
