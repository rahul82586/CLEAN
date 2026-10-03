[🏠 Document Start](../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../../Platform-Components.md) / [Backup Server](../../../Backup-Server.md) / [SQL Export](../../SQL-Export.md) / [mt5_deals](../mt5-deals.md) / Enumerations

[Previous](../mt5-deals.md) | [Next](../mt5-accounts.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

To pass information about deals the following enumerations are used:

  * [EnDealAction (#endealaction)](Enumerations.md#endealaction)
  * [EnEntryFlags (#enentryflags)](Enumerations.md#enentryflags)
  * [EnDealReason (#endealreason)](Enumerations.md#endealreason)



<a id="endealaction"></a>
## EnDealAction (#endealaction)

Types of actions performed by a deal are enumerated in EnDealAction.

ID number | Value | Description  
DEAL_BUY | 0 | A Buy deal.  
DEAL_SELL | 1 | A Sell deal.  
DEAL_BALANCE | 2 | Balance operation.  
DEAL_CREDIT | 3 | Credit operation.  
DEAL_CHARGE | 4 | Additional charges/withdrawals.  
DEAL_CORRECTION | 5 | Correcting operations.  
DEAL_BONUS | 6 | Bonuses.  
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
DEAL_AGENT | 18 | Charging an agent commission. Used in case of an instant commission charge to an agent (every time the agent's client performs a deal).  
DEAL_SO_COMPENSATION | 19 | An operation connected with the [compensation of a negative account (#compensate)](../../../../Platform-Setup/Groups/Group-Settings.md#compensate) after the Stop Out event.  
DEAL_SO_COMPENSATION_CREDIT | 20 | [Withdrawing credit funds (#so-credit)](../../../../Platform-Setup/Groups/Group-Settings.md#so-credit) after a negative balance compensation operation.  
  
<a id="enentryflags"></a>
## EnEntryFlags (#enentryflags)

Types of actions performed by a deal with respect to positions are enumerated in EnEntryFlags.

ID number | Value | Description  
ENTRY_IN | 0 | Entering the market or adding the volume.  
ENTRY_OUT | 1 | Exit from the market or partial closure.  
ENTRY_INOUT | 2 | Reversal.  
ENTRY_OUT_BY | 3 | Close by — a simultaneous closure of two opposite positions of the sane financial instrument. This operation type is only used in the [hedging mode (#hedging)](../../../../Platform-Setup/Groups/Position-Accounting-Systems.md#hedging).  
  
<a id="endealreason"></a>
## EnDealReason (#endealreason)

Types of reasons for order placing are listed in EnDealReason.

ID number | Value | Description  
DEAL_REASON_CLIENT | 0 | Deal performed by a client manually through the client terminal.  
DEAL_REASON_EXPERT | 1 | Deal performed by a client with using an Expert Advisor.  
DEAL_REASON_DEALER | 2 | Deal performed by a dealer through the manager terminal.  
DEAL_REASON_SL | 3 | Deal performed as a result of Stop Loss activation.  
DEAL_REASON_TP | 4 | Deal performed as a result of Take Profit activation.  
DEAL_REASON_SO | 5 | Deal performed when the client reached the Stop-Out level.  
DEAL_REASON_ROLLOVER | 6 | Deal performed when reopening a position for charging swaps.  
DEAL_REASON_EXTERNAL_CLIENT | 7 | Deal performed by a client from an external trading system. For this type of deals the commission is charged as distinct from DEAL_REASON_EXTERNAL_SERVICE.  
DEAL_REASON_VMARGIN | 8 | Deal performed for accruing variation margin.  
DEAL_REASON_GATEWAY | 9 | Deal performed by a MetaTrader 5 gateway that had connected to the trading platform.  
DEAL_REASON_SIGNAL | 10 | Deal performed as a result of copying [a trade signal](https://www.mql5.com/en/signals "Trading signals") according to a subscription in the client terminal.  
DEAL_REASON_SETTLEMENT | 11 | Deal performed to compulsory close a position due to the settlement of a futures contract/option.  
DEAL_REASON_TRANSFER | 12 | Deal performed due to transferring a position at the settlement price to a new symbol with the same underlying asset.  
DEAL_REASON_SYNC | 13 | Deal performed as a result of synchronization of an account's trade state with an external system.  
DEAL_REASON_EXTERNAL_SERVICE | 14 | Deal performed from an external trading system for technical reasons (for example, to correct the trade state of a client). For this type of deals the commission is not charged.  
DEAL_REASON_MIGRATION | 15 | Deal created as a result of importing trade operations from a MetaTrader 4 server.  
DEAL_REASON_MOBILE | 16 | The deal is conducted via the MetaTrader 5 mobile terminal for Android or iPhone.  
DEAL_REASON_WEB | 17 | The deal is conducted via the web terminal.  
DEAL_REASON_SPLIT | 18 | The deal is conducted as a result of a symbol split.  
DEAL_REASON_CORPORATE_ACTION | 19 | The deal is created as a result of a corporate action, such as consolidating or renaming securities, transferring a client to a different account, etc. API applications set this flag for service operations so that the platform does not account for such corporate actions in commission calculations.
