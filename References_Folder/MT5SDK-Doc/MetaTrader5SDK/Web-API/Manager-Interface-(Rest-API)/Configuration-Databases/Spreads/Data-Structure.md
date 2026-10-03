[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / Data Structure

[Previous](../Spreads.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

A spread configuration is passed in JSON format in response to the [/api/spread/add](Add.md) and [/api/spread/next](Get-by-Index.md) requests.

Parameter | Type | Purpose  
ID | Integer | Spread configuration identifier.  
Flags | Integer | Spread configuration flags. Currently not used.  
MarginInitial | Float | Parameter value for setting the initial margin.  
MarginMaintenance | Float | Parameter value of for setting the maintenance margin.  
MarginType | Integer | Margin charging type. Passed as a value of the [EnSpreadMarginType (#enspreadmargintype)](../../../../Configuration-Interfaces/Spreads/IMTConSpread/Enumerations.md#enspreadmargintype) enumeration.  
ALegAdd | Object | [Spread A leg (#leg)](Data-Structure.md#leg).  
BLegAdd | Object | [Spread B leg (#leg)](Data-Structure.md#leg).  
  
Spread leg

Parameter | Type | Purpose  
Mode | Integer | Method for specifying symbols for a spread leg. Passed as a value of the [EnLegMode (#enlegmode)](../../../../Configuration-Interfaces/Spreads/IMTConSpreadLeg/Enumerations.md#enlegmode) enumeration.  
Flags | Integer | Spread leg flags. Currently not used.  
Symbol | String | Symbol or basic asset for a spread leg.  
TimeFrom | Integer | The beginning of the period for filtering symbols by expiration time when specifying a basic asset for a spread leg.  
TimeTo | Integer | The end of the period for filtering symbols by expiration time when specifying a basic asset for a spread leg.  
Ratio | Float | The weight of the specified symbol.
