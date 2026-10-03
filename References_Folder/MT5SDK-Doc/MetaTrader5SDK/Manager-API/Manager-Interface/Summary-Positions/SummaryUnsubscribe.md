[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Summary Positions](../Summary-Positions.md) / SummaryUnsubscribe

[Previous](SummarySubscribe.md) | [Next](SummaryCurrency.md)

# IMTManagerAPI::SummaryUnsubscribe

Unsubscribe from events associated with changes in the summary of clients' positions.

C++
    
    
    MTAPIRES  IMTManagerAPI::SummaryUnsubscribe(
       IMTSummarySink*  sink      // A pointer to the IMTSummarySink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SummaryUnsubscribe(
       CIMTSummarySink  sink      // CIMTSummarySink object
       )

Python
    
    
    ManagerAPI.SummaryUnsubscribe(
       sink             # IMTSummarySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTSummarySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This is a pair method to [IMTManagerAPI::SummarySubscribe](SummarySubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
