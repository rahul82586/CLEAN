[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Volume Functions](../Volume-Functions.md) / VolumeExtToSize

[Previous](VolumeToSize.md) | [Next](VolumeFromSize.md)

# SMTMath::VolumeToSize

Converting the increased accuracy volume from lots to amount.

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

### Program Parameters

**volume**  
[in] Input volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

**contract_size**  
[in] Contract size.

### Return Value

Volume as amount (lots * contract size).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [SMTMath::VolumeToSize](VolumeToSize.md) method.
