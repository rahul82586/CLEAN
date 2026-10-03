[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Clear

[Previous](IMTFilling-Assign.md) | [Next](IMTFilling-Login.md)

# IMTECNFilling::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTECNFilling::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method deletes data from all fields ​​and removes embedded objects.
