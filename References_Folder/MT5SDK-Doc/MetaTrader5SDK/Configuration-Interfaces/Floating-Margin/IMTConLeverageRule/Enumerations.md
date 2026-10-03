[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / Enumerations

[Previous](../IMTConLeverageRule.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConLeverageRule](../IMTConLeverageRule.md) class contains the following enumerations:

  * [IMTConLeverageRule::EnRangeMode (#enrangemode)](Enumerations.md#enrangemode)



<a id="enrangemode"></a>
## IMTConLeverageRule::EnRangeMode (#enrangemode)

IMTConLeverageRule::EnRangeMode contains types of rule levels.

ID | Value | Description  
RANGE_VOLUME |  | Total volume of open positions across all instruments form the [IMTConLeverageRule::Path](Path.md) parameter.  
RANGE_VOLUME_PER_SYMBOL |  | Volume of open positions for each individual instrument from the [IMTConLeverageRule::Path](Path.md) parameter.  
RANGE_VALUE |  | Total value of open positions across all instruments from the [IMTConLeverageRule::Path](Path.md) parameter.  
RANGE_VALUE_PER_SYMBOL |  | Value of open positions for each individual instrument from the [IMTConLeverageRule::Path](Path.md) parameter.  
RANGE_FIRST |  | Enumeration start. Corresponds to RANGE_VOLUME.  
RANGE_LAST |  | Enumeration end. Corresponds to RANGE_VALUE_PER_SYMBOL.  
  
The enumeration is used in the [IMTConLeverageRule::RangeMode](RangeMode.md) method.
