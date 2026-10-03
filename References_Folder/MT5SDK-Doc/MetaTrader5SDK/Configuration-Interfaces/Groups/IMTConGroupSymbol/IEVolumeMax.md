[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / IEVolumeMax

[Previous](IESlipLosingDefault.md) | [Next](IEVolumeMaxExt.md)

# IMTConGroupSymbol::IEVolumeMax

Gets the maximum volume of a trade operation that can be executed in the instant execution mode.

C++
    
    
    UINT64  IMTConGroupSymbol::IEVolumeMax()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.IEVolumeMax()

Python (Manager API)
    
    
    MTConGroupSymbol.IEVolumeMax

### Return Value

The maximum volume of a trade operation that can be executed in the instant execution mode in the UINT64 format (one unit is equal to 1/10,000 of a lot). In case this limit is exceeded, trade operations are processed in the manual execution mode.

### Note

This method operates with individual symbol settings for groups.

# IMTConGroupSymbol::IEVolumeMax

Sets the maximum volume of a trade operation that can be executed in the instant execution mode.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::IEVolumeMax(
       const UINT64  volume      // Maximum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.IEVolumeMax(
       ulong         volume      // Maximum volume
       )

Python (Manager API)
    
    
    MTConGroupSymbol.IEVolumeMax

### Parameters

**volume**  
[in] The maximum volume of a trade operation that can be executed in the instant execution mode in the UINT64 format (one unit is equal to 1/10,000 of a lot). In case this limit is exceeded, trade operations are processed in the manual execution mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method operates with individual symbol settings for groups.
