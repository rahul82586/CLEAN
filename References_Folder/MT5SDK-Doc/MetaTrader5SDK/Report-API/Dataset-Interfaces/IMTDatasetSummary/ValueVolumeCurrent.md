[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / ValueVolumeCurrent

[Previous](ValueVolumeInitial.md) | [Next](../../Data-Cache-Interfaces.md)

# IMTDatasetSummary::ValueVolumeCurrent

Get a previously set current (unexecuted) volume value in a summary cell.
    
    
    UINT64  IMTDatasetSummary::ValueVolumeCurrent()  const

### Return Value

A previously set current (unexecuted) volume value in a summary cell. Volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

A received summary must be of [IMTDatasetSummary::TYPE_VOLUME_ORDER (#entype)](Enumerations.md#entype) type. Otherwise, the method returns 0.
