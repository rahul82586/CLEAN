[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon AccountAllocationNext

[Previous](IMTCon-AccountAllocationTotal.md) | [Next](../IMTConAccountAllocation.md)

# IMTConAccountAllocation::AccountAllocationNext

Get the account allocation configuration by index.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::AccountAllocationNext(
       const UINT                pos,   // Configuration position
       IMTConAccountAllocation*  cfg    // Configuration object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.AccountAllocationNext(
       uint                      pos,   // Configuration position
       CIMTConAccountAllocation  cfg    // Configuration object
       )

### Parameters

**pos**  
[in] The position of the configuration in the list, starting from 0.

**cfg**  
[out] Account allocation configuration objectIMTConAccountAllocation. The object must first be created using theIMTServerAPI::CommonCreateAllocation,IMTReportAPI::CommonCreateAllocationorIMTAdminAPI::CommonCreateAllocationmethod.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method copies the parameters of the configuration with the specified index into the 'cfg' object.
