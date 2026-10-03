[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon AccountAllocationShift

[Previous](IMTCon-AccountAllocationClear.md) | [Next](IMTCon-AccountAllocationTotal.md)

# IMTConAccountAllocation::AccountAllocationShift

Move the account allocation configuration in the list.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAllocationShift(
       const UINT  pos,       // Configuration position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAllocationShift(
       uint        pos,       // Configuration position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] The position of the configuration in the list, starting from 0.

**shift**  
[in] Configuration shift relative to its current position. A negative value means shift towards the top of the list, and a positive value shifts the item towards the end.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
