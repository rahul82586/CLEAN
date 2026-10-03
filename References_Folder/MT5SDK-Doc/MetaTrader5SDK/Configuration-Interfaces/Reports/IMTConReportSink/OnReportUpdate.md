[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportSink](../IMTConReportSink.md) / OnReportUpdate

[Previous](OnReportAdd.md) | [Next](OnReportDelete.md)

# IMTConReportSink::OnReportUpdate

A handler of the event of updating a report configuration.

C++
    
    
    virtual void  IMTConReportSink::OnReportUpdate(
       const IMTConReport*  report      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConReportSink.OnReportUpdate(
       CIMTConReport        report      // Configuration object
       )

### Parameters

**report**  
[in] A pointer to the updated configuration object.

### Note

This method is called by the API to notify of the fact that a report configuration has been updated.
