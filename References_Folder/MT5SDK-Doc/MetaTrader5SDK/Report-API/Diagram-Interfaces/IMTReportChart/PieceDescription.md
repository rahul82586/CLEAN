[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Diagram Interfaces](../../Diagram-Interfaces.md) / [IMTReportChart](../IMTReportChart.md) / PieceDescription

[Previous](PieceTooltip.md) | [Next](SeriesClear.md)

# IMTReportChart::PieceDescription

Get the description of the pie chart element.
    
    
    LPCWSTR  IMTReportChart::PieceDescription()

### Return Value

If successful, it returns a pointer to the string with the description. Otherwise, it returns NULL.

# IMTReportChart::PieceDescription

Set the description of the pie chart element.
    
    
    MTAPIRES  IMTReportChart::PieceDescription(
       LPCWSTR  description      // Description
       )

### Parameters

**description**  
[in] Description of the pie chart element.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum description length is 256 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
