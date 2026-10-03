[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / Enumerations

[Previous](../IMTConSpread.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

[IMTConSpread](../IMTConSpread.md) class contains the following enumerations:

  * [IMTConSpread::EnSpreadMarginType (#enspreadmargintype)](Enumerations.md#enspreadmargintype)



<a id="enspreadmargintype"></a>
## IMTConSpread::EnSpreadMarginType (#enspreadmargintype)

The modes of margin charging are enumerated in IMTConSpread::EnSpreadMarginType.

ID | Value | Description  
MARGIN_TYPE_VALUE | 0 | When this type is selected, initial and maintenance margin values that will be charged at the specified combination of positions are set in [IMTConSpread::MarginInitial](MarginInitial.md) and [IMTConSpread::MarginMaintenance](MarginMaintenance.md) parameters.  
MARGIN_TYPE_MAXIMAL | 1 | When this type is selected, the values of initial and maintenance margins will be calculated for each spread leg. The calculation is performed by summing up the margin requirements for all symbols of the leg (by [IMTConSymbol::MarginInitial](../../Symbols/IMTConSymbol/MarginInitial.md) and [IMTConSymbol::MarginMaintenace](../../Symbols/IMTConSymbol/MarginMaintenance.md) values or the appropriate values redefined for [client group](../../Groups/IMTConGroupSymbol.md)). The margin requirements of the leg having a greater value will be used for the spread.  
MARGIN_TYPE_CME_INTER | 2 | When this option is selected, ratios (multipliers) for the appropriate margin types should be selected in [IMTConSpread::MarginInitial](MarginInitial.md) and [IMTConSpread::MarginMaintenance](MarginMaintenance.md) parameters. The total margin value will be defined by summing up the margin requirements for all symbols of the spread (by [IMTConSymbol::MarginInitial](../../Symbols/IMTConSymbol/MarginInitial.md) and [IMTConSymbol::MarginMaintenace](../../Symbols/IMTConSymbol/MarginMaintenance.md) values or the appropriate values redefined for [client group](../../Groups/IMTConGroupSymbol.md)) and multiplying the total value by the specified ratio.  
MARGIN_TYPE_CME_INTRA | 3 | When this option is selected, the margin is calculated the following way: the difference between the total margin of A leg symbols and the total margin of B leg symbols is calculated (the difference in absolute magnitude is used, so that it does not matter what leg is a deductible one). According to the type of the calculated margin, the value specified in [IMTConSpread::MarginInitial](MarginInitial.md) and [IMTConSpread::MarginMaintenance](MarginMaintenance.md) parameters is added to the obtained difference.  
MARGIN_TYPE_FIRST |  | Beginning of enumeration. It corresponds to MARGIN_TYPE_VALUE.  
MARGIN_TYPE_LAST |  | End of enumeration. It corresponds to MARGIN_TYPE_CME_INTRA.  
  
This enumeration is used in [IMTConSpread::MarginType](MarginType.md) method.
