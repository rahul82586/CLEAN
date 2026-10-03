[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Enumerations

[Previous](../IMTPosition.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTPosition](../IMTPosition.md) contains the following enumerations:

  * [IMTPosition::EnPositionAction (#enpositionaction)](Enumerations.md#enpositionaction)
  * [IMTPosition::EnActivation (#enactivation)](Enumerations.md#enactivation)
  * [IMTPosition::EnTradeActivationFlags (#entradeactivationflags)](Enumerations.md#entradeactivationflags)
  * [IMTPosition::EnTradeModifyFlags (#entrademodifyflags)](Enumerations.md#entrademodifyflags)
  * [IMTPosition::EnPositionReason (#enpositionreason)](Enumerations.md#enpositionreason)



<a id="enpositionaction"></a>
## IMTPosition::EnPositionAction (#enpositionaction)

Types of positions are listed in IMTPosition::EnPositionAction.

ID number | Value | Description  
POSITION_BUY | 0 | Buy.  
POSITION_SELL | 1 | Sell.  
POSITION_FIRST |  | Beginning of enumeration. It corresponds to POSITION_BUY.  
POSITION_LAST |  | End of enumeration. It corresponds to POSITION_SELL.  
  
This enumeration is used in the [IMTPosition::Action](Action.md) method.

<a id="enactivation"></a>
## IMTPosition::EnActivation (#enactivation)

Types of position activation are listed in the IMTPosition::EnActivation enumeration.

ID number | Value | Description  
ACTIVATION_NONE | 0 | None.  
ACTIVATION_SL | 1 | Stop Loss.  
ACTIVATION_TP | 2 | Take Profit  
ACTIVATION_STOPOUT | 3 | Stop Out.  
ACTIVATION_FIRST |  | Beginning of enumeration. It corresponds to ACTIVATION_NONE.  
ACTIVATION_LAST |  | End of enumeration. Position::Action ACTIVATION_STOPOUT.  
  
This enumeration is used in the [IMTPosition::ActivationMode](ActivationMode.md) method.

<a id="entradeactivationflags"></a>
## IMTPosition::EnTradeActivationFlags (#entradeactivationflags)

Flags of trade position activation are enumerated in IMTPosition::EnTradeActivationFlags:

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
  
Flags of orders are inherited from the [orders (#entradeactivationflags)](../../Orders/IMTOrder/Enumerations.md#entradeactivationflags), as a result of which the position is created. However, they can be overridden using the [IMTPosition::ActivationFlags](ActivationFlags.md) method (for example, when synchronizing a position via a gateway to an external trading system).

<a id="entrademodifyflags"></a>
## IMTPosition::EnTradeModifyFlags (#entrademodifyflags)

IMTPosition::EnTradeModifyFlags contains the flags assigned to positions when they are changed by an administrator, manager or API:

ID number | Value | Description  
MODIFY_FLAGS_ADMIN | 0x00000001 | Position changed by an administrator.  
MODIFY_FLAGS_MANAGER | 0x00000002 | Open price has been modified by a manager.  
MODIFY_FLAGS_POSITION | 0x00000004 | Flag not used for positions.  
MODIFY_FLAGS_RESTORE | 0x00000008 | Position restored.  
MODIFY_FLAGS_API_ADMIN | 0x00000010 | Position modified using the Manager API administrator interface.  
MODIFY_FLAGS_API_MANAGER | 0x00000020 | Position modified using the Manager API manager interface.  
MODIFY_FLAGS_API_SERVER | 0x00000040 | Position modified using the Server API.  
MODIFY_FLAGS_API_GATEWAY | 0x00000080 | Position modified using the Gateway API.  
ACTIV_FLAGS_NONE | 0x00000000 | No flags.  
ACTIV_FLAGS_ALL |  | All flags are set.  
  
This enumeration is used in the [IMTPosition::ModificationFlags](ModificationFlags.md) method.

<a id="enpositionreason"></a>
## IMTPosition::EnPositionReason (#enpositionreason)

Reasons for position opening are enumerated in IMTPosition::EnPositionReason:

ID number | Value | Description  
POSITION_REASON_CLIENT | 0 | Position opened manually by a client from the client terminal.  
POSITION_REASON_EXPERT | 1 | Position opened by a client using an Expert Advisor.  
POSITION_REASON_DEALER | 2 | Position opened by a dealer through the manager terminal.  
POSITION_REASON_SL | 3 | Not used for positions.  
POSITION_REASON_TP | 4  | Not used for positions.  
POSITION_REASON_SO | 5 | Not used for positions.  
POSITION_REASON_ROLLOVER | 6 | Position reopened to charge swaps.  
POSITION_REASON_EXTERNAL_CLIENT | 7 | Position opened from an external trading system.  
POSITION_REASON_VMARGIN | 8 | Position reopened after charging the variation margin.  
POSITION_REASON_GATEWAY | 9 | Position opened by a MetaTrader 5 gateway connected to the platform.  
POSITION_REASON_SIGNAL | 10 | Position opened as a result of copying a [trading signal](https://www.mql5.com/ru/signals "Trading Signals") according to the subscription in the client terminal.  
POSITION_REASON_SETTLEMENT | 11 | Position opened as a result of operations associated with a futures/option delivery date. It is currently not used.  
POSITION_REASON_TRANSFER | 12 | Position opened as a result of transferring a position with a calculated price to a new symbol with the same underlying asset.  
POSITION_REASON_SYNC | 13 | Position opened while [synchronizing](../../../../Manager-API/Manager-Interface/Trade-Activity/Monitoring-Account-States/TradeAccountSet.md) a trading account state with an external system.  
POSITION_REASON_EXTERNAL_SERVICE | 14 | Position opened in the external trading system for service purposes (e.g. to correct a trading state).  
POSITION_REASON_MIGRATION | 15 | Position opened as a result of import of clients' trading operations from the MetaTrader 4 server.  
POSITION_REASON_MOBILE | 16 | Position opened via the MetaTrader 5 mobile terminal for Android or iPhone.  
POSITION_REASON_WEB | 17 | Position opened via the web terminal.  
POSITION_REASON_SPLIT | 18 | Position opened as a result of a symbol split.  
POSITION_REASON_CORPORATE_ACTION | 19 | Position created as a result of a corporate action, such as consolidating or renaming securities, transferring a client to a different account, etc. API applications set this flag for service operations so that the platform does not account for such corporate actions in commission calculations.  
POSITION_REASON_FIRST |  | Beginning of enumeration. Corresponds to POSITION_REASON_CLIENT.  
POSITION_REASON_LAST |  | End of enumeration. Corresponds to POSITION_REASON_CORPORATE_ACTION.  
  
This enumeration is used in the [IMTPosition::Reason](Reason.md) method.
