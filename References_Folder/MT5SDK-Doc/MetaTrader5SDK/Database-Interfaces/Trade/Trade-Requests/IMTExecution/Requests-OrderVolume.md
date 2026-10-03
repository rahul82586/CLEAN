[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderVolume

[Previous](Requests-OrderType.md) | [Next](Requests-OrderVolumeExt.md)

# IMTExecution::OrderVolume

Gets the order volume in lots.

C++
    
    
    UINT64  IMTExecution::OrderVolume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.OrderVolume()

### Return Value

Order volume in the UINT64 format (one unit corresponds to 1/10000 of the lot).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTExecution::OrderVolumeExt](Requests-OrderVolumeExt.md) method.

# IMTExecution::OrderVolume

Sets the order volume in lots.

C++
    
    
    MTAPIRES  IMTExecution::OrderVolume(
       const UINT64  volume      // Order volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderVolume(
       ulong         volume      // Order volume
       )

### Parameters

**volume**  
[in] Order volume in the UINT64 format (one unit corresponds to 1/10000 of the lot).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTExecution::OrderVolumeExt](Requests-OrderVolumeExt.md) method.
