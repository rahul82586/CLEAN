[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / AccountAgreementDelete

[Previous](AccountAgreementUpdate.md) | [Next](AccountAgreementClear.md)

# IMTConAccountAllocation::AccountAgreementDelete

Remove an agreement from the account allocation configuration.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAgreementDelete(
       const UINT  pos      // Agreement position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAgreementDelete(
       uint        pos      // Agreement position
       )

### Parameters

**pos**  
[in] The position of the agreement in the list, starting from 0.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
