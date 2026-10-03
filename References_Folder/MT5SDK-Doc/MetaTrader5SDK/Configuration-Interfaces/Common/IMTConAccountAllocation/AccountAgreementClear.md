[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / AccountAgreementClear

[Previous](AccountAgreementDelete.md) | [Next](AccountAgreementShift.md)

# IMTConAccountAllocation::AccountAgreementClear

Clear the list of agreements in the account allocation configuration.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAgreementClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAgreementClear()

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears the entire list of agreements in the account allocation setting for the given group.
