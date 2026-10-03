[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Clear

[Previous](IMTHistoryFilling-Assign.md) | [Next](IMTHistoryFilling-Order.md)

# IMTECNHistoryFilling::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
