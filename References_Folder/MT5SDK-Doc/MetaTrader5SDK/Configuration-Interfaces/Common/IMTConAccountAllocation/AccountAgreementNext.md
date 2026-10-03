[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / AccountAgreementNext

[Previous](AccountAgreementTotal.md) | [Next](../IMTConAccountAgreement.md)

# IMTConAccountAllocation::AccountAgreementNext

Get agreement by index.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAgreementNext(
       const UINT               pos,    // Agreement position
       IMTConAccountAgreement*  cfg     // Agreement configuration object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAgreementNext(
       uint                     pos,   // Agreement position
       CIMTConAccountAgreement  cfg    // Agreement configuration object
       )

### Parameters

**pos**  
[in] The position of the agreement in the list, starting from 0.

**cfg**  
[out] Agreement configuration objectIMTConAccountAgreement. The object must first be created using theIMTServerAPI::CommonCreateAgreement,IMTReportAPI::CommonCreateAgreementorIMTAdminAPI::CommonCreateAgreementmethod.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method copies the parameters of the agreement with the specified index into the 'cfg' object.
