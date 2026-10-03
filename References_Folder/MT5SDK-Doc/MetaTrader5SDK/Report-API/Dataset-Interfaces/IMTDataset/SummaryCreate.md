[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / SummaryCreate

[Previous](RowTotal.md) | [Next](SummaryClear.md)

# IMTDataset::SummaryCreate

Create an object of a totals row cell.
    
    
    IMTDatasetSummary*  IMTDataset::SummaryCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTDatasetSummary](../IMTDatasetSummary.md) interface. In case of failure, it returns NULL.

### Note

The created object should be destroyed by calling the [IMTDatasetSummary::Release](../IMTDatasetSummary/Release.md) method of this object.
