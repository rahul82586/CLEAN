[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon GroupAdd

[Previous](IMTCon-CountryNext.md) | [Next](IMTCon-GroupUpdate.md)

# IMTConKYC::GroupAdd

Add a group of accounts for which the KYC provider will be used.

C++
    
    
    MTAPIRES  IMTConKYC::GroupAdd(
       IMTConKYCGroup*  group      // Group object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.GroupAdd(
       CIMTConKYCGroup  group      // Group object
       )

### Parameters

**group**  
[in] TheIMTConKYCGroupgroup object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
