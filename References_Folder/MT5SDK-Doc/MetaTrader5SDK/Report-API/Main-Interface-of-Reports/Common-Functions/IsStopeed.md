[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Common Functions](../Common-Functions.md) / IsStopeed

[Previous](LoggerOutString.md) | [Next](Clear.md)

# IMTReportAPI::IsStopped

Check the presence of the request to stop a report generation.
    
    
    MTAPIRES  IMTReportAPI::IsStopped()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Report generation can be stopped due to the following reasons:

Most of the Report API methods check the requests to stop generation by themselves.

  * a manager has refused to generate a report;
  * configuration of the module responsible for a report generation is turned off;
  * the trade server is stopped;
  * the time for a report generation is up.


