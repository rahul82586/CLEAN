[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray Clear

[Previous](IMTFillingArray-Assign.md) | [Next](IMTFillingArray-Add.md)

# IMTECNFillingArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNFillingArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFillingArray.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
