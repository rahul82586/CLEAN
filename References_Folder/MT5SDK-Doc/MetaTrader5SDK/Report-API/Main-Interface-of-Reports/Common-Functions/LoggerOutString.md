[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Common Functions](../Common-Functions.md) / LoggerOutString

[Previous](LoggerOut.md) | [Next](IsStopeed.md)

# IMTReportAPI::LoggerOutString

Quick output of unformatted stings to the journal.
    
    
    MTAPIRES  IMTReportAPI::LoggerOutString(
       const UINT  code,     // log code
       LPCWSTR     string   // log string
       )

### Parameters

**code**  
[in] Log code which is passed using theEnMTLogCodeenumerations.

**string**  
[in] Log string with optional arguments.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Compared to [IMTReportAPI::LoggerOut](LoggerOut.md), which formats the output, this method uses less resources.
