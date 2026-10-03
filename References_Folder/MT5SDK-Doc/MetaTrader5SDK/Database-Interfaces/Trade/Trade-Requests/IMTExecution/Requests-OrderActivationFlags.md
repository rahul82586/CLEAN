[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderActivationFlags

[Previous](Requests-OrderPrice.md) | [Next](Requests-OrderActivationMode.md)

# IMTExecution::OrderActivationFlags

Gets additional order activation conditions.

C++
    
    
    UINT  IMTExecution::OrderActivationFlags()

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.OrderActivationFlags()

### Return Value

A value of the [IMTOrder::EnTradeActivationFlags (#entradeactivationflags)](../../Orders/IMTOrder/Enumerations.md#entradeactivationflags) enumeration.

### Note

IMTExecution::OrderActivationFlags changes the value of the appropriate order field [IMTOrder::ActivationFlags](../../Orders/IMTOrder/ActivationFlags.md).

# IMTExecution::OrderActivationFlags

Sets additional order activation conditions.

C++
    
    
    MTAPIRES  IMTExecution::OrderActivationFlags(
       const UINT  activation      // Activation conditions
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderActivationFlags(
       uint        activation      // Activation conditions
       )

### Parameters

**activation**  
[in] Additional conditions for the activation of orders. TheIMTOrder::EnTradeActivationFlagsenumeration is used to pass the conditions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

IMTExecution::OrderActivationFlags changes the value of the appropriate order field [IMTOrder::ActivationFlags](../../Orders/IMTOrder/ActivationFlags.md).

Client | Gateway API  
---|---  
Sending a request. |   
| Receiving a request from the queue.  
| Request confirmation ([IMTConfirm](../IMTConfirm/Requests-Retcode.md)) with the response code [MT_RET_REQUEST_PLACED](../../../../Return-Codes/Trade-Requests.md). The state [IMTOrder::ORDER_STATE_PLACED (#enorderstate)](../../Orders/IMTOrder/Enumerations.md#enorderstate) is set for a confirmed order.  
| Trade execution of the [IMTExecition::TE_ORDER_NEW_REQUEST](Requests-Enumerations.md) type meaning that the order has been accepted for processing. Depending on the type of a trade request, one of the following [states (#enorderstate)](../../Orders/IMTOrder/Enumerations.md#enorderstate) can be set to an order: ORDER_STATE_REQUEST_ADD, ORDER_STATE_REQUEST_MODIFY or ORDER_STATE_REQUEST_CANCEL. At this stage you can specify [additional flags (#entradeactivationflags)](../../Orders/IMTOrder/Enumerations.md#entradeactivationflags) to indicate which events should not be handled on the MetaTrader 5 server side.  
| Depending on the results of processing in an external trading system, the IMTExecution trade execution of the corresponding type is formed: [TE_ORDER_NEW (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions), [TE_ORDER_FILL (#entradeexecutions)](Requests-Enumerations.md#entradeexecutions) etc.
