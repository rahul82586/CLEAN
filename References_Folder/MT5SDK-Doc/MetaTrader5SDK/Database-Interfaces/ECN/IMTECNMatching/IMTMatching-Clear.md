[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Clear

[Previous](IMTMatching-Assign.md) | [Next](IMTMatching-Order.md)

# IMTECNMatching::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNMatching::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
