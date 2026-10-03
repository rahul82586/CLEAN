[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamVolumeExt

[Previous](ParamVolume.md) | [Next](ParamDatetime.md)

# IMTConRoute::ParamVolumeExt

Gets the value of an additional parameter that expresses the volume with extended accuracy.

C++
    
    
    UINT64  IMTConRoute::ParamVolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConRoute.ParamVolumeExt()

Python (Manager API)
    
    
    MTConRoute.ParamVolumeExt

### Return Value

Value in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConRoute::ParamVolume](ParamVolume.md) method.

# IMTConRoute::ParamVolumeExt

Sets the value of an additional parameter that expresses the volume with extended accuracy.

C++
    
    
    MTAPIRES  IMTConRoute::ParamVolumeExt(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamVolumeExt(
       ulong         value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamVolumeExt

### Program Parameters

**value**  
[in] Value in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConRoute::ParamVolume](ParamVolume.md) method.
