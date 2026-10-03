[🏠 Document Start](../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../../Platform-Components.md) / [Backup Server](../../../Backup-Server.md) / [SQL Export](../../SQL-Export.md) / [mt5_orders](../mt5-orders.md) / Enumerations

[Previous](../mt5-orders.md) | [Next](../mt5-orders-history.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

To pass information about orders the following enumerations are used:

  * [EnOrderType (#enordertype)](Enumerations.md#enordertype)
  * [EnOrderFilling (#enorderfilling)](Enumerations.md#enorderfilling)
  * [EnOrderTime (#enordertime)](Enumerations.md#enordertime)
  * [EnOrderState (#enorderstate)](Enumerations.md#enorderstate)
  * [EnOrderActivation (#enorderactivation)](Enumerations.md#enorderactivation)
  * [EnOrderReason (#enorderreason)](Enumerations.md#enorderreason)
  * [EnTradeActivationFlags (#entradeactivationflags)](Enumerations.md#entradeactivationflags)


  * [EnTradeModifyFlags (#entrademodifyflags)](Enumerations.md#entrademodifyflags)



<a id="enordertype"></a>
## EnOrderType (#enordertype)

Types of trade orders are listed in EnOrderType.

ID number | Value | Description  
OP_BUY | 0 | A Buy order.  
OP_SELL | 1 | A Sell order.  
OP_BUY_LIMIT | 2 | A Buy Limit order.  
OP_SELL_LIMIT | 3 | A Sell Limit order.  
OP_BUY_STOP | 4 | A Buy Stop order.  
OP_SELL_STOP | 5 | A Sell Stop order.  
OP_BUY_STOP_LIMIT | 6 | A Buy Stop Limit .  
OP_SELL_STOP_LIMIT | 7 | A Sell Stop Limit order.  
OP_CLOSE_BY | 8 | A close by order — closing two oppositely directed positions at a single symbol. This type of operations is used only for the hedging position accounting system ([MARGIN_MODE_RETAIL_HEDGED (#enmarginmode)](../mt5-groups/Enumerations.md#enmarginmode)).  
  
<a id="enorderfilling"></a>
## EnOrderFilling (#enorderfilling)

Types of order filling are listed in EnOrderFilling.

ID number | Value | Description  
ORDER_FILL_FOK | 0 | Fill or Kill. The order must be filled completely or canceled. This type of filling is automatically set for the instant and request execution.  
ORDER_FILL_IOC | 1 | Immediate or Cancel. An order can be filled partially and the residual volume is canceled. This type of filling is only available for the stock and market execution.  
ORDER_FILL_RETURN | 2 | Return the remainder to the queue. This mode is intended only for pending orders.  
  
<a id="enordertime"></a>
## EnOrderTime (#enordertime)

Types of order expiration are listed in EnOrderTime.

ID number | Value | Description  
ORDER_TIME_GTC | 0 | Good till Canceled.  
ORDER_TIME_DAY | 1 | Intraday.  
ORDER_TIME_SPECIFIED | 2 | Specified time.  
ORDER_TIME_SPECIFIED_DAY | 3 | Specified day. An order expires at 00:00 of the specified day or the nearest trading time.  
  
<a id="enorderstate"></a>
## EnOrderState (#enorderstate)

Possible staes of orders are listed in EnOrderState.

ID number | Value | Description  
ORDER_STATE_STARTED | 0 | Started.  
ORDER_STATE_PLACED | 1 | Placed.  
ORDER_STATE_CANCELED | 2 | Canceled.  
ORDER_STATE_PARTIAL | 3 | Partially filled.  
ORDER_STATE_FILLED | 4 | Filled.  
ORDER_STATE_REJECTED | 5 | Rejected.  
ORDER_STATE_EXPIRED | 6 | Expired.  
ORDER_STATE_REQUEST_ADD | 7 | The order passed (by the gateway) to be placed. This state is used for notifying that a request for placing the order is being already processed.  
ORDER_STATE_REQUEST_MODIFY | 8 | The order passed (by the gateway) to be modified. This state is used for notifying that a request for modifying the order is being already processed.  
ORDER_STATE_REQUEST_CANCEL | 9 | The order passed (by the gateway) to be deleted. This state is used for notifying that a request for deleting the order is being already processed.  
  
<a id="enorderactivation"></a>
## EnOrderActivation (#enorderactivation)

Types of order activation are listed in EnOrderActivation.

ID number | Value | Description  
ACTIVATION_NONE | 0 | Not activated.  
ACTIVATION_PENDING | 1 | Activation of a pending order.  
ACTIVATION_STOPLIMIT | 2 | Activation of a Stop Limit order.  
ACTIVATION_EXPIRATION | 3 | Cancellation of an order upon expiration.  
ACTIVATION_STOPOUT | 4 | Order is being removed because of a stop out.  
  
<a id="enorderreason"></a>
## EnOrderReason (#enorderreason)

Types of reasons for order placing are listed in EnOrderReason.

ID number | Value | Description  
ORDER_REASON_CLIENT | 0 | Order placed by a client manually through the client terminal.  
ORDER_REASON_EXPERT | 1 | Order placed by a client with using an Expert Advisor.  
ORDER_REASON_DEALER | 2 | Order placed by a dealer through the manager terminal.  
ORDER_REASON_SL | 3 | Order placed as a result of Stop Loss activation.  
ORDER_REASON_TP | 4 | Order placed as a result of Take Profit activation.  
ORDER_REASON_SO | 5 | Order placed when the client reached the Stop-Out level.  
ORDER_REASON_ROLLOVER | 6 | Order placed when reopening a position for charging swaps.  
ORDER_REASON_EXTERNAL_CLIENT | 7 | Order placed by a client from an external trading system.  
ORDER_REASON_VMARGIN | 8 | Order placed for accruing variation margin.  
ORDER_REASON_GATEWAY | 9 | Order placed by a MetaTrader 5 gateway that had connected to the trading platform.  
ORDER_REASON_SIGNAL | 10 | Order placed as a result of copying [a trade signal](https://www.mql5.com/en/signals "Trading signals") according to a subscription in the client terminal.  
ORDER_REASON_SETTLEMENT | 11 | Order placed as a result of performing operations connected with the settlement of a futures contract/option. Not used at the moment.  
ORDER_REASON_TRANSFER | 12 | Order placed due to transferring a position at the settlement price to a new symbol with the same underlying asset. Not used at the moment.  
ORDER_REASON_SYNC | 13 | Order placed as a result of synchronization of an account's trade state with an external system.  
ORDER_REASON_EXTERNAL_SERVICE | 14 | Order placed from an external trading system for technical reasons (for example, to correct the trade state of a client).  
ORDER_REASON_MIGRATION | 15 | Order created as a result of importing trade operations from a MetaTrader 4 server.  
ORDER_REASON_MOBILE | 16 | Order created via the MetaTrader 5 mobile terminal for Android or iPhone.  
ORDER_REASON_WEB | 17 | Order created via the web terminal.  
ORDER_REASON_SPLIT | 18 | Order created as a result of a symbol split.  
ORDER_REASON_CORPORATE_ACTION | 19 | Order created as a result of a corporate action, such as consolidating or renaming securities, transferring a client to a different account, etc. API applications set this flag for service operations so that the platform does not account for such corporate actions in commission calculations.  
  
<a id="entradeactivationflags"></a>
## EnTradeActivationFlags (#entradeactivationflags)

Types of activation flags that can be assigned to orders upon forming a trade execution are listed in EnTradeActivationFlags:

ID number | Value | Description  
ACTIV_FLAGS_NO_LIMIT | 0x01 | Do not handle reaching of the Limit level.  
ACTIV_FLAGS_NO_STOP | 0x02 | Do not handle the reaching of the stop level.  
ACTIV_FLAGS_NO_SLIMIT | 0x04 | Do not handle reaching of the Stop-Limit level.  
ACTIV_FLAGS_NO_SL | 0x08 | Do not handle activation upon Stop Loss.  
ACTIV_FLAGS_NO_TP | 0x10 | Do not handle activation upon Take Profit.  
ACTIV_FLAGS_NO_SO | 0x20 | Do not handle activation upon Stop-Out.  
ACTIV_FLAGS_NO_EXPIRATION | 0x40 | Do not handle order cancellation upon expiration.  
ACTIV_FLAGS_NONE | 0x00 | No flags.  
  
Flags of orders are inherited by [positions](../mt5-positions.md) created as a result of their execution.

<a id="entrademodifyflags"></a>
## EnTradeModifyFlags (#entrademodifyflags)

EnTradeModifyFlags lists the flags assigned to orders when they are changed by an administrator, manager or API:

ID number | Value | Description  
MODIFY_FLAGS_ADMIN | 0x00000001 | Order changed by an administrator.  
MODIFY_FLAGS_MANAGER | 0x00000002 | Open price has been modified by a manager.  
MODIFY_FLAGS_POSITION | 0x00000004 | Flag not used for orders.  
MODIFY_FLAGS_RESTORE | 0x00000008 | Order restored.  
MODIFY_FLAGS_API_ADMIN | 0x00000010 | Order changed via Manager API administrator interface.  
MODIFY_FLAGS_API_MANAGER | 0x00000020 | Order changed via Manager API manager interface.  
MODIFY_FLAGS_API_SERVER | 0x00000040 | Order changed via Server API.  
MODIFY_FLAGS_API_GATEWAY | 0x00000080 | Order changed via Gateway API.  
ACTIV_FLAGS_NONE | 0x00000000 | No flags.
