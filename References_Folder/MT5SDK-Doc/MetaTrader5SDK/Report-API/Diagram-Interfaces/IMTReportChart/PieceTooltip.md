[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / PieceTooltip

[Previous](BarHeight.md) | [Next](PieceDescription.md)

# IMTReportChart::PieceTooltip

Get a pie chart element tooltip.
    
    
    LPCWSTR  IMTReportChart::PieceTooltip()

### Return Value

If successful, it returns a pointer to the string with a tooltip. Otherwise, it returns NULL.

# IMTReportChart::PieceTooltip

Set a pie chart element tooltip.
    
    
    MTAPIRES  IMTReportChart::PieceTooltip(
       LPCWSTR  tooltip      // Tooltip
       )

### Parameters

**tooltip**  
[in] Toltip.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum tooltip length is 256 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.

  * %VARIABLE% — inserts a pie chart element value specified in a header series (series of the [IMTReportSeries::TYPE_TITLE (#enseriestype)](../IMTReportSeries/Enumerations.md#enseriestype)) type.
  * %VALUE% — inserts a point absolute value (the value specified for a series point using [IMTReportSeries::ValueAdd*](../IMTReportSeries/ValueAdd.md) methods).
  * %PERCENT_VALUE% — inserts the value of a percentage ratio of a pie chart element value to the whole chart.
  * %DESCRIPTION% — inserts a value of the point specified using the [IMTReportSeries::ValueDescription](../IMTReportSeries/ValueDescription.md) method.
  * <BR> — inserts a line folding.


