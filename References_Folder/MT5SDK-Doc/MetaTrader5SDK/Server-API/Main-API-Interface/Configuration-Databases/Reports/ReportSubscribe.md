[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportSubscribe

[Previous](ReportParamCreate.md) | [Next](ReportUnsubscribe.md)

# IMTServerAPI::ReportSubscribe

Subscribe to events and hooks associated with the configuration of reports.
    
    
    MTAPIRES  IMTServerAPI::ReportSubscribe(
       IMTConReportSink*  sink      // A pointer to the IMTConReportSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConReportSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConReportSink](../../../../Configuration-Interfaces/Reports/IMTConReportSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
