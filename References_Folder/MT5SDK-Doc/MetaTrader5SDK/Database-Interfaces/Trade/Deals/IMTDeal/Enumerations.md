[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Enumerations

[Previous](../IMTDeal.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTDeal](../IMTDeal.md) contains the following enumerations:

  * [IMTDeal::EnDealAction (#endealaction)](Enumerations.md#endealaction)
  * [IMTDeal::EnDealEntry (#endealentry)](Enumerations.md#endealentry)
  * [IMTDeal::EnDealReason (#endealreason)](Enumerations.md#endealreason)
  * [IMTDeal::EnTradeModifyFlags (#entrademodifyflags)](Enumerations.md#entrademodifyflags)



<a id="endealaction"></a>
## IMTDeal::EnDealAction (#endealaction)

Types of actions performed by a deal are enumerated in IMTDeal::EnDealAction.

ID number | Value | Description  
DEAL_BUY | 0 | A Buy deal.  
DEAL_SELL | 1 | A Sell deal.  
DEAL_BALANCE | 2 | A balance operation.  
DEAL_CREDIT | 3 | Credit operation.  
DEAL_CHARGE | 4  | Additional charges/withdrawals.  
DEAL_CORRECTION | 5 | Correcting operations.  
DEAL_BONUS | 6 | Bonuses. Operations of this type affect the credit assets of a client ([IMTUser::Credit](../../../Users/IMTUser/Credit.md)).  
DEAL_COMMISSION | 7 | Commission.  
DEAL_COMMISSION_DAILY | 8 | Daily commission.  
DEAL_COMMISSION_MONTHLY | 9 | Monthly commission.  
DEAL_AGENT_DAILY | 10 | Daily agent commission.  
DEAL_AGENT_MONTHLY | 11 | Daily agent commission.  
DEAL_INTERESTRATE | 12 | Accrual of annual interest.  
DEAL_BUY_CANCELED | 13 | A canceled Buy deal. Using the IMTExecution::TE_DEAL_CANCEL trade execution, the Gateway API can notify the platform about the cancellation of a previously executed deal in the external trading system. In this case the type of the earlier executed Buy trade is replaced with this one. The profit/loss of a trade is cleared. Then the client's position is recalculated and the appropriate profit/loss is added/subtracted as a separate balance operation. Deal cancellation does not change the client's order history. Deal cancellation does not entail changes in client's orders history. A deal of the DEAL_BUY_CANCELED type is not included into the calculation of the financial state of account and is not taken into account in recalculated positions.  
DEAL_SELL_CANCELED | 14 | A canceled Sell deal. Using the IMTExecution::TE_DEAL_CANCEL trade execution, the Gateway API can notify the platform about the cancellation of a previously executed deal in the external trading system. In this case the type of the earlier executed Buy trade is replaced with this one. The profit/loss of a trade is cleared. Then the client's position is recalculated and the appropriate profit/loss is added/subtracted as a separate balance operation. Deal cancellation does not change the client's order history. Deal cancellation does not entail changes in client's orders history. A deal of the DEAL_SELL_CANCELED type is not included into the calculation of the financial state of account and is not taken into account in recalculated positions.  
DEAL_DIVIDEND | 15 | Dividend operations.  
DEAL_DIVIDEND_FRANKED | 16 | Franked (non-taxable) dividend operations (tax is paid by a company, not a client).  
DEAL_TAX | 17 | Charging a tax.  
DEAL_AGENT | 18 | Charging an agent commission. Used during an instant commission charge to an agent (each time the agent's client performs a deal).  
DEAL_SO_COMPENSATION | 19 | An operation connected with the compensation of a negative account after the Stop Out event ([IMTConGroup::TRADEFLAGS_SO_COMPENSATION (#entradeflags)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#entradeflags)).  
DEAL_SO_COMPENSATION_CREDIT | 20 | Withdrawing credit funds after a negative balance compensation operation ([IMTConGroup::TRADEFLAGS_SO_COMPENSATION_CREDIT (#entradeflags)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#entradeflags)).  
DEAL_FIRST |  | Beginning of enumeration. It corresponds to DEAL_BUY.  
DEAL_LAST |  | End of enumeration. Corresponds to DEAL_SO_COMPENSATION.  
  
This enumeration is used in the [IMTDeal::Action](Action.md) method.

<a id="endealentry"></a>
## IMTDeal::EnDealEntry (#endealentry)

Types of actions performed by a deal relative to positions are enumerated in IMTDeal::EnDealEntry.

ID number | Value | Description  
ENTRY_IN | 0 | Entering the market or adding the volume.  
ENTRY_OUT | 1 | Exit from the market or partial closure.  
ENTRY_INOUT | 2 | The deal that closed an existing position and opened a new one in the opposite direction. It is only used with the netting position accounting system ([EnMarginMode::MARGIN_MODE_RETAIL (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode) or [EnMarginMode::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)). For example, if there is a Buy 1.0 EURUSD position, a counter trade Sell 3.0 EURUSD is executed. In this case, the trader will receive one final Sell 2.0 EURUSD position, which is the opposite to the previously existing. The position ticket does not change in this case.  
ENTRY_OUT_BY | 3 | Close by — a simultaneous closure of two opposite positions of the sane financial instrument. This operation type is only used in the hedging mode ([EnMarginMode::MARGIN_MODE_RETAIL_HEDGED (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).  
ENTRY_FIRST |  | Beginning of enumeration. Corresponds to ENTRY_IN.  
ENTRY_LAST |  | End of enumeration. Corresponds to ENTRY_OUT_BY.  
  
This enumeration is used in the [IMTDeal::Entry](Entry.md) method.

<a id="endealreason"></a>
## IMTDeal::EnDealReason (#endealreason)

The reasons for transaction are listed in IMTDeal::EnDealReason:

ID number | Value | Description  
DEAL_REASON_CLIENT | 0 | The deal is conducted by a client manually through the client terminal.  
DEAL_REASON_EXPERT | 1 | The deal is conducted by a client using an Expert Advisor.  
DEAL_REASON_DEALER | 2 | The deal is conducted by a dealer through the manager terminal.  
DEAL_REASON_SL | 3 | The deal is conducted as a result of Stop Loss activation.  
DEAL_REASON_TP | 4  | The deal is conducted as a result of Take Profit activation.  
DEAL_REASON_SO | 5 | The deal is conducted when the client reached the Stop-Out level.  
DEAL_REASON_ROLLOVER | 6 | The deal is conducted when reopening a position for charging swaps.  
DEAL_REASON_EXTERNAL_CLIENT | 7 | The deal is conducted from an external trading system. As opposed to DEAL_REASON_EXTERNAL_SERVICE, commission is charged in this type of deal.  
DEAL_REASON_VMARGIN | 8 | The deal is conducted to charge the variation margin.  
DEAL_REASON_GATEWAY | 9 | The deal is conducted by a MetaTrader 5 gateway connected to the platform.  
DEAL_REASON_SIGNAL | 10 | The deal is conducted as a result of copying a [trading signal](https://www.mql5.com/ru/signals "Trading Signals")according to the subscription in the client terminal.  
DEAL_REASON_SETTLEMENT | 11 | Forced closing of a position due to a futures/option delivery date coming into effect.  
DEAL_REASON_TRANSFER | 12 | The deal is conducted as a result of relocating a position with a calculated price to a new symbol with the same underlying asset.  
DEAL_REASON_SYNC | 13 | The deal is conducted while [synchronizing](../../../../Manager-API/Manager-Interface/Trade-Activity/Monitoring-Account-States/TradeAccountSet.md) a trading account with an external system.  
DEAL_REASON_EXTERNAL_SERVICE | 14 | Deal performed from an external trading system for technical reasons (for example, to correct the trade state of a client). Commission is not charged on this type of deals.  
DEAL_REASON_MIGRATION | 15 | The deal is created while importing clients' trading operations from the MetaTrader 4 server.  
DEAL_REASON_MOBILE | 16 | The deal is conducted via the MetaTrader 5 mobile terminal for Android or iPhone.  
DEAL_REASON_WEB | 17 | The deal is conducted via the web terminal.  
DEAL_REASON_SPLIT | 18 | The deal is conducted as a result of a symbol split.  
DEAL_REASON_CORPORATE_ACTION | 19 | The deal is created as a result of a corporate action, such as consolidating or renaming securities, transferring a client to a different account, etc. API applications set this flag for service operations so that the platform does not account for such corporate actions in commission calculations.  
DEAL_REASON_FIRST |  | Beginning of enumeration. It corresponds to DEAL_REASON_CLIENT.  
DEAL_REASON_LAST |  | End of enumeration. Corresponds to DEAL_REASON_CORPORATE_ACTION.  
  
The enumeration is used in the [IMTDeal::Reason](Reason.md) method.

<a id="entrademodifyflags"></a>
## IMTDeal::EnTradeModifyFlags (#entrademodifyflags)

IMTDeal::EnTradeModifyFlags contains flags that can be assigned to deals modified by an administrator, a manager or API:

ID number | Value | Description  
MODIFY_FLAGS_ADMIN | 0x00000001 | The deal has been modified by an administrator.  
MODIFY_FLAGS_MANAGER | 0x00000002 | Open price has been modified by a manager.  
MODIFY_FLAGS_POSITION | 0x00000004 | The flag means that deal modification flags have been [inherited](ModificationFlags.md) from the position, which was closed by the deal.  
MODIFY_FLAGS_RESTORE | 0x00000008 | The deal has been restored.  
MODIFY_FLAGS_API_ADMIN | 0x00000010 | The deal has been modified using the administrator interface of the Manager API.  
MODIFY_FLAGS_API_MANAGER | 0x00000020 | The deal has been modified using the manager interface of the Manager API.  
MODIFY_FLAGS_API_SERVER | 0x00000040 | The deal has been modified using the Server API.  
MODIFY_FLAGS_API_GATEWAY | 0x00000080 | The deal has been modified using the Gateway API.  
ACTIV_FLAGS_NONE | 0x00000000 | No flags.  
ACTIV_FLAGS_ALL |  | All flags are set.  
  
The enumeration is used in the [IMTDeal::ModificationFlags](ModificationFlags.md) method.
