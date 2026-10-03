[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProvider](../IMTProvider.md) / IMTProvider Clear

[Previous](IMTProvider-Assign.md) | [Next](IMTProvider-ID.md)

# IMTECNProvider::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNProvider::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProvider.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
