[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / ValueDescription

[Previous](ValueDelete.md) | [Next](../IMTReportChart.md)

# IMTReportSeries::ValueDescription

Get a description for a series value.
    
    
    LPCWSTR  IMTReportSeries::ValueDescription(
       const UINT  pos      // Position
       )  const

### Parameters

**pos**  
[in] Position of a series value, description of which must be received, starting with 0.

### Return Value

If successful, it returns a pointer to the string with a description text. Otherwise, it returns NULL.

### Note

Description is displayed in a tooltip to a series value when pointing the mouse cursor over it.

# IMTReportSeries::ValueDescription

Set a description for a series value.
    
    
    MTAPIRES  IMTReportSeries::ValueDescription(
       const UINT  pos,       // Position
       LPCWSTR     descr      // Description text
       )

### Parameters

**pos**  
[in] Position of a series value that must be complemented by the description, starting with 0. Indicate position of the already existing value.

**descr**  
[in] Description text.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Description is displayed in a tooltip to a series value when pointing the mouse cursor over it.
