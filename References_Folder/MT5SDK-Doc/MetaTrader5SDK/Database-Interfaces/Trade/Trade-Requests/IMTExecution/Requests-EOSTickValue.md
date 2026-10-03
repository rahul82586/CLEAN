[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests EOSTickValue

[Previous](Requests-EOSProrfitRate.md) | [Next](Requests-EOSRolloverValueLong.md)

# IMTExecution::EOSTickValue

Set a new tick price for recalculating profit/loss for the deals performed during the session.

C++
    
    
    MTAPIRES  IMTExecution::EOSTickValue(
       const double  value     // Tick price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.EOSTickValue(
       double        value     // Tick price
       )

### Parameters

**value**  
[in] A new tick price for recalculating profit/loss for the deals performed during the session.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The new tick price is used for generating a trade execution for the event of return recalculation for the deals executed during the trading session ([IMTExecution::EOS_CALC_DEALS (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions)).

The bounds of the session for which the return recalculation is performed, are determined using the methods [IMTExecution:: EOSSessionStart](Requests-EOSSessionStart.md) and [IMTExecution:: EOSSessionEnd](Requests-EOSSessionEnd.md).

If the new tick price is not specified, a value from the symbol settings is used ([IMTConSymbol::TickValue](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TickValue.md)).
