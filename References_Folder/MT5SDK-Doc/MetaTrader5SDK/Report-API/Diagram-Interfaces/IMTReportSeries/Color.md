[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / Color

[Previous](Flags.md) | [Next](Tooltip.md)

# IMTReportSeries::Color

Get the color used for a data series display on a chart.
    
    
    UINT  IMTReportSeries::Color()  const

### Return Value

The color used for a data series display on a chart.

# IMTReportSeries::Color

Set the color that will be used for a data series display on a chart.
    
    
    MTAPIRES  IMTReportSeries::Color(
       const UINT  color      // Color
       )

### Parameters

**color**  
[in] Data series display color.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
