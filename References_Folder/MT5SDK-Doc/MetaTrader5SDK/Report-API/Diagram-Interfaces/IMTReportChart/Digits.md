[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / Digits

[Previous](Type.md) | [Next](Flags.md)

# IMTReportChart::Digits

Get the number of decimal places for formatting the values shown in a chart.
    
    
    UINT  IMTReportChart::Digits()  const

### Return Value

The number of decimal places for formatting the values shown in a chart.

# IMTReportChart::Digits

Set the number of decimal places for formatting the values shown in a chart.
    
    
    MTAPIRES  IMTReportChart::Digits(
       const UINT  digits      // Decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places for formatting the values shown in a chart.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
