[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Flags

[Previous](IMTMatching-State.md) | [Next](IMTMatching-TimeSetupMsc.md)

# IMTECNMatching::Flags

Get matching order flags.

C++
    
    
    UINT64  IMTECNMatching::Flags()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNMatching.Flags()

### Return Value

[IMTECNMatching::ENCMatchingOrderFlags (#enecnmatchingorderflags)](IMTMatching-Enumerations.md#enecnmatchingorderflags) enumeration value.

# IMTECNMatching::Flags

Set matching order flags.

C++
    
    
    MTAPIRES  IMTECNMatching::Flags(
       const UINT64  flags   // flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Flags(
       ulong         flags   // flags
       )

### Parameters

**state**  
[in] Matching order flags. Flags are passed using theIMTECNMatching::ENCMatchingOrderFlagsenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
