[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / Title

[Previous](Clear.md) | [Next](Type.md)

# IMTReportChart::Title

Get a chart header.
    
    
    LPCWSTR  IMTReportChart::Title()  const

### Return Value

If successful, it returns a pointer to the string with the chart name. Otherwise, it returns NULL.

# IMTReportChart::Title

Set a chart header.
    
    
    MTAPIRES  IMTReportChart::Title(
       LPCWSTR  title      // Header
       )

### Parameters

**title**  
[in] Chart header.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum header length is 256 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
