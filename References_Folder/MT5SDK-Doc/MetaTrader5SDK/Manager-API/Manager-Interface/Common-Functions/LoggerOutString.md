[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Common Functions](../Common-Functions.md) / LoggerOutString

[Previous](LoggerOut.md) | [Next](LoggerFlush.md)

# IMTManagerAPI::LoggerOutString

Fast output method which prints unformatted logs to the Manager API local journal.

C++
    
    
    MTAPIRES  IMTManagerAPI::LoggerOutString(
       const UINT       code,     // log code
       LPCWSTR          string    // log string
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.LoggerOutString(
       EnMTLogCode      code,     // log code
       string           string    // log string
       )

### Parameters

**code**  
[in] Log code which is passed using theEnMTLogCodeenumerations.

**string**  
[in] Log string with optional arguments.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Compared to [IMTManagerAPI::LoggerOut](LoggerOut.md), which formats the output, this method consumes less resources.
