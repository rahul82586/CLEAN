[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon AccountAllocationDelete

[Previous](IMTCon-AccountAllocationUpdate.md) | [Next](IMTCon-AccountAllocationClear.md)

# IMTConAccountAllocation::AccountAllocationDelete

Delete an account allocation configuration.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAllocationDelete(
       const UINT  pos      // Configuration position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAllocationDelete(
       uint        pos      // Configuration position
       )

### Parameters

**pos**  
[in] The position of the configuration in the list, starting from 0.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
