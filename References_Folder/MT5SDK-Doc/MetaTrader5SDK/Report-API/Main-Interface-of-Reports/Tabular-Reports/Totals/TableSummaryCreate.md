[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Totals](../Totals.md) / TableSummaryCreate

[Previous](../Totals.md) | [Next](TableSummaryClear.md)

# IMTReportAPI::TableSummaryCreate

Create an object of a totals row cell.
    
    
    IMTDatasetSummary*  IMTReportAPI::TableSummaryCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTDatasetSummary](../../../Dataset-Interfaces/IMTDatasetSummary.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTDatasetSummary::Release](../../../Dataset-Interfaces/IMTDatasetSummary/Release.md) method of this object.
