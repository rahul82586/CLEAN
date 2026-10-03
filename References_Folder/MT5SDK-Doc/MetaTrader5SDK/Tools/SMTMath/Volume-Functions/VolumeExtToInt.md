[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Volume Functions](../Volume-Functions.md) / VolumeExtToInt

[Previous](VolumeToInt.md) | [Next](VolumeToDouble.md)

# SMTMath::VolumeExtToInt

Converting the increased accuracy volume from double to int.

C++
    
    
    static UINT64  SMTMath::VolumeExtToInt(
       const double  volume      // Input volume
       )

.NET (Gateway/Manager API)
    
    
    static ulong  SMTMath.VolumeExtToInt(
       double        volume      // Input volume
       )

### Program Parameters

**volume**  
[in] The input volume in lots.

### Return Value

Resulting volume in the UINT64 format (one unit corresponds to 1/ lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [SMTMath::VolumeToInt](VolumeToInt.md) method.
