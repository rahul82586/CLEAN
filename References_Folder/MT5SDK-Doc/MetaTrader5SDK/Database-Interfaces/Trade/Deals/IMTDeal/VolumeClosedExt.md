[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / VolumeClosedExt

[Previous](VolumeClosed.md) | [Next](Profit.md)

# IMTDeal::VolumeClosedExt

Gets the extended accuracy volume of a position that was closed by this deal.

C++
    
    
    UINT64  IMTDeal::VolumeClosedExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.VolumeClosedExt()

### Return Value

The position volume that was closed by the deal. The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The value can only be obtained for deal type [IMTDeal::ENTRY_OUT (#endealentry)](Enumerations.md#endealentry)[IMTDeal::ENTRY_INOUT (#endealentry)](Enumerations.md#endealentry)

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTDeal::VolumeClosed](VolumeClosed.md) method.

# IMTDeal::VolumeClosedExt

Sets the extended accuracy volume of a position that was closed by this deal.

C++
    
    
    MTAPIRES  IMTDeal::VolumeClosedExt(
       const UINT64  volume      // Closed volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.VolumeClosedExt(
       ulong         volume      // Closed volume
       )

### Program Parameters

**volume**  
[in] The position volume that was closed by the deal. The volume is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The value can only be set for deal type [IMTDeal::ENTRY_OUT (#endealentry)](Enumerations.md#endealentry)[IMTDeal::ENTRY_INOUT (#endealentry)](Enumerations.md#endealentry)

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTDeal::VolumeClosed](VolumeClosed.md) method.
