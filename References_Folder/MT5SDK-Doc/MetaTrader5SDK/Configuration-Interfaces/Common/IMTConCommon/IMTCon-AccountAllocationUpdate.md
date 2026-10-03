[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon AccountAllocationUpdate

[Previous](IMTCon-AccountAllocationAdd.md) | [Next](IMTCon-AccountAllocationDelete.md)

# IMTConAccountAllocation::AccountAllocationUpdate

Edit an account allocation configuration.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAllocationUpdate(
       const UINT                     pos,   // Configuration position
       const IMTConAccountAgreement*  cfg    // Configuration object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAllocationUpdate(
       uint                           pos,    // Configuration position
       CIMTConAccountAgreement        cfg     // Configuration object
       )

### Parameters

**pos**  
[in] The position of the configuration in the list, starting from 0.

**cfg**  
[in] Account allocation configuration objectIMTConAccountAllocation.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
