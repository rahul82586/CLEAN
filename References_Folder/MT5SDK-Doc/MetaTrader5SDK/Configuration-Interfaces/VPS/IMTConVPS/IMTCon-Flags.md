[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon Flags

[Previous](IMTCon-Clear.md) | [Next](IMTCon-MQL5Login.md)

# IMTConVPS::Flags

Get additional Sponsored VPS settings.

C++
    
    
    UINT64  IMTConVPS::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnFlags  CIMTConVPS.Flags()

Python
    
    
    MTConVPS.Flags

### Return Value

Additional settings as the values of the [IMTConVPS::EnFlags (#enflags)](IMTCon-Enumerations.md#enflags) enumeration.

# IMTConVPS::Flags

Set additional Sponsored VPS settings.

C++
    
    
    MTAPIRES  IMTConVPS::Flags(
       const UINT64  flags   // Sponsored VPS settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.Flags(
       EnFlags       flags   // Sponsored VPS settings
       )

Python
    
    
    MTConVPS.Flags

### Parameters

**flags**  
[in] Additional settings as the values of theIMTConVPS::EnFlagsenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
