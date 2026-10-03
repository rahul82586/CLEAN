[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / SeriesShift

[Previous](SeriesUpdate.md) | [Next](SeriesTotal.md)

# IMTReportChart::SeriesShift

Change the position of a [data series](../IMTReportSeries.md) in a chart.
    
    
    MTAPIRES  IMTReportChart::SeriesShift(
       const UINT  pos,       // Series position
       const int   shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a data series, starting with 0

**shift**  
[in] Shift of a series relative to its current position. A negative value means the shift to the top, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
