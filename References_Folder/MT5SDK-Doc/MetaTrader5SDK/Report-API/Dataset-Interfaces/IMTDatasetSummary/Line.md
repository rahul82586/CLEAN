[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetSummary](../IMTDatasetSummary.md) / Line

[Previous](ColumnID.md) | [Next](MergeColumn.md)

# IMTDatasetSummary::Line

Get the number of the row, at which a summary cell is displayed.
    
    
    UINT  IMTDatasetSummary::Line()  const

### Return Value

The number of the row, at which a summary cell is displayed.

### Note

The number is specified with reference to a table end (0 means that a summary is displayed right after the table's last entry, 1 - over a row after the last entry etc.).

# IMTDatasetSummary::Line

Set the number of the row, at which a summary cell is displayed.
    
    
    MTAPIRES  IMTDatasetSummary::Line(
       const UINT  line      // Number of a row
       )

### Parameters

**line**  
[in] The number of the row, at which a summary cell is displayed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The number is specified with reference to a table end (0 means that a summary is displayed right after the table's last entry, 1 - over a row after the last entry etc.).
