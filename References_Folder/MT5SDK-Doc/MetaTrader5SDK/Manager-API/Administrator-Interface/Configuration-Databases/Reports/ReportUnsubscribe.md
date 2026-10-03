[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportUnsubscribe

[Previous](ReportSubscribe.md) | [Next](ReportUpdate.md)

# IMTAdminAPI::ReportUnsubscribe

Unsubscribe from events associated with the configuration of reports.

C++
    
    
    MTAPIRES  IMTAdminAPI::ReportUnsubscribe(
       IMTConReportSink*  sink      // A pointer to the IMTConReportSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ReportUnsubscribe(
       CIMTConReportSink  sink      // CIMTConReportSink object
       )

Python
    
    
    AdminAPI.ReportUnsubscribe(
       sink               # IMTConReportSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConReportSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::ReportSubscribe](ReportSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
