[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests EOSSessionStart

[Previous](Requests-PositionPriceTP.md) | [Next](Requests-EOSSessionEnd.md)

# IMTExecution::EOSSessionStart

Get the time of the session beginning.

C++
    
    
    INT64  IMTExecution::EOSSessionStart()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTExecution.EOSSessionStart()

### Return Value

The time of the session beginning, specified in seconds that have elapsed since 01.01.1970.

# IMTExecution::EOSSessionStart

Set the time of the session beginning.

C++
    
    
    MTAPIRES  IMTExecution::EOSSessionStart(
       INT64  start      // Beginning of the session
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.EOSSessionStart(
       long   start      // Beginning of the session
       )

### Parameters

**start**  
[in] The time of the session beginning, specified in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The beginning and end of the session are specified when generating a trade execution for the event of recalculation of daily deals at the end of a trading session ([IMTExecution::EOS_CALC_DEALS (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions)).
