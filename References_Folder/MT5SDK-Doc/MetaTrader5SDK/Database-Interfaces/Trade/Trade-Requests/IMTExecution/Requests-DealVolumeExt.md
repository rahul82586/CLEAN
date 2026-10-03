[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealVolumeExt

[Previous](Requests-DealVolume.md) | [Next](Requests-DealVolumeRemaind.md)

# IMTExecution::DealVolumeExt

Gets the deal volume in lots with an extended accuracy.

C++
    
    
    UINT64  IMTExecution::DealVolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.DealVolumeExt()

### Return Value

Deal volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTExecution::DealVolume](Requests-DealVolume.md) method.

# IMTExecution::DealVolumeExt

Sets the deal volume in lots with an extended accuracy.

C++
    
    
    MTAPIRES  IMTExecution::DealVolumeExt(
       const UINT64  volume      // Deal volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealVolumeExt(
       ulong         volume      // Deal volume
       )

### Program Parameters

**volume**  
[in] Deal volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTExecution::DealVolume](Requests-DealVolume.md) method.
