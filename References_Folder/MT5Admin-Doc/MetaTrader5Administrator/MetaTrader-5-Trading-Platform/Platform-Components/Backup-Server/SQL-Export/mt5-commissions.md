[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_commissions

[Previous](mt5-groups-symbols.md) | [Next](mt5-commissions-tiers.md)

# mt5_commissions

[Commission settings for groups](../../../Platform-Setup/Groups/Commission-Settings.md) are exported to this table. The table contains the following fields:

Name | Type | Purpose  
Commission_ID | Integer | Initial key. A unique [commission setting ID (#commissions)](../../../Platform-Setup/Groups/Group-Settings.md#commissions).  
Group_ID | Integer | [ID of the group](mt5-groups.md), a commission setting belongs to.  
Name | String | Commission setting name (up to 64 characters).  
Description | String | Commission setting description (up to 64 characters).  
Path | String | Path to a symbol or a group of symbols covered by a commission setting.  
Mode | Integer | Commission type: 0 — standard, 1 — agent.  
ModeRange | Integer | Commission [levels type (#level)](../../../Platform-Setup/Groups/Commission-Settings.md#level):

  * 0 — volume
  * 1 — turnover in money
  * 2 — turnover in volume

  
ModeCharge | Integer | Commission [charge mode (#charge)](../../../Platform-Setup/Groups/Commission-Settings.md#charge):

  * 0 — daily
  * 1 — monthly
  * 2 — instant

  
TurnoverCurrency | String | Currency, in which the [money turnover (#level)](../../../Platform-Setup/Groups/Commission-Settings.md#level) is calculated.  
ModeEntry | Integer | Commission calculation mode depending on the trade direction:

  * 0 — all trades regardless of direction.
  * 1 — only entry deals.
  * 2 — only exit deals.

  
ModeAction | Integer | Commission calculation mode depending on the trade type:

  * 0 — all trades regardless of type.
  * 1 — only Buy deals.
  * 2 — only Sell deals.

  
ModeProfit | Integer | Commission calculation modes depending on the deal profit:

  * 0 — all deals.
  * 1 — only profitable deals.
  * 2 — only losing deals.

  
ModeReason | Integer | Commission calculation modes depending on the reason for the deal.

  * 0x00000000 — no commission will be charged for any trades.
  * 0x00000001 — the deal was performed by the client manually via the client terminal.
  * 0x00000002 — the deal was performed by the client using an Expert Advisor.
  * 0x00000004 — the deal was performed by a dealer via the Manager terminal.
  * 0x00000008 — the deal was performed from an external trading system.
  * 0x00000010 — the deal was performed via the MetaTrader 5 mobile terminal for Android or iPhone.
  * 0x00000020 — the deal was performed via the web terminal.
  * 0x00000040 — the deal was performed as a result of copying of a trading signal, in accordance with the subscription, in the client terminal.


