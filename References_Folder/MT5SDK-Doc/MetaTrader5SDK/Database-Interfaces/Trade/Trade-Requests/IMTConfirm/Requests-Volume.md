[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Volume

[Previous](Requests-Retcode.md) | [Next](Requests-VolumeExt.md)

# IMTConfirm::Volume

Gets the volume in which the trade request was confirmed.

C++
    
    
    UINT64  IMTConfirm::Volume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConfirm.Volume()

### Return Value

The volume in which the trade request was confirmed. Volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConfirm::VolumeExt](Requests-VolumeExt.md) method.

# IMTConfirm::Volume

Sets the volume in which the trade request was confirmed.

C++
    
    
    MTAPIRES  IMTConfirm::Volume(
       const UINT64  volume      // Confirmation volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.Volume(
       ulong         volume      // Confirmation volume
       )

### Parameters

**volume**  
[in] The volume in which the trade request was confirmed. Volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConfirm::VolumeExt](Requests-VolumeExt.md) method.
