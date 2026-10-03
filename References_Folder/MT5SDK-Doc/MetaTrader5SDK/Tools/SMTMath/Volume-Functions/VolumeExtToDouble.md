[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Volume Functions](../Volume-Functions.md) / VolumeExtToDouble

[Previous](VolumeToDouble.md) | [Next](VolumeToSize.md)

# SMTMath::VolumeExtToDouble

Converting the increased accuracy volume from int to double.

C++
    
    
    static double  SMTMath::VolumeExtToDouble(
       const UINT64  volume      // Input volume
       )

.NET (Gateway/Manager API)
    
    
    static double  SMTMath.VolumeExtToDouble(
       ulong         volume      // Input volume
       )

### Program Parameters

**volume**  
[in] Input volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

The resulting volume in lots.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [SMTMath::VolumeToDouble](VolumeToDouble.md) method.
