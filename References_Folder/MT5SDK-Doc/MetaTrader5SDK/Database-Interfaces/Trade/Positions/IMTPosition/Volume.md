[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Volume

[Previous](PriceTP.md) | [Next](VolumeExt.md)

# IMTPosition::Volume

Gets the volume of a trade position.

C++
    
    
    UINT64  IMTPosition::Volume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTPosition.Volume()

### Return Value

The volume of a position in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTPosition::VolumeExt](VolumeExt.md) method.

# IMTPosition::Volume

Sets the volume of a trade position.

C++
    
    
    MTAPIRES  IMTPosition::Volume(
       const UINT64  volume      // Position volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Volume(
       ulong         volume      // Position volume
       )

### Parameters

**volume**  
[in] The volume of a position in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTPosition::VolumeExt](VolumeExt.md) method.
