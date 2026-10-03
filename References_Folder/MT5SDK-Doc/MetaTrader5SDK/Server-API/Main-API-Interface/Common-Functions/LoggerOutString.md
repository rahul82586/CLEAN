[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Common Functions](../Common-Functions.md) / LoggerOutString

[Previous](LoggerOut.md) | [Next](LoggerRequest.md)

# IMTServerAPI::LoggerOutString

Output unformatted stings to the server journal (quick output).
    
    
    MTAPIRES  IMTServerAPI::LoggerOutString(
       const UINT  code,     // log code
       LPCWSTR     string    // log string
       )

### Parameters

**code**  
[in] Log code which is passed using theEnMTLogCodeenumerations.

**string**  
[in] Log string with optional arguments.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Compared to [IMTServerAPI::LoggerOut](LoggerOut.md), which formats the output, this method uses less resources.
