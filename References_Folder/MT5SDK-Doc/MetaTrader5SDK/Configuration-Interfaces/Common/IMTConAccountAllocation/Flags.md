[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / Flags

[Previous](Description.md) | [Next](Leverages.md)

# IMTConAccountAllocation::Flags

Get additional account allocation settings for the group.

C++
    
    
    UINT  IMTConAccountAllocation::Flags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAccountAllocation.Flags()

### Return Value

[IMTConAccountAllocation::EnFlags (#enflags)](Enumerations.md#enflags) enumeration value.

# IMTConAccountAllocation::Flags

Set additional account allocation settings for the group.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::Flags(
       const UINT  flags     // Account allocation settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.Flags(
       uint        flags      // Account allocation settings
       )

### Parameters

**flags**  
[in] Account allocation settings are passed using theIMTConAccountAllocation::EnFlagsenumeration.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
