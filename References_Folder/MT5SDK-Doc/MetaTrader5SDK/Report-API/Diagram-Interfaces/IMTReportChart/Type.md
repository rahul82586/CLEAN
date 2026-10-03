[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / Type

[Previous](Title.md) | [Next](Digits.md)

# IMTReportChart::Type

Get a chart type.
    
    
    UINT  IMTReportChart::Type()  const

### Return Value

A value of the [IMTReportChart::EnChartType (#encharttype)](Enumerations.md#encharttype) enumeration.

# IMTReportChart::Type

Set a diagram type.
    
    
    MTAPIRES  IMTReportChart::Type(
       const UINT  type      // Type of a diagram
       )

### Parameters

**type**  
[in] Type of a diagram. To pass the options, theIMTReportChart::EnChartTypeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
