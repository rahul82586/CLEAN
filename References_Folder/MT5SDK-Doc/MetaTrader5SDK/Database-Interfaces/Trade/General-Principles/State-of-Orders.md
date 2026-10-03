[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [General Principles](../General-Principles.md) / State of Orders

[Previous](Types-of-Execution.md) | [Next](Fill-Policy.md)

# State of Orders

Every order on the trade server is in a certain state. The state provides information on how the order has been processed. The following states are possible

  * Started — the order correctness has been checked, and now the order is waiting to be processed
  * Placed — the order has been accepted and placed
  * Partially filled — the order has been partially filled, the market operation has been executed for part of the initially requested volume
  * Filled — the order has been filled in full
  * Canceled — the order has been canceled by client
  * Rejected — the order has been rejected
  * Expired — the order was canceled upon expiration
  * Request adding — a request to place an order has been forwarded to an external system
  * Request modification — a request to modify an order has been forwarded to an external system
  * Request canceling — a request to delete an order has been forwarded to an external system



> Possible states of orders are listed in [IMTOrder::EnOrderState (#enorderstate)](../Orders/IMTOrder/Enumerations.md#enorderstate).

You should differentiate between trading requests ([IMTRequest](../Trade-Requests/Requests-IMTRequest.md)) and orders ([IMTOrder](../Orders/IMTOrder.md)). Client and manager terminals, as well as Manager API applications send trading requests to the trade server. The server checks these requests for correctness and adds them to the queue for processing. At this moment, an order in the Started state is formed based on the trading request.

Further request processing depends on routing rules ([IMTConRoute](../../../Configuration-Interfaces/Routing/IMTConRoute.md)): it can be immediately rejected (the order state changes to Rejected), sent for processing to a dealer or a gateway, or processed by the trade server. 

## Processing by the Gateway or Dealer

The dealer or the gateway can immediately process the request or forward it to an external system for processing:

  * If the dealer/gateway generates the [IMTConfirm](../Trade-Requests/Requests-IMTConfirm.md) response with the [MT_RET_REQUEST_DONE](../../../Return-Codes/Trade-Requests.md) response code, the order is executed. If this is a market order, its state changes to Filled (or Partially Filled in case of a partial execution). If this is a pending order, the state changes to Placed.
  * If a gateway generates the [IMTConfirm](../Trade-Requests/Requests-IMTConfirm.md) response with the [MT_RET_REQUEST_PLACED](../../../Return-Codes/Trade-Requests.md) response code, the platform considers that the order will be processed in an external system. The order state changes to Placed (the order type does not matter). After that the gateway should send an appropriate request to an external system, receive a response and generate the [IMTExecution](../Trade-Requests/Requests-IMTExecution.md) trade execution. The next state of the order depends on the trade execution type. See the [Gateway API](../../../Gateway-API/Trade-Operations-in.md) section for more information about how operations are processed in an external system.
  * If the dealer/gateway generates the [IMTConfirm](../Trade-Requests/Requests-IMTConfirm.md) response with any other response code, the order is rejected, and the order state changes to Rejected.



## Processing by the Server

The request processing algorithm on the server depends on routing rules and the type of the request/order. For example, an order can be automatically confirmed. If this is a market order, its state changes to Filled or Partially Filled. If this is a pending order, the state changes to Placed. If the client has sent a request to cancel an order, the state of that order changes to Canceled.

## Active Orders on the Server

State of orders can change without any request from the client or dealer side. For example, expiration time can be specified in an order. The server cancels the order upon expiration, and the order state changes to Expired. If a pending order triggers, its state changes from Placed to Filled or Partially filled.

The below diagram shows the main stages of trade request processing with corresponding order states.

![order_state](images/order_state.png)
