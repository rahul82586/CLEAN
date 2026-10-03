[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests EOSProrfitRate

[Previous](Requests-EOSProrfitRateSell.md) | [Next](Requests-EOSTickValue.md)

# IMTExecution::EOSProrfitRate

Set a new rate for recalculating profit/loss for the deals performed during the session.

C++
    
    
    MTAPIRES  IMTExecution::EOSProrfitRate(
       const double  rate_buy      // A rate for buy deals
       const double  rate_sell     // A rate for sell deals
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.EOSProrfitRate(
       double        rate_buy      // A rate for buy deals
       double        rate_sell     // A rate for sell deals
       )

### Parameters

**rate_buy**  
[in] A rate for recalculating profit/loss for buy deals.

**rate_sell**  
[in] A rate for recalculating profit/loss for sell deals.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The new rate is used for generating a trade execution for the event of return recalculation for the deals executed during the trading session ([IMTExecution::EOS_CALC_DEALS (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions)).
