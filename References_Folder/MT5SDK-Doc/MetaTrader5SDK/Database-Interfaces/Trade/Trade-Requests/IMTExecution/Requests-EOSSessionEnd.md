[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests EOSSessionEnd

[Previous](Requests-EOSSessionStart.md) | [Next](Requests-EOSPriceSettlement.md)

# IMTExecution::EOSSessionEnd

Get the time of the session end.

C++
    
    
    INT64  IMTExecution::EOSSessionEnd()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTExecution.EOSSessionEnd()

### Return Value

The end of session time, specified in seconds that have elapsed since 01.01.1970.

# IMTExecution::EOSSessionEnd

Set the session end time.

C++
    
    
    MTAPIRES  IMTExecution::EOSSessionEnd(
       INT64  end      // End of the session
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.EOSSessionEnd(
       long   end      // End of the session
       )

### Parameters

**end**  
[in] The end of session time, specified in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The beginning and end of the session are specified when generating a trade execution for the event of recalculation of daily deals at the end of a trading session ([IMTExecution::EOS_CALC_DEALS (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions)).
