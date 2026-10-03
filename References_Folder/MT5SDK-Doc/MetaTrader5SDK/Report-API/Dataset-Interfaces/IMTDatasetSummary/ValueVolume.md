[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueVolume

[Previous](ValuePrices.md) | [Next](ValueVolumeInitial.md)

# IMTDatasetSummary::ValueVolume

Get a previously set volume value in a summary cell.
    
    
    UINT64  IMTDatasetSummary::ValueVolume()  const

### Return Value

A previously set volume value in a summary cell. Volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

A received summary must be of [IMTDatasetSummary::TYPE_VOLUME (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.

# IMTDatasetSummary::ValueVolume

Set a volume value in a summary cell.
    
    
    MTAPIRES  IMTDatasetSummary::ValueVolume(
       const UINT64  value      // Value
       )

### Parameters

**value**  
[in] Summary cell volume value. Volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_VOLUME (#entype)](Enumerations.md#entype).

# IMTDatasetSummary::ValueVolume

Set initial and current (unexecuted) volume values in a summary cell.
    
    
    MTAPIRES  IMTDatasetSummary::ValueVolume(
       const UINT64  value_initial,     // Initial volume
       const UINT64  value_current      // Current volume
       )

### Parameters

**value_initial**  
[in] Initial value in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

**value_current**  
[in] Current (unexecuted) volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After the method is called summary cell type changes for [IMTDatasetSummary::TYPE_VOLUME_ORDER (#entype)](Enumerations.md#entype).
