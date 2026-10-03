[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummarySink](../IMTSummarySink.md) / OnSummaryUpdate

[Previous](../IMTSummarySink.md) | [Next](../../Assets.md)

# IMTSummarySink::OnSummaryUpdate

A handler of an event of update of summary positions.

C++
    
    
    virtual void  IMTSummarySink::OnSummaryUpdate(
       const IMTSummary*  summary      // A pointer to the object of the summary position record
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSummarySink.OnSummaryUpdate(
       CIMTSummary        summary      // The object of the summary position record
       )

### Parameters

**summary**  
[in] A pointer to the object of the updated summary position record.

### Note

This method is called by the API to notify that a summary position record has been modified.
