[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / Flags

[Previous](Manager.md) | [Next](Type.md)

# IMTConFund::Flags

Get additional fund properties.

C++
    
    
    UINT  IMTConFund::Flags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.Flags()

### Return Value

Additional fund properties as flags from the [IMTConFund::EnFlags (#enflags)](Enumerations.md#enflags) enumeration.

# IMTConFund::Flags

Set additional fund properties.

C++
    
    
    MTAPIRES  IMTConFund::Flags(
       const UINT  flags     // Flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.Flags(
       uint        flags     // Flags
       )

### Parameters

**flags**  
[in] Additional fund properties as flags from theIMTConFund::EnFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
