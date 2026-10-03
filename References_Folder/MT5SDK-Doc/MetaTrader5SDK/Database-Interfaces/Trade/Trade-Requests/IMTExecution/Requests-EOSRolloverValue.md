[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests EOSRolloverValue

[Previous](Requests-EOSRolloverValueShort.md) | [Next](Requests-ApiDataSet.md)

# IMTExecution::EOSRolloverValue

Set the rollover size for a position.

C++
    
    
    MTAPIRES  IMTExecution::EOSRolloverValue(
       const double  value_long      // Long position rollover
       const double  value_short     // Short position rollover
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.EOSRolloverValue(
       double        value_long      // Long position rollover
       double        value_short     // Short position rollover
       )

### Parameters

**value_long**  
[in] Long position rollover set in the client's deposit currency.

**value_short**  
[in] Short position rollover set in the client's deposit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A symbol the rollover is accrued for is specified in the [IMTExecution::Symbol](Requests-Symbol.md) field. Short and long position rollover values in the value_long and value_short parameters are specified in the client's deposit currency. These values ​​will be added to the current (existing) values ​​of position rollovers in the [IMTPosition::Storage](../../Positions/IMTPosition/Storage.md) field.
