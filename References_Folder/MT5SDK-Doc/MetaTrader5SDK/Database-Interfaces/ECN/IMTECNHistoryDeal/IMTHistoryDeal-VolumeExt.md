[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal VolumeExt

[Previous](IMTHistoryDeal-Action.md) | [Next](IMTHistoryDeal-Price.md)

# IMTECNHistoryDeal::VolumeExt

Get the volume of a deal.

C++
    
    
    UINT64  IMTECNHistoryDeal::VolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryDeal.VolumeExt()

### Return Value

Deal volume. The value is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

# IMTECNHistoryDeal::VolumeExt

Set the volume of a deal.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::VolumeExt(
       const UINT64  volume     // volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.VolumeExt(
       ulong         volume     // volume
       )

### Parameters

**volume**  
[in] Deal volume. The value is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
