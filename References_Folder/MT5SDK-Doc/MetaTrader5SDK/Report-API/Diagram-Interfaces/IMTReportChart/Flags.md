[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / Flags

[Previous](Digits.md) | [Next](BarHeight.md)

# IMTReportChart::Flags

Get chart flags.
    
    
    UINT64  IMTReportChart::Flags()  const

### Return Value

A value of the [IMTReportChart::EnChartFlags (#enchartflags)](Enumerations.md#enchartflags) enumeration.

# IMTReportChart::Flags

Set chart flags.
    
    
    MTAPIRES  IMTReportChart::Flags(
       const UINT64  flags      // flags
       )

### Parameters

**flags**  
[in] Chart flags. To pass the options, theIMTReportChart::EnChartFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
