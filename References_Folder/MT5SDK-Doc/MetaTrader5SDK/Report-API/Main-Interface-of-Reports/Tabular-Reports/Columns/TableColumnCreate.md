[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Tabular Reports](../../Tabular-Reports.md) / [Columns](../Columns.md) / TableColumnCreate

[Previous](../Columns.md) | [Next](TableColumnClear.md)

# IMTReportAPI::TableColumnCreate

A column object creation.
    
    
    IMTDatasetColumn*  IMTReportAPI::TableColumnCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTDatasetColumn](../../../Dataset-Interfaces/IMTDatasetColumn.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTDatasetColumn::Release](../../../Dataset-Interfaces/IMTDatasetColumn/Release.md) method of this object.
