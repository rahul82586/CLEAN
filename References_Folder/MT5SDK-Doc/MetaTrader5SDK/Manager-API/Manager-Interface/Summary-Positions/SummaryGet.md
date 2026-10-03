[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Summary Positions](../Summary-Positions.md) / SummaryGet

[Previous](SummaryNext.md) | [Next](SummaryGetAll.md)

# IMTManagerAPI::SummaryGet

Get a record from a summary table for a symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::SummaryGet(
       LPCWSTR      symbol,      // Symbol
       IMTSummary*  summary      // Summary position object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SummaryGet(
       string       symbol,      // Symbol
       CIMTSummary  summary      // Summary position object
       )

Python
    
    
    ManagerAPI.SummaryGet(
       str          symbol       # Symbol
       )

### Parameters

**symbol**  
[in] Symbol.

**summary**  
[out] Summary position object. The summary object must first be created using theIMTManagerAPI::SummaryCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To receive information about summary, it is necessary to subscribe to events of its changes using the [IMTManagerAPI::SummarySubscribe](SummarySubscribe.md) method.
