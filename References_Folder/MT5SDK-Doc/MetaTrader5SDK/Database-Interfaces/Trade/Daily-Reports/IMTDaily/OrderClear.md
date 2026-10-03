[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / OrderClear

[Previous](OrderDelete.md) | [Next](OrderShift.md)

# IMTDaily::OrderClear

Clear the list of [orders](../../Orders.md) in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::OrderClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.OrderClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears the entire list of orders in a daily report.
