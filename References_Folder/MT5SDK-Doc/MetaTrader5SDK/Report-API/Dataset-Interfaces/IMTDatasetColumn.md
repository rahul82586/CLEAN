[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Dataset Interfaces](../Dataset-Interfaces.md) / IMTDatasetColumn

[Previous](IMTDatasetRequest/FieldNext.md) | [Next](IMTDatasetColumn/Enumerations.md)

# IMTDatasetColumn

The IMTDatasetColumn interface is used for working with a table columns. It contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDatasetColumn/Release.md) | Delete the current object.  
[Assign](IMTDatasetColumn/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDatasetColumn/Clear.md) | Clear an object.  
[Name](IMTDatasetColumn/Name.md) | Get and set a column name shown in the manager terminal.  
[ColumnID](IMTDatasetColumn/ColumnID.md) | Get and set the column ID.  
[Type](IMTDatasetColumn/Type.md) | Get and set the column type.  
[Width](IMTDatasetColumn/Width.md) | Get and set the column relative width, while displaying in the manager terminal.  
[WidthMax](IMTDatasetColumn/WidthMax.md) | Get and set the maximum size of a column in pixels.  
[Digits](IMTDatasetColumn/Digits.md) | Get and set the number of decimal places by default for values in a column.  
[DigitsColumn](IMTDatasetColumn/DigitsColumn.md) | Get and set the ID of the column describing the number of decimal places, according to which the value in the current column must be formatted.  
[Flags](IMTDatasetColumn/Flags.md) | Get and set column flags.  
[Offset](IMTDatasetColumn/Offset.md) | Get and set the shift inside the one entry specifying the beginning of a column data.  
[Size](IMTDatasetColumn/Size.md) | Get and set the size of the column data in bytes.  
  
The IMTDatasetColumn interface contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnType (#entype)](IMTDatasetColumn/Enumerations.md#entype) | Types of values in a column.  
[EnFlags (#enflags)](IMTDatasetColumn/Enumerations.md#enflags) | Column display flags.  
  
> In earlier MetaTrader 5 API versions, the IMTDatasetColumn interface was called IMTReportColumn.
