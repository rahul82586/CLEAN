[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Entry Points](../Entry-Points.md) / MTReportCreate

[Previous](MTReportAbout.md) | [Next](../Report-Plugin-Interface.md)

# MTReportCreate

MTReportCreate entry point. This method is called by the server to create an instance of an object of the reports module that implements the [IMTReportContext](../Report-Plugin-Interface.md) interface.
    
    
    MTAPIENTRY MTAPIRES  MTReportCreate(
       const UINT         index,          // Report index
       const UINT         apiversion,     // API Version
       IMTReportConext**  context         // Pointer to a pointer to the module
       )

### Parameters

**index**  
[in] Report index within the module beginning from zero.

**apiversion**  
[in] The current version of the Report API supported by the server is passed in this parameter.

**context**  
[out] A pointer to a pointer to thereports context.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
