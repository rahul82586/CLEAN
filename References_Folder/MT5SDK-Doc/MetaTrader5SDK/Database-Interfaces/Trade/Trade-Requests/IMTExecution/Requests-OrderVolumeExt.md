[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderVolumeExt

[Previous](Requests-OrderVolume.md) | [Next](Requests-OrderPrice.md)

# IMTExecution::OrderVolumeExt

Gets the order volume in lots with an extended accuracy.

C++
    
    
    UINT64  IMTExecution::OrderVolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.OrderVolumeExt()

### Return Value

Order volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTExecution::OrderVolume](Requests-OrderVolume.md) method.

# IMTExecution::OrderVolumeExt

Sets the order volume with an extended accuracy.

C++
    
    
    MTAPIRES  IMTExecution::OrderVolumeExt(
       const UINT64  volume      // Order volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderVolumeExt(
       ulong         volume      // Order volume
       )

### Program Parameters

**volume**  
[in] Order volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTExecution::OrderVolume](Requests-OrderVolume.md) method.
