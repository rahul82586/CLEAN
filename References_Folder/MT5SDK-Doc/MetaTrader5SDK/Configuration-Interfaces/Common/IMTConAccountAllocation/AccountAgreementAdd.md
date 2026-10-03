[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / AccountAgreementAdd

[Previous](ConfirmationEmail.md) | [Next](AccountAgreementUpdate.md)

# IMTConAccountAllocation::AccountAgreementAdd

Add an agreement to the account allocation configuration.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAgreementAdd(
       IMTConAccountAgreement*  cfg    // Agreement configuration object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAgreementAdd(
       CIMTConAccountAgreement  cfg   // Agreement configuration object
       )

### Parameters

**cfg**  
[in] Agreement configuration objectIMTConAccountAgreement.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
