[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon AccountAllocationClear

[Previous](IMTCon-AccountAllocationDelete.md) | [Next](IMTCon-AccountAllocationShift.md)

# IMTConAccountAllocation::AccountAllocationClear

Clear the list of account allocation configurations.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAllocationClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAllocationClear()

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method deletes all account allocation configurations.
