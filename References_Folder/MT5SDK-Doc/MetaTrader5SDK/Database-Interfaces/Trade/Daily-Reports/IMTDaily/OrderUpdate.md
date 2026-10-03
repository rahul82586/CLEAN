[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / OrderUpdate

[Previous](OrderAdd.md) | [Next](OrderDelete.md)

# IMTDaily::OrderUpdate

Modify a [trade order](../../Orders.md) in a daily report by its index.

C++
    
    
    MTAPIRES  IMTDaily::OrderUpdate(
       const UINT       pos,       // Position in the list 
       const IMTOrder*  order      // An order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.OrderUpdate(
       uint             pos,       // Position in the list 
       CIMTOrder        order      // Order object
       )

### Parameters

**pos**  
[in] The position of a trade order in the list, starting with 0.

**order**  
[in] An object of a trading order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
