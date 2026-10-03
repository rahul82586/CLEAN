[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests EOSProrfitRateBuy

[Previous](Requests-EOSPriceSettlement.md) | [Next](Requests-EOSProrfitRateSell.md)

# IMTExecution::EOSProrfitRateBuy

Get a new rate for recalculating profit/loss for buy deals.

C++
    
    
    double  IMTExecution::EOSProrfitRateBuy()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.EOSProrfitRateBuy()

### Return Value

A new rate for recalculating profit/loss for buy deals.

### Note

The new rate is used for generating a trade execution for the event of return recalculation for the deals executed during the trading session ([IMTExecution::EOS_CALC_DEALS (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions)).
