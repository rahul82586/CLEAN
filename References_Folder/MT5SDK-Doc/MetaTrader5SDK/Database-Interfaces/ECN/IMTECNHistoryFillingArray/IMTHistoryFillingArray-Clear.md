[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFillingArray](../IMTHistoryFillingArray.md) / IMTHistoryFillingArray Clear

[Previous](IMTHistoryFillingArray-Assign.md) | [Next](IMTHistoryFillingArray-Add.md)

# IMTECNHistoryFillingArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNHistoryFillingArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFillingArray.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
