[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerCurrent

[Previous](ManagerReportCreate.md) | [Next](ManagerTotal.md)

# IMTReportAPI::ManagerCurrent

Get the configuration of the manager that requested a report generation from a manager terminal.
    
    
    MTAPIRES  IMTReportAPI::ManagerCurrent(
       IMTConManager*  manager      // An object of manager configuration
       )

### Parameters

**manager**  
[out] An object of manager configuration. The manager object must be first created using theIMTReportAPI::ManagerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
