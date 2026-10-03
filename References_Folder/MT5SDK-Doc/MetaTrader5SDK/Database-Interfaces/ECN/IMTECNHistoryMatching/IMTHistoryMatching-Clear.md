[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching Clear

[Previous](IMTHistoryMatching-Assign.md) | [Next](IMTHistoryMatching-Order.md)

# IMTECNHistoryMatching::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
