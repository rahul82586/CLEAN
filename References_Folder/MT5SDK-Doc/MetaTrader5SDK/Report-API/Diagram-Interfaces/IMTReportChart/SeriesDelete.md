[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / SeriesDelete

[Previous](SeriesAddCopy.md) | [Next](SeriesDetach.md)

# IMTReportChart::SeriesDelete

Delete an object of a data series by its position.
    
    
    MTAPIRES  IMTReportChart::SeriesDelete(
       const UINT  pos      // Series position
       )

### Parameters

**pos**  
[in] Position of a data series, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The object to delete will be automatically released by calling the [IMTReportSeries::Release](../IMTReportSeries/Release.md) method.
