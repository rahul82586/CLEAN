[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Common Functions](../Common-Functions.md) / LoggerOut

[Previous](Free.md) | [Next](LoggerOutString.md)

# IMTServerAPI::LoggerOut

Add messages to the server journal.
    
    
    MTAPIRES  IMTServerAPI::LoggerOut(
       const UINT  code,     // Message code
       LPCWSTR     msg,      // Message string
                   ...       // Optional arguments
       )

### Parameters

**code**  
[in] Message code that is passed using theEnMTLogCodeenumeration.

**msg**  
[in] A message string with optional arguments.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Each string is limited to 16KB without the standard string header.
