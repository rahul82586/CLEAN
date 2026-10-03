[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon GroupDelete

[Previous](IMTCon-GroupUpdate.md) | [Next](IMTCon-GroupClear.md)

# IMTConKYC::GroupDelete

Delete the group of accounts for which the KYC provider is used.

C++
    
    
    MTAPIRES  IMTConKYC::GroupDelete(
       const UINT  pos      // Group position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.GroupDelete(
       uint        pos      // Group position
       )

### Parameters

**pos**  
[in] Group position in the list, starting from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
