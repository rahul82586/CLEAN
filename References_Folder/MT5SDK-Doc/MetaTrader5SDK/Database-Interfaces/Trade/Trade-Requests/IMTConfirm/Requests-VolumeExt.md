[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests VolumeExt

[Previous](Requests-Volume.md) | [Next](Requests-Price.md)

# IMTConfirm::VolumeExt

Gets the extended accuracy volume in which the trade request was confirmed.

C++
    
    
    UINT64  IMTConfirm::VolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConfirm.VolumeExt()

### Return Value

The volume in which the trade request was confirmed, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConfirm::Volume](Requests-Volume.md) method.

# IMTConfirm::VolumeExt

Sets the extended accuracy volume in which the trade request was confirmed.

C++
    
    
    MTAPIRES  IMTConfirm::VolumeExt(
       const UINT64  volume      // Confirmation volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.VolumeExt(
       ulong         volume      // Confirmation volume
       )

### Program Parameters

**volume**  
[in] Trade request confirmation volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConfirm::Volume](Requests-Volume.md) method.
