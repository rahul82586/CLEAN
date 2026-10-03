[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Clear

[Previous](IMTHistoryDeal-Assign.md) | [Next](IMTHistoryDeal-Order.md)

# IMTECNHistoryDeal::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
