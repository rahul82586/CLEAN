[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon GroupClear

[Previous](IMTCon-GroupDelete.md) | [Next](IMTCon-GroupShift.md)

# IMTConKYC::GroupClear

Clear the list of groups for which the KYC provider is used.

C++
    
    
    MTAPIRES  IMTConKYC::GroupClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.GroupClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

This method removes from the list all groups for which the KYC provider is used.
