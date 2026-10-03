[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Summary Positions](../Summary-Positions.md) / SummarySubscribe

[Previous](SummaryCreateArray.md) | [Next](SummaryUnsubscribe.md)

# IMTManagerAPI::SummarySubscribe

Subscribe to events associated with changes in the summary of clients' positions.

C++
    
    
    MTAPIRES  IMTManagerAPI::SummarySubscribe(
       IMTSummarySink*  sink      // A pointer to the IMTSummarySink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SummarySubscribe(
       CIMTSummarySink  sink      // CIMTSummarySink object
       )

Python
    
    
    ManagerAPI.SummarySubscribe(
       sink             # IMTSummarySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTSummarySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTSummarySink](../../../Database-Interfaces/Trade/Summary-Positions/IMTSummarySink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
