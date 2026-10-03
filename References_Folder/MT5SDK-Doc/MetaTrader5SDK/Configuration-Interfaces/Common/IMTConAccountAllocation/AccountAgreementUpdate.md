[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / AccountAgreementUpdate

[Previous](AccountAgreementAdd.md) | [Next](AccountAgreementDelete.md)

# IMTConAccountAllocation::AccountAgreementUpdate

Edit an agreement in the account allocation configuration.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAgreementUpdate(
       const UINT                     pos,   // Agreement position
       const IMTConAccountAgreement*  cfg    // Agreement configuration object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAgreementUpdate(
       uint                           pos,    // Agreement position
       CIMTConAccountAgreement        cfg     // Agreement configuration object
       )

### Parameters

**pos**  
[in] The position of the agreement in the list, starting from 0.

**cfg**  
[in] Agreement configuration objectIMTConAccountAgreement.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
