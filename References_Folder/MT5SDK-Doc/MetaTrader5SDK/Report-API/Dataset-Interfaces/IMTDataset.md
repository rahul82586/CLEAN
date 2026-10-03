[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Dataset Interfaces](../Dataset-Interfaces.md) / IMTDataset

[Previous](../Dataset-Interfaces.md) | [Next](IMTDataset/Enumerations.md)

# IMTDataset

The IMTDataset interface is designed to work with dashboard data: columns, rows and final values. These data can be displayed in the widget as a graph and/or a table. It contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDataset/Release.md) | Delete the current object.  
[Assign](IMTDataset/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDataset/Clear.md) | Clear an object.  
[Flags](IMTDataset/Flags.md) | Get and set data set flags.  
[ColumnCreate](IMTDataset/ColumnCreate.md) | Create a column object.  
[ColumnClear](IMTDataset/ColumnClear.md) | Clear table columns description.  
[ColumnAdd](IMTDataset/ColumnAdd.md) | Add a column description to a table end.  
[ColumnDelete](IMTDataset/ColumnDelete.md) | Delete a column description from a table by index.  
[ColumnTotal](IMTDataset/ColumnTotal.md) | Get a number of columns in a table.  
[ColumnSize](IMTDataset/ColumnSize.md) | Get a total size of one table row in bytes.  
[ColumnNext](IMTDataset/ColumnNext.md) | Get a column description by index.  
[RowClear](IMTDataset/RowClear.md) | Delete the contents of a whole table.  
[RowWrite](IMTDataset/RowWrite.md) | Add (output) one record to a table.  
[RowTotal](IMTDataset/RowTotal.md) | Get the number of rows in a table.  
[SummaryCreate](IMTDataset/SummaryCreate.md) | Create an object of a totals row cell.  
[SummaryClear](IMTDataset/SummaryClear.md) | Clear all total records.  
[SummaryAdd](IMTDataset/SummaryAdd.md) | Add a totals row cell into a table.  
[SummaryDelete](IMTDataset/SummaryDelete.md) | Delete a cell in a table totals row by its index.  
[SummaryNext](IMTDataset/SummaryNext.md) | Get the cells of a table totals row by its index.  
[SummaryTotal](IMTDataset/SummaryTotal.md) | Get the total amount of totals cells in a table.  
  
The IMTDataset interface contains the following enumerations:

Interface | Purpose  
---|---  
[EnDataSetFlags (#endatasetflags)](IMTDataset/Enumerations.md#endatasetflags) | Data set flags.  
  
> In earlier MetaTrader 5 API versions, the IMTDataset interface was called IMTReportDashboardData.
