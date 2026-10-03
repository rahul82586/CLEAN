[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_routing

[Previous](mt5-firewall.md) | [Next](mt5-routing/Enumerations.md)

# mt5_routing

Data about trade request [routing rules](../../../Platform-Setup/Routing.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Name | String | The name of a routing rule.  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has been changed.  
Mode | Integer | The state of a routing rule: 0 — disabled, 1 — enabled.  
Request | Integer | Types of requests for which the rule is applicable. The types are passed using the [EnRouteFlags (#enrouteflags)](mt5-routing/Enumerations.md#enrouteflags) enumeration (as a sum of flags).  
Type | Integer | Types of orders for which the rule is applicable. The types are passed using the [EnTypeFlags (#entypeflags)](mt5-routing/Enumerations.md#entypeflags) enumeration (as a sum of flags).  
Flags | Integer | Currently not used.  
ActionType | Integer | The value type for Action. Based on this field, it is possible to determine the field in which the Action value is contained: ActionValueInt, ActionValueUInt, ActionValueFloat or ActionValueString. Possible values:

  * 0 — the current parameter does not have values (for example, [ACTION_CLEAR_TP (#enrouteaction)](mt5-routing/Enumerations.md#enrouteaction))
  * 1 — the value is located in the ActionValueString field, and its type is string
  * 2 — the value is located in the ActionValueInt field, and its type is int
  * 3 — the value is located in the UInt field, and its type is uint
  * 4 — the value is located in the ActionValueFloat field, and its type is float

  
Action | Integer | The type of action that is applied to a request in accordance with a rule. Passed as a value of the [EnRouteAction (#enrouteaction)](mt5-routing/Enumerations.md#enrouteaction) enumeration.  
ActionValueInt | Integer | An int value for the action applied to the rule. For example, for the rule "pass to online dealers", the 0 value means that the additional option "skip this rule if no dealers online" is disabled.  
ActionValueUInt | Integer | An uint value for the action applied to the rule.  
ActionValueFloat | Fraction | A float value for the action applied to the rule.  
ActionValueString | String | A string value for the action applied to the rule.
