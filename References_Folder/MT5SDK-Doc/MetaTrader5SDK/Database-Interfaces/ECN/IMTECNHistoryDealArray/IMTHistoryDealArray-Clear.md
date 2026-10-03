[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Clear

[Previous](IMTHistoryDealArray-Assign.md) | [Next](IMTHistoryDealArray-Add.md)

# IMTECNHistoryDealArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDealArray.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
