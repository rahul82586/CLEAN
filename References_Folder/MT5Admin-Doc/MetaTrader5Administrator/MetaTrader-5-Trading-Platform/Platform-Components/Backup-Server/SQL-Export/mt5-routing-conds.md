[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_routing_conds

[Previous](mt5-routing-dealers.md) | [Next](mt5-feeders.md)

# mt5_routing_conds

Data about [additional conditions (#condition)](../../../Platform-Setup/Routing/Actions-and-Conditions.md#condition) specified in a routing rule is exported to this table.

Name | Type | Description  
Condition_ID | Integer | The unique identifier of the condition.  
Name | String | The name of the routing rule to which the additional condition applies.  
Condition | Integer | The type of the additional condition for the rule. Passed using the [EnRouteCondition (#enroutecondition)](mt5-routing/Enumerations.md#enroutecondition) enumeration.  
Rule | Integer | A method for comparing a condition with the specified value. Passed using the [EnConditionRule (#enconditionrule)](mt5-routing/Enumerations.md#enconditionrule) enumeration.  
Type | Integer | The type of value of the additional condition for a routing rule. Based on this field, it is possible to determine the field in which the Condition value is contained: ValueInt, ValueUInt, ValueFloat or ValueString. Possible values:

  * 0 — the current parameter does not have values (currently not used)
  * 1 — the value is located in the ValueString field, and its type is string
  * 2 — the value is located in the ValueInt field, and its type is int
  * 3 — the value is located in the ValueUInt field, and its type is uint
  * 4 — the value is located in the ValueFloat field, and its type is float

  
ValueInt | Integer | An int value for the condition.  
ValueUInt | Integer | An uint value for the condition.  
ValueUInt | Integer | An uint value for the condition. Used for volume with extended accuracy.  
ValueFloat | Float | A float value for the condition.  
ValueString | String | A float value for the condition. For example, for the "Symbols" condition, the names of symbol (symbol groups) will be specified in this field.
