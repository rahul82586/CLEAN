[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon AccountAllocationAdd

[Previous](IMTCon-AccountWithdrawalURL.md) | [Next](IMTCon-AccountAllocationUpdate.md)

# IMTConAccountAllocation::AccountAllocationAdd

Add an account allocation configuration.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAllocationAdd(
       IMTConAccountAllocation*  cfg   // Configuration object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAllocationAdd(
       CIMTConAccountAllocation  cfg  // Configuration object
       )

### Parameters

**cfg**  
[in] Account allocation configuration objectIMTConAccountAllocation.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
