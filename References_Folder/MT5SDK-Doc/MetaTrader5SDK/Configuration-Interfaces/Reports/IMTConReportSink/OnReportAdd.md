[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportSink](../IMTConReportSink.md) / OnReportAdd

[Previous](../IMTConReportSink.md) | [Next](OnReportUpdate.md)

# IMTConReportSink::OnReportAdd

A handler of the event of adding a new report configuration.

C++
    
    
    virtual void  IMTConReportSink::OnReportAdd(
       const IMTConReport*  report      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConReportSink.OnReportAdd(
       CIMTConReport        report      // Configuration object
       )

### Parameters

**report**  
[in] A pointer to the object of the added configuration.

### Note

This method is called by the API to notify of adding of a new report configuration.
