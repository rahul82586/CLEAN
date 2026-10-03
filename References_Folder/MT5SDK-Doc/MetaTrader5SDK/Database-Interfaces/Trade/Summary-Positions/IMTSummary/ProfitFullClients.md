[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / ProfitFullClients

[Previous](ProfitCoverage.md) | [Next](ProfitFullCoverage.md)

# IMTSummary::ProfitFullClients

Gets the total profit/loss of client positions including swaps and commissions. The currency in which the profit is calculated is set using the [IMTManagerAPI::SummaryCurrency](../../../../Manager-API/Manager-Interface/Summary-Positions/SummaryCurrency.md) method.

C++
    
    
    double  IMTSummary::ProfitFullClients()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTSummary.ProfitFullClients()

### Return Value

The total profit (loss) of client positions including swaps and commissions.
