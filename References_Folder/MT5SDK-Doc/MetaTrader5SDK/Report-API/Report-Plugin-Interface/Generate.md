[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Report Plugin Interface](../Report-Plugin-Interface.md) / Generate

[Previous](Release.md) | [Next](../Main-Interface-of-Reports.md)

# IMTReportContext::Generate

Method of the generation of the report requested by a server during the arrival of an appropriate request from a manager terminal.
    
    
    MTAPIRES  IMTReportContext::Generate(
       const UINT    type,     // Type of a report
       IMTReportAPI  *api      // Pointer to the API interface
       )

### Parameters

**type**  
[in] Type of a generated report. Transfered using theMTReportInfo::EnTypesenumeration.

***api**  
[in] Pointer to the interface of the Report API.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Maximum allowed time for generating a report is 10 minutes.
