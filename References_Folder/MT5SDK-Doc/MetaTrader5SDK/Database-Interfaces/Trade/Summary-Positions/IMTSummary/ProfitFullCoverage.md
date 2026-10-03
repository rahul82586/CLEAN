[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / ProfitFullCoverage

[Previous](ProfitFullClients.md) | [Next](ProfitUncovered.md)

# IMTSummary::ProfitFullCoverage

Gets the total profit/loss of hedging positions of all symbols. The currency in which the profit is calculated is set using the [IMTManagerAPI::SummaryCurrency](../../../../Manager-API/Manager-Interface/Summary-Positions/SummaryCurrency.md) method.

C++
    
    
    double  IMTSummary::ProfitFullCoverage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTSummary.ProfitFullCoverage()

### Return Value

The total profit (loss) of hedging positions including swaps and commissions.

### Note

Positions of all hedging accounts from all coverage* groups are taken into account.
