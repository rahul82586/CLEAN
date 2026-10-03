[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / ProfitUncovered

[Previous](ProfitFullCoverage.md) | [Next](ProfitUncoveredFull.md)

# IMTSummary::ProfitUncovered

Gets the difference between total profit (loss) of client and hedging positions excluding swaps and commissions. The currency in which the profit is calculated is set using the [IMTManagerAPI::SummaryCurrency](../../../../Manager-API/Manager-Interface/Summary-Positions/SummaryCurrency.md) method.

C++
    
    
    double  IMTSummary::ProfitUncovered()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTSummary.ProfitUncovered()

### Return Value

The difference between total profit (loss) of client and hedging positions excluding swaps and commissions.
