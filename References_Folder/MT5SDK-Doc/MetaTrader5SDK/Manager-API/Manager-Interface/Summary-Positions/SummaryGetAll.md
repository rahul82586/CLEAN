[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Summary Positions](../Summary-Positions.md) / SummaryGetAll

[Previous](SummaryGet.md) | [Next](../Exposure.md)

# IMTManagerAPI::SummaryGetAll

Get an array of summary records.

C++
    
    
    MTAPIRES  IMTManagerAPI::SummaryGetAll(
       IMTSummaryArray*  summary      // An object of the array of summary positions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SummaryGetAll(
       CIMTSummaryArray  summary      // An object of the array of summary positions
       )

Python
    
    
    ManagerAPI.SummaryGetAll()

### Parameters

**summary**  
[out] An object of the array of summary positions. The summary object must first be created using theIMTManagerAPI::SummaryCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To receive information about summary, it is necessary to subscribe to events of its changes using the [IMTManagerAPI::SummarySubscribe](SummarySubscribe.md) method.

Information about the profit/loss of positions ([IMTSummary::Profit*](../../../Database-Interfaces/Trade/Summary-Positions/IMTSummary/ProfitClients.md)) belonging to clients, whose deposit currency ([IMTConGroup::Currency](../../../Configuration-Interfaces/Groups/IMTConGroup/Currency.md)) differs from the summary currency ([IMTManagerAPI::SummaryCurrency](SummaryCurrency.md)) may not be available immediately. After connecting and synchronizing with the server, the Manager API application must receive at least one quote for the symbol, required for converting profit from the deposit currency to the summary currency. Until then, the values of [IMTSummary::Profit*](../../../Database-Interfaces/Trade/Summary-Positions/IMTSummary/ProfitClients.md) for such clients will be zero. Information on position volumes ([IMTSummary::Volume*](../../../Database-Interfaces/Trade/Summary-Positions/IMTSummary/VolumeBuyClients.md)) is available immediately.
