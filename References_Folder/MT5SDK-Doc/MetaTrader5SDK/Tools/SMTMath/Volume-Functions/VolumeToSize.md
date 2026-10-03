[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Volume Functions](../Volume-Functions.md) / VolumeToSize

[Previous](VolumeExtToDouble.md) | [Next](VolumeExtToSize.md)

# SMTMath::VolumeToSize

Converting the volume from lots to amount.

C++
    
    
    static double  SMTMath::VolumeToSize(
       const UINT64  volume,            // Input volume
       double        contract_size      // Contract size
       )

.NET (Gateway/Manager API)
    
    
    static double  SMTMath.VolumeToSize(
       ulong         volume,            // Input volume
       double        contract_size      // Contract size
       )

### Parameters

**volume**  
[in] Input volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

**contract_size**  
[in] Contract size.

### Return Value

Volume as amount (lots * contract size).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [SMTMath::VolumeExtToSize](VolumeExtToSize.md) method.
