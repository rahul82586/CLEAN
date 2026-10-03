[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCGroup](../IMTConGroup.md) / IMTConGroup Clear

[Previous](IMTConGroup-Assign.md) | [Next](IMTConGroup-Group.md)

# IMTConKYCGroup::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConKYCGroup::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYCGroup.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

This method cleans all fields ​​and removes embedded objects.
