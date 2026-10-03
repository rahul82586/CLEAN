[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / StateSet

[Previous](State.md) | [Next](Reason.md)

# IMTOrder::State

Sets the order state.

C++
    
    
    MTAPIRES  IMTOrder::StateSet(
       const UINT  state     // The order state
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.StateSet(
       uint        state     // The order state
       )

Python
    
    
    MTOrder.State()

### Parameters

**state**  
[in] Order state. The order state is passed using theIMTOrder::EnOrderStateenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an appropriate error code is returned.

### Note

Do not edit order states unless you have a specific reason, since this can cause serious consequences. For example, if you change the state of a filled order (ORDER_STATE_FILLED) to Placed (ORDER_STATE_PLACED), it can trigger once again.
