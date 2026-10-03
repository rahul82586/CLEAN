[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / OrderAdd

[Previous](PositionGet.md) | [Next](OrderUpdate.md)

# IMTDaily::OrderAdd

Add a [trade order](../../Orders.md) to the daily report.

C++
    
    
    MTAPIRES  IMTDaily::OrderAdd(
       IMTOrder*  order      // An order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.OrderAdd(
       CIMTOrder  order      // An order object
       )

### Parameters

**order**  
[in] An object of a trading order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
