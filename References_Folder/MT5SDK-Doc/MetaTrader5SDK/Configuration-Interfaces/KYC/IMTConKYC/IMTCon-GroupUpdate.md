[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon GroupUpdate

[Previous](IMTCon-GroupAdd.md) | [Next](IMTCon-GroupDelete.md)

# IMTConKYC::GroupUpdate

Change the group of accounts for which the KYC provider is used.

C++
    
    
    MTAPIRES  IMTConKYC::GroupUpdate(
       const UINT               pos,      // Group position
       const IMTConKYCGroup*    group     // Group position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.GroupUpdate(
       uint                     pos,      // Group position
       CIMTConKYCGroup          group     // Group position
       )

### Parameters

**pos**  
[in] Group position in the list, starting from 0.

**group**  
[in] Account group objectIMTConKYCGroup.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
