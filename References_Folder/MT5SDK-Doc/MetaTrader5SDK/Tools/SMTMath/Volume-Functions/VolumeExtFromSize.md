[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Volume Functions](../Volume-Functions.md) / VolumeExtFromSize

[Previous](VolumeFromSize.md) | [Next](../Functions-of-Monetary-Units.md)

# SMTMath::VolumeFromSize

Obtaining extended accuracy volume in lots from the volume specified as amount.

C++
    
    
    static UINT64  SMTMath::VolumeFromSize(
       const double  size,              // Input volume
       double        contract_size      // Contract size
       )

.NET (Gateway/Manager API)
    
    
    static ulong  SMTMath.VolumeFromSize(
       double        size,              // Input volume
       double        contract_size      // Contract size
       )

### Program Parameters

**size**  
[in] Input volume as amount.

**contract_size**  
[in] Contract size.

### Return Value

Volume in the UINT64 format (one unit corresponds to 1/ lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [SMTMath::VolumeFromSize](VolumeFromSize.md) method.
