[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Common Functions](../Common-Functions.md) / LoggerOut

[Previous](Free.md) | [Next](LoggerOutString.md)

# IMTAdminAPI::LoggerOut

Add messages to the local journal of the administrator interface.

C++
    
    
    MTAPIRES  IMTAdminAPI::LoggerOut(
       const UINT  code,     // Message code
       LPCWSTR     format,   // Message string
                   ...       // Optional arguments
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LoggerOut(
       EnMTLogCode      code,    // Message code
       string           format,  // Message string
       params object[]  args     // Optional arguments
       )

Python
    
    
    AdminAPI.LoggerOut(
       code,            # Message code
       msg              # Message string
       )

### Parameters

**code**  
[in] Message code that is passed using theEnMTLogCodeenumeration.

**format**  
[in] A message string with optional arguments.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Each string is limited to 16KB without the standard string header.
