[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Entry Points](../Entry-Points.md) / MTReportAbout

[Previous](../Entry-Points.md) | [Next](MTReportCreate.md)

# MTReportAbout

Point MTReportAbout provides the initial information about the report module to the server.
    
    
    MTAPIENTRY MTAPIRES  MTReportAbout(
       const UINT     index     // Report index
       MTReportInfo&  info      // Reference to MTReportInfo
       )

### Parameters

**index**  
[in] Report index within the module beginning from zero.

**info**  
[out] A reference to theMTReportInfostructure.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. If the return code is different from MT_RET_OK, the plug will not appear in the list of modules.

### Note

The module must correctly fill in the [MTReportInfo](../../Structures/MTReportInfo.md) structure.
