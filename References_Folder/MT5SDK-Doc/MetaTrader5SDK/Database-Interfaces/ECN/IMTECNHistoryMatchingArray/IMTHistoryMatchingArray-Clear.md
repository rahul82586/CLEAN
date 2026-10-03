[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatchingArray](../IMTHistoryMatchingArray.md) / IMTHistoryMatchingArray Clear

[Previous](IMTHistoryMatchingArray-Assign.md) | [Next](IMTHistoryMatchingArray-Add.md)

# IMTECNHistoryMatchingArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNHistoryMatchingArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
