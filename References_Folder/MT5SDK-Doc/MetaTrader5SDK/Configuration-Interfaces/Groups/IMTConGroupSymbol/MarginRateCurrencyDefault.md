[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginRateCurrencyDefault

[Previous](MarginRateCurrency.md) | [Next](MarginLong.md)

# IMTConGroupSymbol::MarginRateCurrencyDefault

Get the default margin currency rate set for the symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    double  IMTConGroupSymbol::MarginRateCurrencyDefault()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginRateCurrencyDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateCurrencyDefault

### Note

Margin currency rate — rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble. The parameter is used when calculating security deposit for futures contracts ([Exchange FORTS Futures (#encalcmode)](../../Symbols/IMTConSymbol/Enumerations.md#encalcmode)) traded on Moscow Exchange (calculating variation margin and security deposit using the current USD exchange rate). The values are sent by the Moscow Exchange when using the gateway MetaTrader 5 to MOEX Derivatives.
