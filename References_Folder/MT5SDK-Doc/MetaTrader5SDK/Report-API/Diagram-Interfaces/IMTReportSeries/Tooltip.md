[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / Tooltip

[Previous](Color.md) | [Next](ValueClear.md)

# IMTReportSeries::Tooltip

Get a text of a tooltip that is displayed when pointing the mouse cursor over a series.
    
    
    LPCWSTR  IMTReportSeries::Tooltip()  const

### Return Value

If successful, it returns a pointer to the string with a tooltip text. Otherwise, it returns NULL.

# IMTReportSeries::Tooltip

Set a text of a tooltip that will be displayed when pointing the mouse cursor over a series.
    
    
    MTAPIRES  IMTReportSeries::Tooltip(
       LPCWSTR  tooltip      // Tooltip
       )

### Parameters

**tooltip**  
[in] Series tooltip.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum tooltip length is 1024 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.

  * %VARIABLE% — inserts the value of the point from a header series (the series of the [IMTReportSeries::TYPE_TITLE (#enseriestype)](Enumerations.md#enseriestype) type is usually displayed as X axis tooltip).
  * %VALUE% — inserts a point absolute value (the value specified for a series point using [IMTReportSeries::ValueAdd*](ValueAdd.md) methods).
  * %NORMALIZED_VALUE% — inserts a point normalized value. It is calculated as a percentage ratio of the point absolute value to the sum of the values of all points that correspond the same header series value.
  * %DESCRIPTION% — inserts a value of the point specified using the [IMTReportSeries::ValueDescription](ValueDescription.md) method.
  * %TITLE% — inserts a series header value specified using the [IMTReportSeries::Title](Title.md) method.
  * <BR> — inserts a line folding.


