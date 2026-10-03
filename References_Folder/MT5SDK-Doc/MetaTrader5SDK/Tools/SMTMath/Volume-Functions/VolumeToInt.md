[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Volume Functions](../Volume-Functions.md) / VolumeToInt

[Previous](../Volume-Functions.md) | [Next](VolumeExtToInt.md)

# SMTMath::VolumeToInt

Converting a volume from double to int.

C++
    
    
    static UINT64  SMTMath::VolumeToInt(
       const double  volume      // Input volume
       )

.NET (Gateway/Manager API)
    
    
    static ulong  SMTMath.VolumeToInt(
       double        volume      // Input volume
       )

### Parameters

**volume**  
[in] The input volume in lots.

### Return Value

Resulting volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [SMTMath::VolumeExtToInt](VolumeExtToInt.md) method.
