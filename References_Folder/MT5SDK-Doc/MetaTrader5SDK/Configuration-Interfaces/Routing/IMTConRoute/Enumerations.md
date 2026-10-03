[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / Enumerations

[Previous](../IMTConRoute.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConRoute](../IMTConRoute.md) class contains the following enumerations:

  * [IMTConRoute::EnRouteMode (#enroutemode)](Enumerations.md#enroutemode)
  * [IMTConRoute::EnRouteFlags (#enrouteflags)](Enumerations.md#enrouteflags)
  * [IMTConRoute::EnTypeFlags (#entypeflags)](Enumerations.md#entypeflags)
  * [IMTConRoute::EnRouteAction (#enrouteaction)](Enumerations.md#enrouteaction)



<a id="enroutemode"></a>
## IMTConRoute::EnRouteMode (#enroutemode)

The states of a routing rule are listed in IMTConRoute::EnRouteMode.

ID | Value | Description  
MODE_DISABLED | 0 | The rule is disabled.  
MODE_ENABLED | 1 | The rule is enabled.  
MODE_FIRST |  | Beginning of enumeration. Corresponds to MODE_DISABLED.  
MODE_LAST |  | End of enumeration. Corresponds to MODE_ENABLED.  
  
This enumeration is used in the [IMTConRoute::Mode](Mode.md) method.

<a id="enrouteflags"></a>
## IMTConRoute::EnRouteFlags (#enrouteflags)

Conditions for applying a rule based on the request type are enumerate in IMTConRoute::EnRouteFlags.

ID | Value | Description  
REQUEST_NONE | 0x00000000 | Conditions by the request type are not specified.  
REQUEST_PRICE | 0x00000001 | Price request (for request execution).  
REQUEST_REQUEST | 0x00000002 | Confirmation of order execution ar a dealer's type in the request execution mode (with the order confirmation option enabled).  
REQUEST_INSTANT | 0x00000004 | Placing an order in the instant execution mode.  
REQUEST_MARKET | 0x00000008 | Placing an order in the market execution mode.  
REQUEST_EXCHANGE | 0x00000010 | Placing an order in the exchange execution mode.  
REQUEST_PENDING | 0x00000020 | Placing a pending order.  
REQUEST_SLTP | 0x00000040 | Modification of Stop Loss and Take Profit of a position.  
REQUEST_MODIFY | 0x00000080 | Modification of a pending order.  
REQUEST_REMOVE | 0x00000100 | Deleting a pending order.  
REQUEST_ACTIVATE | 0x00000200 | Activation (triggering) of a pending order.  
REQUEST_STOPLIMIT | 0x00000400 | Activation of a Stop Limit order.  
REQUEST_SL | 0x00000800 | Triggering of a Stop Loss order.  
REQUEST_TP | 0x00001000 | Triggering of a Take Profit order.  
REQUEST_STOPOUT_ORDER | 0x00002000 | A request to delete a pending order in case of reaching the stop-out level (if margin requirements are set for pending orders)  
REQUEST_STOPOUT_POSITION | 0x00004000 | A request to close a position when reaching stop-out.  
REQUEST_EXPIRATION | 0x00008000 | Cancellation of an order upon expiration.  
REQUEST_DEALER_POS_EXECUTE | 0x00010000 | Position opening and closing by a dealer.  
REQUEST_DEALER_ORD_PENDING | 0x00020000 | Placing of a pending order by a dealer.  
REQUEST_DEALER_POS_MODIFY | 0x00040000 | Position modification by a dealer.  
REQUEST_DEALER_ORD_MODIFY | 0x00080000 | Order modification by a dealer.  
REQUEST_DEALER_ORD_REMOVE | 0x00100000 | Order deletion by a dealer.  
REQUEST_DEALER_ORD_ACTIVATE | 0x00200000 | Order activation by a dealer.  
REQUEST_DEALER_ORD_SLIMIT | 0x00400000 | Activation of a Stop Limit order by a dealer. After this action is performed, the order turns into a limit order.  
REQUEST_DEALER_CLOSE_BY | 0x00800000 | Close By. An operation of closing two oppositely directed positions at a single symbol performed by a dealer.  
REQUEST_CLOSE_BY | 0x01000000 | Close By. An operation of closing two oppositely directed positions at a single symbol performed by a client.  
REQUEST_ALL |  | Enabling all the above listed conditions.  
REQUEST_FIRST |  | Beginning of enumeration. Corresponds to REQUEST_NONE  
REQUEST_LAST |  | End of enumeration. Corresponds to REQUEST_ALL.  
  
This enumeration is used in the [IMTConRoute::Request](Request.md) method.

<a id="entypeflags"></a>
## IMTConRoute::EnTypeFlags (#entypeflags)

Conditions for applying a rule based on the order type are enumerate in IMTConRoute::EnTypeFlags.

ID | Value | Description  
TYPE_NONE | 0x0000 | No conditions by the order type.  
TYPE_BUY | 0x0001 | A Buy order.  
TYPE_SELL | 0x0002 | A Sell order.  
TYPE_BUY_LIMIT | 0x0004 | A limit Buy order.  
TYPE_SELL_LIMIT | 0x0008 | A limit Sell order.  
TYPE_BUY_STOP | 0x0010 | A stop Buy order.  
TYPE_SELL_STOP | 0x0020 | A stop Sell order.  
TYPE_BUY_STOP_LIMIT | 0x0040 | A limit Buy Stop order.  
TYPE_SELL_STOP_LIMIT | 0x0080 | A limit Sell Stop order.  
TYPE_ALL |  | All types of events.  
TYPE_FIRST |  | Beginning of enumeration. Corresponds to TYPE_NONE.  
TYPE_LAST |  | End of enumeration. Corresponds to TYPE_ALL.  
  
This enumeration is used in the [IMTConRoute::Type](Type.md) method.

<a id="enrouteaction"></a>
## IMTConRoute::EnRouteAction (#enrouteaction)

Types of actions that are applied to requests are listed in IMTConRoute::EnRouteAction.

ID | Value | Description  
ACTION_DELAY_TIME | 0 | Delay request execution by the specified number of milliseconds. After applying this action to a request, its execution continues in accordance with the created rules located below in the list. The delay is indicated in a separate parameter.  
ACTION_DELAY_TICK | 1 | Delay request execution by the specified number of ticks. After applying this action to a request, its execution continues in accordance with the created rules located below in the list. The delay is indicated in a separate parameter.  
ACTION_CLEAR_TP | 2 | Clear the Take Profit level set in the order.  
ACTION_CLEAR_SL | 3 | Clear the Stop Loss level set in the order.  
ACTION_CLEAR_SLTP | 4  | Clear the Stop Loss and Take Profit levels set in the order.  
ACTION_DEALER | 1001 | Enqueue the request to be processed by the specified dealer. To set the flag skipping action when there are no online dealers, set a nonzero value for the [IMTConRoute::ParamInt](ParamInt.md) parameter.  
ACTION_DEALER_ONLINE | 1002 | Pass the request to dealers that are currently online. To set the flag skipping action when there are no online dealers, set a nonzero value for the [IMTConRoute::ParamInt](ParamInt.md) parameter.  
ACTION_REJECT | 1003 | Reject a request. Along with this action, you can specify your own reason for rejecting the request. This reason will be displayed in the trading dialog in client terminals. Use the [IMTConRoute::ParamString](ParamString.md) field to add your comment. The maximum comment length is limited to 31 characters.  
ACTION_REQUOTE | 1004 | Send current market prices in response to the request.  
ACTION_CONFIRM_CLIENT | 1005 | Confirm the execution of an order at a price requested in it.  
ACTION_CONFIRM_MARKET | 1006 | Confirm the execution of an order at the current market price. The action is applied to both client orders and orders placed by dealers.  
ACTION_CANCEL_ORDER | 1007 | Cancel a pending order during its activation or modification. For example, if a pending order has triggered, but the client has already reached the maximum position volume and a new position cannot be opened, the routing rule will remove this order. Otherwise, the order would have continued to trigger on each new tick. When removing an order by this rule, "deleted [by dealer]" is added to the order comment. An entry about the routing rule that canceled the order is also added to the server journal. The server returns error code [MT_RET_REQUEST_REJECT_CANCEL](../../../Return-Codes/Trade-Requests.md). The action can only be applied during pending order activation or modification (including modification by a dealer). The rule does not affect other trade requests.  
ACTION_FIRST |  | Beginning of enumeration. Corresponds to ACTION_DELAY_TIME.  
ACTION_LAST |  | End of enumeration. Corresponds to ACTION_CANCEL_ORDER.  
  
This enumeration is used in the [IMTConRoute::Action](Action.md) method.
