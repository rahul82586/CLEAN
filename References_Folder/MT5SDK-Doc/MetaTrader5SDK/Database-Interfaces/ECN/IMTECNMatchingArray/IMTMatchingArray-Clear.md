[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatchingArray](../IMTMatchingArray.md) / IMTMatchingArray Clear

[Previous](IMTMatchingArray-Assign.md) | [Next](IMTMatchingArray-Add.md)

# IMTECNMatchingArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNMatchingArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatchingArray.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
