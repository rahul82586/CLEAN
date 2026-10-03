[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / Type

[Previous](Title.md) | [Next](Flags.md)

# IMTReportSeries::Type

Get a data series type.
    
    
    UINT  IMTReportSeries::Type()  const

### Return Value

A value of the [IMTReportSeries::EnSeriesType (#enseriestype)](Enumerations.md#enseriestype) enumeration.

# IMTReportSeries::Type

Set data series type.
    
    
    MTAPIRES  IMTReportSeries::Type(
       const UINT  type      // Series type
       )

### Parameters

**type**  
[in] Data series type. To set the options, theIMTReportSeries::EnSeriesTypeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
