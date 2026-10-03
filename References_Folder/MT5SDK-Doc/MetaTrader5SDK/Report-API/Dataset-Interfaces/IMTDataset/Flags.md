[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / Flags

[Previous](Clear.md) | [Next](ColumnCreate.md)

# IMTDatasetSummary::Flags

Get the flags of a dashboard data set.
    
    
    UINT64  IMTDatasetSummary::Flags()  const

### Return Value

[IMTDataset::EnDataSetFlags (#endatasetflags)](Enumerations.md#endatasetflags) enumeration value.

### Note

The method is reserved for future use.

# IMTDatasetSummary::Flags

Set the flags of a dashboard data set.
    
    
    MTAPIRES  IMTDatasetSummary::Flags(
       const UINT64  flags      // flags
       )

### Parameters

**flags**  
[in] Data set flags. TheIMTDataset::EnDataSetFlagsenumeration is used to pass them.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is reserved for future use.
