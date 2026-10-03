[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests EOSProrfitRateSell

[Previous](Requests-EOSProrfitRateBuy.md) | [Next](Requests-EOSProrfitRate.md)

# IMTExecution::EOSProrfitRateSell

Get a new rate for recalculating profit/loss for sell deals.

C++
    
    
    double  IMTExecution::EOSProrfitRateSell()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.EOSProrfitRateSell()

### Return Value

A new rate for recalculating profit/loss for sell deals.

### Note

The new rate is used for generating a trade execution for the event of return recalculation for the deals executed during the trading session ([IMTExecution::EOS_CALC_DEALS (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions)).
