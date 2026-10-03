[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Common Functions](../Common-Functions.md) / LoggerOutString

[Previous](LoggerOut.md) | [Next](LoggerFlush.md)

# IMTGatewayAPI::LoggerOutString

Quick output of unformatted stings to the journal.

C++
    
    
    MTAPIRES  IMTGatewayAPI::LoggerOutString(
       const UINT        code,   // log code
       LPCWSTR           string  // log string
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.LoggerOutString(
       EnMTLogCode      code,    // log code
       string           string   // log string
       )

### Parameters

**code**  
[in] Log code which is passed using theEnMTLogCodeenumerations.

**msg**  
[in] The message string.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Compared to [IMTGatewayAPI::LoggerOut](LoggerOut.md), which formats the output, this method consumes less resources.
