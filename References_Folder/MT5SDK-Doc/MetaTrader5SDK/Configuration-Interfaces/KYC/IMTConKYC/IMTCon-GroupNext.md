[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon GroupNext

[Previous](IMTCon-GroupTotal.md) | [Next](../IMTConCountry.md)

# IMTConKYC::GroupNext

Get the group for which the KYC provider is used by its index in the list.

C++
    
    
    MTAPIRES  IMTConKYC::GroupNext(
       const UINT       pos,       // Group position
       IMTConKYCGroup*  group      // Group object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.GroupNext(
       uint             pos,       // Group position
       CIMTConKYCGroup  group      // Group object
       )

### Parameters

**pos**  
[in] Group position in the list, starting from 0.

**group**  
[out] Group object. The 'group' object must be created in advance using theIMTServerAPI::KYCGroupCreateorIMTAdminAPI::KYCGroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
