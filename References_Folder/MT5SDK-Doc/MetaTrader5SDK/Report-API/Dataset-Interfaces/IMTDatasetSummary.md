[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Dataset Interfaces](../Dataset-Interfaces.md) / IMTDatasetSummary

[Previous](IMTDatasetColumn/Size.md) | [Next](IMTDatasetSummary/Enumerations.md)

# IMTDatasetSummary

The IMTDatasetSummary interface is used for working with a table summary row. It contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDatasetSummary/Release.md) | Delete the current object.  
[Assign](IMTDatasetSummary/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDatasetSummary/Clear.md) | Clear an object.  
[ColumnID](IMTDatasetSummary/ColumnID.md) | Get and set the ID of the column, under which a summary is specified.  
[Line](IMTDatasetSummary/Line.md) | Get and set the number of the row, at which a summary cell is displayed.  
[MergeColumn](IMTDatasetSummary/MergeColumn.md) | Get and set the ID of the column, to which the joining of summary cells is performed.  
[Color](IMTDatasetSummary/Color.md) | Get and set a text color in a summary cell.  
[Flags](IMTDatasetSummary/Flags.md) | Get and set summary cell flags.  
[Type](IMTDatasetSummary/Type.md) | Get a data type in a summary cell.  
[Digits](IMTDatasetSummary/Digits.md) | Get and set the number of decimal places for formatting the value shown in a cell.  
[ValueInt](IMTDatasetSummary/ValueInt.md) | Get and set an integer cell value.  
[ValueUInt](IMTDatasetSummary/ValueUInt.md) | Get and set an unsigned integer cell value.  
[ValueDouble](IMTDatasetSummary/ValueDouble.md) | Get and set the value of a double type cell.  
[ValueMoney](IMTDatasetSummary/ValueMoney.md) | Get and set a summary cell monetary value.  
[ValueString](IMTDatasetSummary/ValueString.md) | Get and set a summary cell string value.  
[ValueDate](IMTDatasetSummary/ValueDate.md) | Get and set a summary cell value of the date type.  
[ValueTime](IMTDatasetSummary/ValueTime.md) | Get and set a summary cell value of the time type.  
[ValueDateTime](IMTDatasetSummary/ValueDateTime.md) | Get and set a summary cell value of the datetime type.  
[ValuePrice](IMTDatasetSummary/ValuePrice.md) | Get and set a summary cell price value.  
[ValuePricesBid](IMTDatasetSummary/ValuePricesBid.md) | Get a previously set Bid price value in a summary cell.  
[ValuePricesAsk](IMTDatasetSummary/ValuePricesAsk.md) | Get a previously set Ask price value in a summary cell.  
[ValuePrices](IMTDatasetSummary/ValuePrices.md) | Set Bid and Ask prices values in a summary cell.  
[ValueVolume](IMTDatasetSummary/ValueVolume.md) | Get and set a volume value in a summary cell.  
[ValueVolumeInitial](IMTDatasetSummary/ValueVolumeInitial.md) | Get a previously set initial volume value in a summary cell.  
[ValueVolumeCurrent](IMTDatasetSummary/ValueVolumeCurrent.md) | Get a previously set current (unexecuted) volume value in a summary cell.  
  
The IMTDatasetSummary interface contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnType (#entype)](IMTDatasetSummary/Enumerations.md#entype) | Types of values in a summary row.  
[EnFlags (#enflags)](IMTDatasetSummary/Enumerations.md#enflags) | Summary row flags.  
  
> In earlier MetaTrader 5 API versions, the IMTDatasetSummary interface was called IMTReportSummary.
