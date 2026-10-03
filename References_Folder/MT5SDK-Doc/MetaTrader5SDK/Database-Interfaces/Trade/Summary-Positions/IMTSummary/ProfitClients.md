[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / ProfitClients

[Previous](PriceSellCoverage.md) | [Next](ProfitCoverage.md)

# IMTSummary::ProfitClients

Gets the total profit/loss of client positions excluding swaps and commissions. The currency in which the profit is calculated is set using the [IMTManagerAPI::SummaryCurrency](../../../../Manager-API/Manager-Interface/Summary-Positions/SummaryCurrency.md) method.

C++
    
    
    double  IMTSummary::ProfitClients()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTSummary.ProfitClients()

### Return Value

The total profit (loss) of client positions excluding swaps and commissions.
