[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Volume Functions](../Volume-Functions.md) / VolumeToDouble

[Previous](VolumeExtToInt.md) | [Next](VolumeExtToDouble.md)

# SMTMath::VolumeToDouble

Converting a volume from int to double.

C++
    
    
    static double  SMTMath::VolumeToDouble(
       const UINT64  volume      // Input volume
       )

.NET (Gateway/Manager API)
    
    
    static double  SMTMath.VolumeToDouble(
       ulong         volume      // Input volume
       )

### Parameters

**volume**  
[in] Input volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

Resulting volume in lots.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [SMTMath::VolumeExtToDouble](VolumeToDouble.md) method.
