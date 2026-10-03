[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / Data Structure

[Previous](../Routing.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

A routing configuration is passed in JSON format in response to the [/api/route/add](Add.md), [/api/route/next](Get-by-Index.md) and [/api/route/get](Get-by-Name.md) requests.

Parameter | Type | Purpose  
Name | String | The name of a routing rule.  
Mode | Integer | The state of the routing rule. Passed as a value of the [EnRouteMode (#enroutemode)](../../../../Configuration-Interfaces/Routing/IMTConRoute/Enumerations.md#enroutemode)enumeration.  
Request | Integer | Types of requests for which the rule is applicable. Passed as a value of the [EnRouteFlags (#enrouteflags)](../../../../Configuration-Interfaces/Routing/IMTConRoute/Enumerations.md#enrouteflags) enumeration.  
Type | Integer | Types of orders for which the rule is applicable. Passed as a value of the [EnTypeFlags (#entypeflags)](../../../../Configuration-Interfaces/Routing/IMTConRoute/Enumerations.md#entypeflags) enumeration.  
Flags | Integer | Rule flags. Currently not used.  
Action | Integer | The type of action that is applied to a request in accordance with the rule. Passed as a value of the [EnRouteAction (#enrouteaction)](../../../../Configuration-Interfaces/Routing/IMTConRoute/Enumerations.md#enrouteaction) enumeration.  
ActionValueInt | Integer | The value of an additional parameter of INT type.  
ActionValueUInt | Integer | The value of an additional parameter of UINT type.  
ActionValueFloat | Float | The value of an additional parameter of double type.  
ActionValueString | String | The value of an additional parameter of string type.  
Conditions | Array | [Additional conditions (#conditions)](Data-Structure.md#conditions) for rule triggering.  
Dealers | Array | [Dealers (#dealers)](Data-Structure.md#dealers) to whom requests under the conditions of this rule will be sent for processing.  
  
<a id="conditions"></a>
## Additional conditions (#conditions)

Parameter | Type | Purpose  
Condition | Integer | The type of the additional condition for the rule. Passed as a value of the [EnRouteCondition (#enroutecondition)](../../../../Configuration-Interfaces/Routing/IMTConCondition/Enumerations.md#enroutecondition) enumeration.  
Rule | Integer | A method for comparing a condition with the specified value. Passed as a value of the [EnConditionRule (#enconditionrule)](../../../../Configuration-Interfaces/Routing/IMTConCondition/Enumerations.md#enconditionrule) enumeration.  
ValueInt | Integer | Condition value of INT type.  
ValueUInt | Integer | Condition value of UINT type.  
ValueDouble | Float | Condition value of double type.  
ValueString | String | Condition value of string type.  
  
<a id="dealers"></a>
## Dealers (#dealers)

Parameter | Type | Purpose  
Login | Integer  | The login of the dealer to whom requests under this rule will be sent.  
Name | String | The name of the dealer to whom requests under this rule will be sent.
