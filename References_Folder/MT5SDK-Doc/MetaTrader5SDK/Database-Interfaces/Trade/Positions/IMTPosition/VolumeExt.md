[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / VolumeExt

[Previous](Volume.md) | [Next](Profit.md)

# IMTPosition::VolumeExt

Gets the trade position volume with an extended accuracy.

C++
    
    
    UINT64  IMTPosition::VolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTPosition.VolumeExt()

### Return Value

The trade position volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTPosition::Volume](Volume.md) method.

# IMTPosition::VolumeExt

Sets the trade position volume with an extended accuracy.

C++
    
    
    MTAPIRES  IMTPosition::VolumeExt(
       const UINT64  volume      // Position volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.VolumeExt(
       ulong         volume      // Position volume
       )

### Program Parameters

**volume**  
[in] The trade position volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTPosition::Volume](Volume.md) method.
