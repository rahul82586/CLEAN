[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / Flags

[Previous](Type.md) | [Next](Color.md)

# IMTReportSeries::Flags

Get data series flags.
    
    
    UINT64  IMTReportSeries::Flags()  const

### Return Value

A value of the [IMTReportSeries::EnSeriesFlags (#enseriesflags)](Enumerations.md#enseriesflags) enumeration.

# IMTReportSeries::Flags

Set data series flags.
    
    
    MTAPIRES  IMTReportSeries::Flags(
       const UINT64  flags      // series flags
       )

### Parameters

**flags**  
[in] Data series flags. To set the options, theIMTReportSeries::EnSeriesFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
