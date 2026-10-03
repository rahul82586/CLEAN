[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / ColumnCreate

[Previous](Flags.md) | [Next](ColumnClear.md)

# IMTDataset::ColumnCreate

Create a column object.
    
    
    IMTDatasetColumn*  IMTDataset::ColumnCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTDatasetColumn](../IMTDatasetColumn.md) interface. In case of a failure, it returns NULL.

### Note

The created object should be destroyed by calling the [IMTDatasetColumn::Release](../IMTDatasetColumn/Release.md) method of this object.
