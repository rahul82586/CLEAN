[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealVolumeRemaind

[Previous](Requests-DealVolumeExt.md) | [Next](Requests-DealVolumeRemaindExt.md)

# IMTExecution::DealVolumeRemaind

Gets the remaining (not filled) volume in the order.

C++
    
    
    UINT64  IMTExecution::DealVolumeRemaind()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.DealVolumeRemaind()

### Return Value

The remaining (not filled) volume of the order in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTExecution::DealVolumeRemaindExt](Requests-DealVolumeRemaindExt.md) method.

# IMTExecution::DealVolumeRemaind

Sets the remaining (not filled) volume in the order.

C++
    
    
    MTAPIRES  IMTExecution::DealVolumeRemaind(
       const UINT64  volume      // Remaining volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealVolumeRemaind(
       ulong         volume      // Remaining volume
       )

### Parameters

**volume**  
[in] The remaining (not filled) volume of the order in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTExecution::DealVolumeRemaindExt](Requests-DealVolumeRemaindExt.md) method.
