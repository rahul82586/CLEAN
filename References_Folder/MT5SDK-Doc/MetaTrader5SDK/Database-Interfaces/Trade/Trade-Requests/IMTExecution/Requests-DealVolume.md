[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealVolume

[Previous](Requests-DealAction.md) | [Next](Requests-DealVolumeExt.md)

# IMTExecution::DealVolume

Gets the deal volume in lots.

C++
    
    
    UINT64  IMTExecution::DealVolume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.DealVolume()

### Return Value

The deal volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTExecution::DealVolumeExt](Requests-DealVolumeExt.md) method.

# IMTExecution::DealVolume

Sets the deal volume in lots.

C++
    
    
    MTAPIRES  IMTExecution::DealVolume(
       const UINT64  volume      // Deal volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealVolume(
       ulong         volume      // Deal volume
       )

### Parameters

**volume**  
[in] The deal volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTExecution::DealVolumeExt](Requests-DealVolumeExt.md) method.
