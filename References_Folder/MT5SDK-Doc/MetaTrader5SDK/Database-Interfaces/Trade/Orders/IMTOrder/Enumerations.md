[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / Enumerations

[Previous](../IMTOrder.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTOrder](../IMTOrder.md) contains the following enumerations:

  * [IMTOrder::EnOrderType (#enordertype)](Enumerations.md#enordertype)
  * [IMTOrder::EnOrderFilling (#enorderfilling)](Enumerations.md#enorderfilling)
  * [IMTOrder::EnOrderTime (#enordertime)](Enumerations.md#enordertime)
  * [IMTOrder::EnOrderState (#enorderstate)](Enumerations.md#enorderstate)
  * [IMTOrder::EnOrderActivation (#enorderactivation)](Enumerations.md#enorderactivation)
  * [IMTOrder::EnOrderReason (#enorderreason)](Enumerations.md#enorderreason)
  * [IMTOrder::EnTradeActivationFlags (#entradeactivationflags)](Enumerations.md#entradeactivationflags)
  * [IMTOrder::EnTradeModifyFlags (#entrademodifyflags)](Enumerations.md#entrademodifyflags)



<a id="enordertype"></a>
## IMTOrder::EnOrderType (#enordertype)

[Types of trade orders](../../General-Principles/Types-of-Orders.md) are listed in IMTOrder::EnOrderType.

ID number | Value | Description  
OP_BUY | 0 | A Buy order.  
OP_SELL | 1 | A Sell order.  
OP_BUY_LIMIT | 2 | A Buy Limit order.  
OP_SELL_LIMIT | 3 | A Sell Limit order.  
OP_BUY_STOP | 4  | A Buy Stop order.  
OP_SELL_STOP | 5 | A Sell Stop order.  
OP_BUY_STOP_LIMIT | 6 | A Buy Stop Limit .  
OP_SELL_STOP_LIMIT | 7 | A Sell Stop Limit order.  
OP_CLOSE_BY | 8 | A Close By order — a simultaneous closure of two opposite positions of the sane financial instrument. This operation type is only used in the hedging mode ([EnMarginMode::MARGIN_MODE_RETAIL_HEDGED (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).  
OP_FIRST |  | Beginning of enumeration. In corresponds to OP_BUY.  
OP_LAST |  | End of enumeration. Corresponds to OP_CLOSE_BY.  
  
This enumeration is used in the following methods:

  * [IMTOrder::Type](Type.md)
  * [IMTRequest::Type](../../Trade-Requests/IMTRequest/Requests-Type.md)



<a id="enorderfilling"></a>
## IMTOrder::EnOrderFilling (#enorderfilling)

Order filling types are listed in IMTOrder::EnOrderFilling.

ID number | Value | Description  
ORDER_FILL_FOK | 0 | Fill or Kill. An order must be filled completely or canceled. This type of filling is automatically set for [the instant and request execution](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExecMode.md). This type can also be used for market and exchange execution, depending on the [IMTConSymbol::FillFlags](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/FillFlags.md) symbol setting.  
ORDER_FILL_IOC | 1 | Immediate or Cancel. An order can be filled partially and the residual volume is canceled. This filling type can be used for market orders with [market execution](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExecMode.md) and for all order types with [exchange execution](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExecMode.md). The availability of the type is determined by the [IMTConSymbol::FillFlags](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/FillFlags.md) symbol setting.  
ORDER_FILL_RETURN | 2 | Return the remainder to the queue. This mode is used for pending orders. It can be used for market orders only with [exchange execution](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExecMode.md).  
ORDER_FILL_BOC | 3 | The BOC policy indicates that an order can only be placed in the Depth of Market (order book). If the order can be filled immediately when placed, this order is canceled. This policy guarantees that the price of the placed order will be worse than the current market. BOC is used to implement passive trading: it is guaranteed that the order cannot be executed immediately when placed and thus it does not affect current liquidity. This fill policy is only supported for limit and stop limit orders.  
ORDER_FILL_FIRST |  | Beginning of enumeration. It corresponds to ORDER_FILL_FOK.  
ORDER_FILL_LAST |  | End of enumeration. It corresponds to ORDER_FILL_BOC.  
  
This enumeration is used in the following methods:

  * [IMTOrder::TypeFill](TypeFill.md)
  * [IMTRequest::TypeFill](../../Trade-Requests/IMTRequest/Requests-TypeFill.md)



<a id="enordertime"></a>
## IMTOrder::EnOrderTime (#enordertime)

Types of order expiration are listed in IMTOrder::EnOrderTime.

ID number | Value | Description  
ORDER_TIME_GTC | 0 | Good till Canceled.  
ORDER_TIME_DAY | 1 | Intraday.  
ORDER_TIME_SPECIFIED | 2 | Specified time.  
ORDER_TIME_SPECIFIED_DAY | 3 | Specified day. The expiration time is 00:00 of the specified day or the nearest trading time.  
ORDER_TIME_FIRST |  | Beginning of enumeration. It corresponds to ORDER_TIME_GTC.  
ORDER_TIME_LAST |  | End of enumeration. Corresponds to ORDER_TIME_SPECIFIED_DAY.  
  
This enumeration is used in the following methods:

  * [IMTOrder::TypeTime](TypeTime.md)
  * [IMTRequest::TypeTime](../../Trade-Requests/IMTRequest/Requests-TypeTime.md)



<a id="enorderstate"></a>
## IMTOrder::EnOrderState (#enorderstate)

Possible [states of orders](../../General-Principles/State-of-Orders.md) are listed in IMTOrder::EnOrderState.

ID number | Value | Description  
ORDER_STATE_STARTED | 0 | Started — the order correctness has been checked, and now the order is awaiting processing.  
ORDER_STATE_PLACED | 1 | Placed — for pending orders, this state means that the order has been accepted and placed. For market orders, this state is only used when forwarding operations to an external system. In this case, this state means that the order has been forwarded and is awaiting execution in the external system.  
ORDER_STATE_CANCELED | 2 | Canceled — the order has been canceled by the client.  
ORDER_STATE_PARTIAL | 3 | Partially filled — the order has been partially filled, so the market operation has been executed for part of the initially requested volume.  
ORDER_STATE_FILLED | 4  | Filled — the order has been filled in full.  
ORDER_STATE_REJECTED | 5 | Rejected — the order has been rejected by the broker.  
ORDER_STATE_EXPIRED | 6 | Expired — the order has been canceled upon expiration.  
ORDER_STATE_REQUEST_ADD | 7 | The order passed (by the gateway) to be placed. This state is used for notifying that a request for placing the order is being already processed.  
ORDER_STATE_REQUEST_MODIFY | 8 | The order passed (by the gateway) to be modified. This state is used for notifying that a request for modifying the order is being already processed.  
ORDER_STATE_REQUEST_CANCEL | 9 | The order passed (by the gateway) to be deleted. This state is used for notifying that a request for deleting the order is being already processed.  
ORDER_STATE_FIRST |  | Beginning of enumeration. It corresponds to ORDER_STATE_STARTED.  
ORDER_STATE_LAST |  | End of enumeration. It corresponds to ORDER_STATE_REQUEST_CANCEL.  
  
This enumeration is used in the [IMTOrder::State](State.md) method.

<a id="enorderactivation"></a>
## IMTOrder::EnOrderActivation (#enorderactivation)

Types of order activation are listed in EnOrderActivation.

ID number | Value | Description  
ACTIVATION_NONE | 0 | Not activated.  
ACTIVATION_PENDING | 1 | Activation of a pending order.  
ACTIVATION_STOPLIMIT | 2 | Activation of a Stop Limit order.  
ACTIVATION_EXPIRATION | 3 | Cancellation of an order upon expiration.  
ACTIVATION_STOPOUT | 4  | The order is being removed due to the stop-out.  
ACTIVATION_FIRST |  | Beginning of enumeration. It corresponds to ACTIVATION_FIRST.  
ACTIVATION_LAST |  | End of enumeration. Position::Action ACTIVATION_STOPOUT.  
  
This enumeration is used in the [IMTOrder::ActivationMode](ActivationMode.md) method.

<a id="enorderreason"></a>
## IMTOrder::EnOrderReason (#enorderreason)

Types of reasons for order placing are listed in IMTOrder::EnOrderReason.

ID number | Value | Description  
ORDER_REASON_CLIENT | 0 | Order placed by a client manually through the client terminal.  
ORDER_REASON_EXPERT | 1 | Order placed by a client with using an Expert Advisor.  
ORDER_REASON_DEALER | 2 | An order placed by a dealer from a manager terminal.  
ORDER_REASON_SL | 3 | Order placed as a result of Stop Loss activation.  
ORDER_REASON_TP | 4  | Order placed as a result of Take Profit activation.  
ORDER_REASON_SO | 5 | Order placed when the client reached the Stop-Out level.  
ORDER_REASON_ROLLOVER | 6 | Order placed when reopening a position for charging swaps.  
ORDER_REASON_EXTERNAL_CLIENT | 7 | The order has been placed by a client from the external trading system.  
ORDER_REASON_VMARGIN | 8 | The order was placed to calculate variation margin.  
ORDER_REASON_GATEWAY | 9 | The order has been placed by the MetaTrader 5 gateway connected to the platform.  
ORDER_REASON_SIGNAL | 10 | The order has been placed as a result of copying a [trading signal ](https://www.mql5.com/ru/signals "Trading Signals")according to the subscription in the client terminal.  
ORDER_REASON_SETTLEMENT | 11 | The order was placed as a result of operations connected with the futures/options delivery date coming into effect. It is currently not used. It is currently not used.  
ORDER_REASON_TRANSFER | 12 | Order placed as a result of relocating a position with a calculated price to a new symbol with the same underlying asset. It is currently not used.  
ORDER_REASON_SYNC | 13 | The order was placed while [synchronizing](../../../../Manager-API/Manager-Interface/Trade-Activity/Monitoring-Account-States/TradeAccountSet.md) a trading account with an external system.  
ORDER_REASON_EXTERNAL_SERVICE | 14 | The order was placed from the external trading system for operational purposes (for example, to correct a trading status).  
ORDER_REASON_MIGRATION | 15 | The order was created while importing clients' trading operations from the MetaTrader 4 server.  
ORDER_REASON_MOBILE | 16 | Order created via the MetaTrader 5 mobile terminal for Android or iPhone.  
ORDER_REASON_WEB | 17 | Order created via the web terminal.  
ORDER_REASON_SPLIT | 18 | Order created as a result of a symbol split.  
ORDER_REASON_CORPORATE_ACTION | 19 | Order created as a result of a corporate action, such as consolidating or renaming securities, transferring a client to a different account, etc. API applications set this flag for service operations so that the platform does not account for such corporate actions in commission calculations.  
ORDER_REASON_FIRST |  | Beginning of enumeration. It corresponds to ORDER_REASON_CLIENT.  
ORDER_REASON_LAST |  | End of enumeration. Corresponds to ORDER_REASON_CORPORATE_ACTION.  
  
This enumeration is used in the [IMTOrder::Reason](Reason.md) method.

<a id="entradeactivationflags"></a>
## IMTOrder::EnTradeActivationFlags (#entradeactivationflags)

Types of activation flags that can be assigned to orders during formation of a trade execution (IMTExecution::OrderActivation) are listed in IMTOrder::EnTradeActivationFlags:

ID number | Value | Description  
ACTIV_FLAGS_NO_LIMIT | 0x01 | Do not handle reaching of the Limit level. Only used for orders.  
ACTIV_FLAGS_NO_STOP | 0x02 | Do not handle the reaching of the stop level. Only used for orders.  
ACTIV_FLAGS_NO_SLIMIT | 0x04 | Do not handle reaching of the Stop-Limit level. Only used for orders.  
ACTIV_FLAGS_NO_SL | 0x08 | Do not handle activation upon Stop Loss. Only used for positions.  
ACTIV_FLAGS_NO_TP | 0x10 | Do not handle activation upon Take Profit. Only used for positions.  
ACTIV_FLAGS_NO_SO | 0x20 | Do not handle activation upon Stop-Out. Used for positions and orders.  
ACTIV_FLAGS_NO_EXPIRATION | 0x40 | Do not handle order cancellation upon expiration. Only used for orders.  
ACTIV_FLAGS_NONE | 0x00 | No flags.  
ACTIV_FLAGS_ALL |  | All flags are set.  
  
Flags of orders are inherited by [positions](../../Positions/IMTPosition/ActivationFlags.md) created as a result of their execution. This enumeration is used in the [IMTOrder::ActivationFlags](ActivationFlags.md) method.

<a id="entrademodifyflags"></a>
## IMTOrder::EnTradeModifyFlags (#entrademodifyflags)

IMTOrder::EnTradeModifyFlags lists the flags assigned to orders when they are changed by an administrator, manager or API:

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
ACTIV_FLAGS_ALL |  | All flags are set.  
  
This enumeration is used in the [IMTOrder::ModificationFlags](ModificationFlags.md) method.
