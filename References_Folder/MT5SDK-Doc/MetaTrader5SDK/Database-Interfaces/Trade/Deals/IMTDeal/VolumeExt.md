[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / VolumeExt

[Previous](Volume.md) | [Next](VolumeClosed.md)

# IMTDeal::VolumeExt

Gets the deal volume with an extended accuracy.

C++
    
    
    UINT64  IMTDeal::VolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.VolumeExt()

### Return Value

Deal volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTDeal::Volume](Volume.md) method.

# IMTDeal::VolumeExt

Sets the deal volume with an extended accuracy.

C++
    
    
    MTAPIRES  IMTDeal::VolumeExt(
       const UINT64  volume      // Deal volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.VolumeExt(
       ulong         volume      // Deal volume
       )

### Program Parameters

**volume**  
[in] Deal volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTDeal::Volume](Volume.md) method.
