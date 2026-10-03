[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / IEVolumeMax

[Previous](IESlipLosing.md) | [Next](IEVolumeMaxExt.md)

# IMTConSymbol::IEVolumeMax

Gets the maximum volume of a trade operation that can be executed in the instant execution mode.

C++
    
    
    UINT64  IMTConSymbol::IEVolumeMax()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConSymbol.IEVolumeMax()

Python (Manager API)
    
    
    MTConSymbol.IEVolumeMax

### Return Value

The maximum volume of a trade operation that can be executed in the instant execution mode in the UINT64 format (one unit is equal to 1/10,000 of a lot). In case this limit is exceeded, trade operations are processed in the manual execution mode.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConSymbol::IEVolumeMax](IEVolumeMax.md) method.

# IMTConSymbol::IEVolumeMax

Sets the maximum volume of a trade operation that can be executed in the instant execution mode.

C++
    
    
    MTAPIRES  IMTConSymbol::IEVolumeMax(
       const UINT64  volume      // Maximum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.IEVolumeMax(
       ulong         volume      // Maximum volume
       )

Python (Manager API)
    
    
    MTConSymbol.IEVolumeMax

### Parameters

**volume**  
[in] The maximum volume of a trade operation that can be executed in the instant execution mode in the UINT64 format (one unit is equal to 1/10,000 of a lot). In case this limit is exceeded, trade operations are processed in the manual execution mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConSymbol::IEVolumeMax](IEVolumeMax.md) method.
