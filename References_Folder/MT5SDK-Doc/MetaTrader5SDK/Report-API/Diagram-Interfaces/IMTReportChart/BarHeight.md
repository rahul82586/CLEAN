[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / BarHeight

[Previous](Flags.md) | [Next](PieceTooltip.md)

# IMTReportChart::BarHeight

Get the chart bar height.
    
    
    UINT  IMTReportChart::BarHeight()  const

### Return Value

Chart bar height.

# IMTReportChart::BarHeight

Set the chart bar height.
    
    
    MTAPIRES  IMTReportChart::BarHeight(
       const UINT  height      // Height
       )

### Parameters

**height**  
[in] Chart bar height.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
