[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / Data Structure

[Previous](../Floating-Margin.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Floating margin configuration is passed in JSON format in response to the following requests: [/api/leverage/add](Add.md), [/api/leverage/next](Get-by-Index.md), and [/api/leverage/get](Get-by-Name.md).

<a id="leverage"></a>
## Configuration parameters (#leverage)

The floating margin configuration includes the following parameters:

Parameter | Type | Description  
Name | String | Name of the floating margin configuration.  
Rules | Array of objects | Array of [rules (#rule)](Data-Structure.md#rule).  
  
<a id="rule"></a>
## Rule parameters (#rule)

Rule parameters are passed in an array inside the [Rules (#rule)](Data-Structure.md#rule) parameter of the configuration.

Parameter | Type | Description  
Name | String | Name of the rule in the floating margin configuration.  
Description | String | Descriptions of the rule in the floating margin configuration.  
Path | String | Path to a symbol or group of symbols for which the floating margin rule is applied.  
RangeMode | Integer | Level type for a rule in a floating margin configuration.  
RangeCurrency | String | The currency to which the notional value of positions in [IMTConLeverageRule::RANGE_VALUE* (#enrangemode)](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageRule/Enumerations.md#enrangemode) modes is converted.  
RangeCurrencyDigits | Integer | Number of decimal places for RangeCurrency currency values.  
Tiers | Array of objects | Array of [levels (#tier)](Data-Structure.md#tier).  
  
<a id="tier"></a>
## Level parameters (#tier)

Level parameters are passed in an array inside the [Tiers (#rule)](Data-Structure.md#rule) parameter of the rule.

Parameter | Type | Description  
RangeFrom | Float | The minimum range value for the level in the floating margin rule.  
RangeTo | Float | The maximum range value for the level in the floating margin rule.  
MarginRateInitial | Float | Initial margin rate for the level in the floating margin rule.  
MarginRateMaintenance | Float | Maintenance margin rate for the level in the floating margin rule.
