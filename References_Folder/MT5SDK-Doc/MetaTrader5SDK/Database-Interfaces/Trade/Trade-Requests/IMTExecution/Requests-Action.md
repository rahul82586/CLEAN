[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Action

[Previous](Requests-ExternalAccount.md) | [Next](Requests-Datetime.md)

# IMTExecution::Action

Get the trade execution type.

C++
    
    
    UINT  IMTExecution::Action()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.Action()

### Return Value

A value of the [IMTExecution::EnTradeExecutions (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions) enumeration.

# IMTExecution::Action

Set the trade execution type.

C++
    
    
    MTAPIRES  IMTExecution::Action(
       const UINT  action      // Trade execution type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Action(
       uint        action      // Trade execution type
       )

### Parameters

**action**  
[in] Trade execution type. To pass the type, theIMTExecution::EnTradeExecutionsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
