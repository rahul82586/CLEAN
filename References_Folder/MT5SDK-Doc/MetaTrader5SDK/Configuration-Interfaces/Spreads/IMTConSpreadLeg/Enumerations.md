[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadLeg](../IMTConSpreadLeg.md) / Enumerations

[Previous](../IMTConSpreadLeg.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The class contains the following enumerations:

  * [IMTConSpreadleg::EnLegMode (#enlegmode)](Enumerations.md#enlegmode)



<a id="enlegmode"></a>
## IMTConSpreadLeg::EnLegMode (#enlegmode)

Symbol specification methods for a spread leg are listed in IMTConSpreadLeg::EnLegMode.

ID | Value | Description  
LEG_MODE_SYMBOL | 0 | Specifying trade symbols for a spread leg as a specific symbol.  
LEG_MODE_FUTURES | 1 | Specifying trade symbols for a spread leg as a basic asset. If a basic asset is specified for the leg, all symbols with this basic asset are considered ([IMTConSymbol::Basis](../../Symbols/IMTConSymbol/Basis.md) field). In this case, symbols can be additionally filtered by the time of their operation (specified in [IMTConSymbol::TimeStart](../../Symbols/IMTConSymbol/TimeStart.md) and [IMTConSymbol::TimeExpiration](../../Symbols/IMTConSymbol/TimeExpiration.md)). To do this, specify the time interval in [IMTConSpreadLeg::TimeFrom](TimeFrom.md) and [IMTConSpreadLeg::TimeTo](TimeTo.md). To be able to use the symbol, its expiration date ([IMTConSymbol::TimeExpiration](../../Symbols/IMTConSymbol/TimeExpiration.md)) should be in the specified interval.  
LEG_MODE_FIRST |  | Beginning of enumeration. It corresponds to LEG_MODE_SYMBOL.  
LEG_MODE_LAST |  | End of enumeration. It corresponds to LEG_MODE_FUTURES.  
  
This enumeration is used in [IMTConSpreadLeg::Mode](Mode.md) method.
