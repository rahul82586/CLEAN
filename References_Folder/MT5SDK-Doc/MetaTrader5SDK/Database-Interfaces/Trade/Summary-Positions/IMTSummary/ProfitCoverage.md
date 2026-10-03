[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / ProfitCoverage

[Previous](ProfitClients.md) | [Next](ProfitFullClients.md)

# IMTSummary::ProfitCoverage

Gets the total profit/loss of hedging positions excluding swaps and commissions. The currency in which the profit is calculated is set using the [IMTManagerAPI::SummaryCurrency](../../../../Manager-API/Manager-Interface/Summary-Positions/SummaryCurrency.md) method.

C++
    
    
    double  IMTSummary::ProfitCoverage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTSummary.ProfitCoverage()

### Return Value

The total profit (loss) of hedging positions excluding swaps and commissions.

### Note

Positions of all hedging accounts from all coverage* groups are taken into account.
