[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportSeries](../IMTReportSeries.md) / Title

[Previous](Clear.md) | [Next](Type.md)

# IMTReportSeries::Title

Get a data series header.
    
    
    LPCWSTR  IMTReportSeries::Title()  const

### Return Value

If successful, it returns a pointer to the string with the series name. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTReportSeries](../IMTReportSeries.md) object.

# IMTReportSeries::Title

Set data series header.
    
    
    MTAPIRES  IMTReportSeries::Title(
       LPCWSTR  title      // Header
       )

### Parameters

**title**  
[in] Data series header.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum header length is 1024 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
