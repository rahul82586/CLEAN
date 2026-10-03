[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / IEVolumeMaxExt

[Previous](IEVolumeMax.md) | [Next](IEVolumeMaxDefault.md)

# IMTConGroupSymbol::IEVolumeMaxExt

Gets the maximum volume (with extended accuracy) of a trade operation that can be executed in the instant execution mode.

C++
    
    
    UINT64  IMTConGroupSymbol::IEVolumeMaxExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.IEVolumeMaxExt()

Python (Manager API)
    
    
    MTConGroupSymbol.IEVolumeMaxExt

### Return Value

The maximum volume of a trade operation that can be executed in the instant execution mode, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots). In case this limit is exceeded, trade operations are processed in the manual execution mode.

### Note

The method operates with individual symbol settings for the group.

# IMTConGroupSymbol::IEVolumeMaxExt

Sets the maximum volume (with extended accuracy) of a trade operation that can be executed in the instant execution mode.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::IEVolumeMaxExt(
       const UINT64  volume      // Maximum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.IEVolumeMaxExt(
       ulong         volume      // Maximum volume
       )

Python (Manager API)
    
    
    MTConGroupSymbol.IEVolumeMaxExt

### Program Parameters

**volume**  
[in] The maximum volume of a trade operation that can be executed in the instant execution mode, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots). In case this limit is exceeded, trade operations are processed in the manual execution mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method operates with individual symbol settings for the group.
