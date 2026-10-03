[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_commissions_tiers

[Previous](mt5-commissions.md) | [Next](mt5-managers.md)

# mt5_commissions_tiers

[Commission levels (#level)](../../../Platform-Setup/Groups/Commission-Settings.md#level) are exported to this table. The table contains the following fields:

Name | Type | Purpose  
Tier_ID | Integer | Initial key. Unique [commission level ID (#level)](../../../Platform-Setup/Groups/Commission-Settings.md#level).  
Commission_ID | Integer | [ID of the commission setting (#commissions)](../../../Platform-Setup/Groups/Group-Settings.md#commissions) the level belongs to.  
Mode | Integer | Commission calculation unit:

  * 0 — account currency
  * 1 — base currency
  * 2 — profit currency
  * 3 — margin currency
  * 4 — points
  * 5 — percentage
  * 6 — specified currency

  
Type | Integer | Commission charge type:

  * 0 — per trade
  * 1 — per volume

  
Value | Float | Commission sum. Commission units depend on the commission calculation method (Mode).  
RangeFrom | Float | The minimum deal volume (turnover), from which the commission will be charged.  
RangeTo | Float | The maximum trade volume (turnover), from which the commission will be charged.  
Minimal | Float | The minimum amount of commission. The value is specified in the group deposit currency.  
Currency | String | Commission calculation currency (if "Specified currency" is selected in the Mode field).
