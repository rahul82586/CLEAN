[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / VolumeClosed

[Previous](VolumeExt.md) | [Next](VolumeClosedExt.md)

# IMTDeal::VolumeClosed

Gets the position volume that was closed by the deal.

C++
    
    
    UINT64  IMTDeal::VolumeClosed()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.VolumeClosed()

### Return Value

The position volume that was closed by the deal. The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The value can be obtained only for the deals of type [IMTDeal::ENTRY_OUT (#endealentry)](Enumerations.md#endealentry)[IMTDeal::ENTRY_INOUT (#endealentry)](Enumerations.md#endealentry)

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTDeal::VolumeClosedExt](VolumeClosedExt.md) method.

# IMTDeal::VolumeClosed

Sets the position volume that was closed by the deal.

C++
    
    
    MTAPIRES  IMTDeal::VolumeClosed(
       const UINT64  volume      // Closed volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.VolumeClosed(
       ulong         volume      // Closed volume
       )

### Parameters

**volume**  
[in] The position volume that was closed by the deal. The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The value can be set only for the deals of type [IMTDeal::ENTRY_OUT (#endealentry)](Enumerations.md#endealentry)[IMTDeal::ENTRY_INOUT (#endealentry)](Enumerations.md#endealentry)

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTDeal::VolumeClosedExt](VolumeClosedExt.md) method.
