[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportSink](../IMTConReportSink.md) / OnReportDelete

[Previous](OnReportUpdate.md) | [Next](OnReportSync.md)

# IMTConReportSink::OnReportDelete

A handler of the event of removing a report configuration.

C++
    
    
    virtual void  IMTConReportSink::OnReportDelete(
       const IMTConReport*  report      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConReportSink.OnReportDelete(
       CIMTConReport        report      // Configuration object
       )

### Parameters

**report**  
A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify of the fact that a report configuration has been deleted.
