[🏠 Document Start](../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../../Platform-Components.md) / [Backup Server](../../../Backup-Server.md) / [SQL Export](../../SQL-Export.md) / [mt5_positions](../mt5-positions.md) / Enumerations

[Previous](../mt5-positions.md) | [Next](../mt5-deals.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

To pass information about positions the following enumerations are used:

  * [EnPositionAction (#enpositionaction)](Enumerations.md#enpositionaction)
  * [EnActivation (#enactivation)](Enumerations.md#enactivation)
  * [EnTradeActivationFlags (#entradeactivationflags)](Enumerations.md#entradeactivationflags)
  * [EnPositionReason (#enpositionreason)](Enumerations.md#enpositionreason)



<a id="enpositionaction"></a>
## EnPositionAction (#enpositionaction)

Types of positions are listed in EnPositionAction.

ID number | Value | Description  
POSITION_BUY | 0 | Buy.  
POSITION_SELL | 1 | Sell.  
  
<a id="enactivation"></a>
## EnActivation (#enactivation)

Types of position activation are listed in the EnActivation enumeration.

ID number | Value | Description  
ACTIVATION_NONE | 0 | None.  
ACTIVATION_SL | 1 | Stop Loss.  
ACTIVATION_TP | 2 | Take Profit  
ACTIVATION_STOPOUT | 3 | Stop Out.  
  
<a id="entradeactivationflags"></a>
## EnTradeActivationFlags (#entradeactivationflags)

Flags of trade position activation are listed in the EnTradeActivationFlags enumeration:

ID number | Value | Description  
ACTIV_FLAGS_NO_LIMIT | 0x01 | Do not handle reaching of the Limit level.  
ACTIV_FLAGS_NO_STOP | 0x02 | Do not handle the reaching of the stop level.  
ACTIV_FLAGS_NO_SLIMIT | 0x04 | Do not handle reaching of the Stop-Limit level.  
ACTIV_FLAGS_NO_SL | 0x08 | Do not handle activation upon Stop Loss.  
ACTIV_FLAGS_NO_TP | 0x10 | Do not handle activation upon Take Profit.  
ACTIV_FLAGS_NO_SO | 0x20 | Do not handle activation upon Stop-Out.  
ACTIV_FLAGS_NO_EXPIRATION | 0x40 | Do not handle order cancellation upon expiration.  
ACTIV_FLAGS_NONE | 0x00 | No flags.  
  
Activation flags are inherited from the [orders](../mt5-orders.md), as a result of which the position is created.

<a id="enpositionreason"></a>
## EnPositionReason (#enpositionreason)

Reasons for position opening are enumerated in EnPositionReason:

ID number | Value | Description  
POSITION_REASON_CLIENT | 0 | Position opened manually by a client from the client terminal.  
POSITION_REASON_EXPERT | 1 | Position opened by a client using an Expert Advisor.  
POSITION_REASON_DEALER | 2 | Position opened by a dealer through the manager terminal.  
POSITION_REASON_SL | 3 | Not used for positions.  
POSITION_REASON_TP | 4  | Not used for positions.  
POSITION_REASON_SO | 5 | Not used for positions.  
POSITION_REASON_ROLLOVER | 6 | Position reopened to charge swaps.  
POSITION_REASON_EXTERNAL_CLIENT | 7 | Position opened from an external trading system.  
POSITION_REASON_VMARGIN | 8 | Not used for positions.  
POSITION_REASON_GATEWAY | 9 | Position opened by a MetaTrader 5 gateway connected to the platform.  
POSITION_REASON_SIGNAL | 10 | Position opened as a result of copying a [trading signal](https://www.mql5.com/en/signals "Trading Signals") according to the subscription in the client terminal.  
POSITION_REASON_SETTLEMENT | 11 | Position opened as a result of operations associated with a futures/option delivery date. It is currently not used.  
POSITION_REASON_TRANSFER | 12 | Position opened as a result of transferring a position with a calculated price to a new symbol with the same underlying asset.  
POSITION_REASON_SYNC | 13 | Position opened while synchronizing a trading account state with an external system.  
POSITION_REASON_EXTERNAL_SERVICE | 14 | Position opened in the external trading system for service purposes (e.g. to correct a trading state).  
POSITION_REASON_MIGRATION | 15 | Position opened as a result of import of clients' trading operations from the MetaTrader 4 server.  
POSITION_REASON_MOBILE | 16 | Position opened via the MetaTrader 5 mobile terminal for Android or iPhone.  
POSITION_REASON_WEB | 17 | Position opened via the web terminal.  
POSITION_REASON_SPLIT | 18 | Position opened as a result of a symbol split.  
POSITION_REASON_CORPORATE_ACTION | 19 | Position created as a result of a corporate action, such as consolidating or renaming securities, transferring a client to a different account, etc. API applications set this flag for service operations so that the platform does not account for such corporate actions in commission calculations.
