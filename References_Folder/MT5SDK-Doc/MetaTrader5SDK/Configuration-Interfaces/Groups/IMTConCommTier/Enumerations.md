[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / Enumerations

[Previous](../IMTConCommTier.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConCommTier](../IMTConCommTier.md) class cintains two enumerations.

<a id="encommissionmode"></a>
## IMTConCommTier::EnCommissionMode (#encommissionmode)

Commission charging methods are listed in IMTConCommTier::EnCommissionMode.

ID | Value | Description  
COMM_MONEY_DEPOSIT | 0 | Money, in the group deposit currency.  
COMM_MONEY_SYMBOL_BASE | 1 | Money, in the base currency of the symbol.  
COMM_MONEY_SYMBOL_PROFIT | 2 | Money, in the symbol profit currency.  
COMM_MONEY_SYMBOL_MARGIN | 3 | Money, in the symbol margin currency.  
COMM_PIPS | 4  | In pips.  
COMM_PERCENT | 5 | Percent from the real price of the deal /overturn. The real price is calculated in base currency of the symbol as the product of its volume, contract size and price (and Tick price/Tick size ratio for Futures). By default, the trade/turnover value calculated in the base currency is converted to the [group deposit currency](../IMTConGroup/Currency.md), and the final commission (the specified percentage) is calculated based on this value. The currency to which the trade/turnover value is converted, can be overridden using the [IMTConCommission::TurnoverCurrency](../IMTConCommission/TurnoverCurrency.md) property. For example, the price of Buy 1 lot EURUSD with a contract size of 100,000 is 100,000 EUR. If the client's deposit currency is USD, the position price is converted at EURUSD rate as of the time of the trade execution. If a specific currency is specified in the Currency field, e.g. AUD, then the value of this position will be converted to Australian dollars at the EURAUD rate. Commission (percent) will be calculated from the resulting value. Further, this value will be converted to the group deposit currency and deducted from the client.  
COMM_MONEY_SPECIFIED | 6 | Money, in the specified currency. The currency is specified in the [IMTConCommTier::Currency](Currency.md) field.  
COMM_PERCENT_PROFIT | 7 | The commission will be calculated as a percentage of the deal profit (if charged instantly) or of the trader's total profit for the day or month (if charged at the end of the day or month). In case of a loss, the corresponding commission value will not be debited from the trader, but will be credited to the trader's account instead. To avoid such charges, set the [minimum commission size](Minimal.md) to 0 and/or set the filter by [deal profit](../IMTConCommission/ProfitMode.md).  
COMM_FIRST |  | Beginning of enumeration. It corresponds to COMM_MONEY_DEPOSIT.  
COMM_LAST |  | End of enumeration. Corresponds to COMM_PERCENT_PROFIT.  
  
> After calculation, the commission amount is converted to the [group deposit currency](../IMTConGroup/Currency.md).

<a id="this-enumeration-is-used-in-the-imtconcommtiermodemodemd-method"></a>
## This enumeration is used in the [IMTConCommTier::Mode](Mode.md) method. (#this-enumeration-is-used-in-the-imtconcommtiermodemodemd-method)

<a id="encommissionvolumetype"></a>
## IMTConCommTier::EnCommissionVolumeType (#encommissionvolumetype)

Commission charging types depending in the trade volume are listed in IMTConCommTier::EnCommissionVolumeType.

ID | Value | Description  
COMM_TYPE_DEAL | 0 | Commission from a deal.  
COMM_TYPE_VOLUME | 1 | Commission from a volume.  
COMM_TYPE_FIRST |  | Beginning of enumeration. It corresponds to COMM_TYPE_DEAL.  
COMM_TYPE_LAST |  | End of enumeration. It corresponds to COMM_TYPE_VOLUME.  
  
<a id="this-enumeration-is-used-in-the-imtconcommtiertypetypemd-method"></a>
## This enumeration is used in the [IMTConCommTier::Type](Type.md) method. (#this-enumeration-is-used-in-the-imtconcommtiertypetypemd-method)
